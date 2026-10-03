"""Verify local observation identity/metrics, not vendor authenticity or authorship."""
from pathlib import Path
from datetime import datetime
import hashlib
import json
import re

BASE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify(directory, expected):
    root = BASE / directory
    data = json.loads((root / 'results.json').read_text('utf-8'))
    ids = set()
    for rec in data['records']:
        assert rec['id'] not in ids
        ids.add(rec['id'])
        assert rec['status'] == 'completed' and rec['input_verified_in_dom'] is True
        datetime.fromisoformat(rec['observed_at'].replace('Z', '+00:00'))
        for field, hashfield in [('input_path', 'input_sha256'), ('receipt', 'receipt_sha256')]:
            p = (root / rec[field]).resolve()
            assert p.is_relative_to(root.resolve())
            assert sha(p) == rec[hashfield], (rec['id'], field)
        obs = json.loads((root / 'observations' / (rec['id'] + '.json')).read_text('utf-8'))
        assert obs == {k: v for k, v in rec.items() if k not in ['status', 'receipt_sha256']}
        submitted = (root / rec['input_path']).read_text('utf-8').strip()
        assert hashlib.sha256(submitted.encode()).hexdigest() == rec['submitted_sha256']
        raw = (root / rec['receipt']).read_text('utf-8')
        if rec['vendor'] == 'GPTZero':
            assert 'Text up-to-date' in raw and 'heading Basic Scan' in raw
            for field, label in [('ai', 'AI'), ('human', 'Human'), ('mixed', 'Mixed')]:
                assert int(re.search(r'button ' + label + r' (\d+)%', raw)[1]) == rec[field]
            assert rec['ai'] + rec['human'] + rec['mixed'] == 100
            assert re.search(r'Model\s+(\S+)', raw)[1] == rec['model']
            assert rec['metric'] == 'Human document probability'
        elif rec['vendor'] == 'QuillBot':
            assert 'Outdated score' not in raw
            for field, label in [('ai', 'AI-generated'), ('human', 'Human-written'), ('refined', 'Human-written & AI-refined')]:
                assert int(re.search(r'text ' + re.escape(label) + r'\r?\n[\s\S]*?text (\d+) %', raw)[1]) == rec[field]
            assert rec['ai'] + rec['human'] + rec['refined'] == 100
            assert re.search(r'Model (v[\d.]+)', raw)[1] == rec['model']
            assert rec['metric'] == 'Human-written text percentage'
            quota = re.search(r'got (\d+) AI scans? left', raw)
            assert (int(quota[1]) if quota else 0) == rec['remaining_scans']
            if not quota:
                assert 'No free AI scans left' in raw
        else:
            raise AssertionError(rec['vendor'])
        assert rec['score'] == rec['human'] and 0 <= rec['score'] <= 100
    assert len(ids) == expected
    assert data['all_selected_targets_met'] is False
    if directory == 'continuation-g':
        for doc in data['documents']:
            for key, vendor in [('gptzero', 'GPTZero'), ('quillbot', 'QuillBot')]:
                result = doc[key]
                rec = next(r for r in data['records'] if r['id'] == result['record_id'])
                assert rec['vendor'] == vendor and rec['input_path'] == doc['path']
                assert rec['input_sha256'] == doc['sha256']
                for field in ['score', 'model', 'metric', 'observed_at', 'receipt', 'status']:
                    assert result[field] == rec[field], (doc['document'], key, field)
                assert result['threshold'] == '>=50%'
                assert result['target_met'] == (rec['score'] >= 50)
    print(f'PASS: {expected} {directory} native detector observations, inputs, receipts and freshness.')


if __name__ == '__main__':
    verify('continuation-g', 8)
    verify('feature-trial', 4)
    root = BASE / 'feature-trial'
    frozen = json.loads((root / 'frozen-inputs.json').read_text('utf-8'))
    for rel, expected_hash in frozen.items():
        path = (root / rel).resolve()
        assert path.is_relative_to(root.resolve()) and sha(path) == expected_hash, rel
    release = json.loads((root / 'release-skill-hashes.json').read_text('utf-8'))
    skill = BASE / 'local-feedback/retained-skill'  # Exact v1.6.0 archive
    actual = {p.relative_to(skill).as_posix(): sha(p) for p in skill.rglob('*')
              if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc'}
    assert actual == release and len(release) == 24
    assert 'version: "1.6.0"' in (skill / 'SKILL.md').read_text('utf-8')
    for metadata, source, output in [
        ('observation.json', 'source-en-incident.txt', 'hix-en-incident.txt'),
        ('undetectable-observation.json', 'source-ko-neighborhood.txt', 'undetectable-ko-neighborhood.txt'),
    ]:
        rec = json.loads((root / 'vendor' / metadata).read_text('utf-8'))
        assert sha(root / 'vendor' / source) == rec['source_sha256']
        assert sha(root / 'vendor' / output) == rec['output_sha256']
        assert rec['independent_detector_score'] is None
    print('PASS: v1.6.0 release, frozen forward tests, two vendor outputs and archived reviews.')
