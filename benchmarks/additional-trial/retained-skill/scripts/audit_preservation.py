"""Offline surface comparison. This is neither an AI detector nor semantic proof."""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys

NUMBER = r"[+\-−]?(?:(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?|\.\d+)(?:[eE][+\-]?\d+)?"
NUMBERS = re.compile(r"(?<![\d.])" + NUMBER + r"(?:[%％‰])?")
UNITS = r"(?:percentage\s+points?|percent|퍼센트포인트|퍼센트|%p|％|%|‰|°[CF]|℃|℉|ms|µs|μs|ns|s|min|hours?|days?|MHz|GHz|Hz|KiB|MiB|GiB|KB|MB|GB|TB|bytes?|tokens?|mL|ml|kg|mg|cm|mm|km|m|g|W|kW|V|USD|KRW|EUR|명|건|개|회|배|원|달러|초|분|시간|일|주|개월|월|년)"
QUANTITIES = re.compile(r"(?<![\d.])(?:[$€£₩]\s*)?" + NUMBER + r"\s*" + UNITS + r"(?![A-Za-z])", re.IGNORECASE)
URLS = re.compile(r"https?://[^\s<>\"`]+")
INLINE = re.compile(r"(`+)([^`\n]+?)\1")
CITATIONS = re.compile(r"\[(?:\^[-\w]+|@[^\]\n]+|\d+(?:\s*[,;–-]\s*\d+)*)\]")
QUOTES = re.compile(r'“[^”\n]+”|"[^"\n]+"|「[^」\n]+」|『[^』\n]+』')
WATCHED = {"\u200b", "\u200c", "\u2060", "\ufeff", "\u00ad", "\u202a", "\u202b", "\u202d", "\u202e", "\u2066", "\u2067", "\u2068", "\u2069"}


def fence_parts(text: str) -> tuple[list[str], str]:
    """Recognize common backtick/tilde fences without rewriting their contents."""
    blocks, prose, buffer = [], [], []
    marker = None
    for line in text.splitlines(keepends=True):
        opening = re.match(r"^ {0,3}(`{3,}|~{3,})", line)
        if marker is None and opening:
            marker = opening.group(1)
            buffer = [line]
        elif marker is not None:
            buffer.append(line)
            if re.match(r"^ {0,3}" + re.escape(marker[0]) + "{" + str(len(marker)) + r",}\s*$", line):
                blocks.append(''.join(buffer).rstrip('\r\n'))
                marker = None
                buffer = []
                prose.append('\n')
        else:
            prose.append(line)
    if buffer:
        blocks.append(''.join(buffer).rstrip('\r\n'))
    return blocks, ''.join(prose)


def url_values(text: str) -> list[str]:
    values = []
    for match in URLS.finditer(text):
        value = match.group().rstrip('.,;:!?')
        # A Markdown closing parenthesis is not part of its destination.
        while value.endswith(')') and value.count(')') > value.count('('):
            value = value[:-1]
        while value.endswith(']') and value.count(']') > value.count('['):
            value = value[:-1]
        values.append(value)
    return values


def features(text: str) -> dict[str, Counter]:
    blocks, prose = fence_parts(text)
    inline = [m.group(0) for m in INLINE.finditer(prose)]
    quoted_blocks = [line for line in prose.splitlines() if re.match(r'^ {0,3}>', line)]
    return {
        'numbers': Counter(NUMBERS.findall(text)),
        'quantities': Counter(QUANTITIES.findall(text)),
        'urls': Counter(url_values(text)),
        'citations': Counter(CITATIONS.findall(prose)),
        'fenced_code': Counter(blocks),
        'inline_code': Counter(inline),
        'quoted_spans': Counter(QUOTES.findall(prose)),
        'blockquote_lines': Counter(quoted_blocks),
    }


def audit(source: str, rewrite: str, protected: list[str] | None = None) -> dict:
    a, b = features(source), features(rewrite)
    flags = []
    for category in a:
        removed, added = a[category] - b[category], b[category] - a[category]
        if removed or added:
            flags.append({'category': category, 'removed': dict(removed), 'added': dict(added)})
    for term in dict.fromkeys(protected or []):
        before, after = source.count(term), rewrite.count(term)
        if before == 0:
            flags.append({'category': 'protection_not_in_source', 'text': term})
        elif before != after:
            flags.append({'category': 'protected_text', 'text': term, 'source_count': before, 'rewrite_count': after})
    introduced = Counter(c for c in rewrite if c in WATCHED) - Counter(c for c in source if c in WATCHED)
    if introduced:
        flags.append({'category': 'added_control_characters', 'codepoints': {f'U+{ord(c):04X}': n for c, n in introduced.items()}})
    return {
        'status': 'review_required' if flags else 'no_surface_change_found',
        'semantic_review_required': True,
        'authorship_assessed': False,
        'source_sha256': hashlib.sha256(source.encode('utf-8')).hexdigest(),
        'rewrite_sha256': hashlib.sha256(rewrite.encode('utf-8')).hexdigest(),
        'source_characters': len(source),
        'rewrite_characters': len(rewrite),
        'review_candidates': flags,
        'limitations': 'Inventories cannot establish semantic fidelity, factual truth, or authorship. Review meaning and document structure separately.',
    }


def same_file(a: Path, b: Path) -> bool:
    """Compare resolved paths and existing file identity, including hard links."""
    return a.resolve() == b.resolve() or (a.exists() and b.exists() and a.samefile(b))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('rewrite', type=Path)
    parser.add_argument('--protect-json', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    try:
        # Keep byte hashes distinct from normalized text used in comparisons.
        source_bytes, rewrite_bytes = args.source.read_bytes(), args.rewrite.read_bytes()
        source = source_bytes.decode('utf-8-sig').replace('\r\n', '\n')
        rewrite = rewrite_bytes.decode('utf-8-sig').replace('\r\n', '\n')
        if '\x00' in source or '\x00' in rewrite:
            raise ValueError('Expected UTF-8 text, not binary document content')
        protected = []
        if args.protect_json:
            data = json.loads(args.protect_json.read_text(encoding='utf-8-sig'))
            protected = data.get('protected') if isinstance(data, dict) else data
            if not isinstance(protected, list) or not all(isinstance(x, str) and x for x in protected):
                raise ValueError('Protection JSON must be an array of nonempty strings or an object with a protected array')
        result = audit(source, rewrite, protected)
        result['source_sha256'] = hashlib.sha256(source_bytes).hexdigest()
        result['rewrite_sha256'] = hashlib.sha256(rewrite_bytes).hexdigest()
        result['hash_basis'] = 'original file bytes; comparisons normalize UTF-8 BOM and CRLF'
        output = json.dumps(result, ensure_ascii=False, indent=2) + '\n'
        if args.output:
            if any(same_file(args.output, path) for path in (args.source, args.rewrite)):
                raise ValueError('The report must not overwrite either input file')
            if args.protect_json and same_file(args.output, args.protect_json):
                raise ValueError('The report must not overwrite the protection file')
            args.output.write_text(output, encoding='utf-8')
        else:
            if hasattr(sys.stdout, 'reconfigure'):
                sys.stdout.reconfigure(encoding='utf-8')
            sys.stdout.write(output)
        return 1 if result['review_candidates'] else 0
    except (OSError, UnicodeError, ValueError) as exc:
        parser.exit(2, f'Input/output error: {exc}\n')


if __name__ == '__main__':
    raise SystemExit(main())
