"""Independent mutation checks of the release verifier, using isolated copies only."""
from contextlib import redirect_stdout
from datetime import datetime, timezone
import hashlib
import io
import json
from pathlib import Path
import runpy
import shutil
import tempfile
import traceback

import argparse
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--repository", type=Path, default=Path(__file__).resolve().parents[2])
parser.add_argument("--out", type=Path, default=Path.cwd() / "local-feedback-negative-recheck.json")
args = parser.parse_args()
SOURCE = args.repository.resolve()
OUT = args.out.resolve()
if OUT.is_relative_to((SOURCE / "benchmarks/local-feedback").resolve()):
    raise ValueError("Write recheck results outside the frozen evidence directory")


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rewrite_json(root, relative, mutate, refresh_manifest=True):
    path = root / relative
    data = json.loads(path.read_text("utf-8"))
    mutate(data)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if refresh_manifest:
        manifest_path = root / "frozen-files.json"
        manifest = json.loads(manifest_path.read_text("utf-8"))
        manifest[relative] = digest(path)
        manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def changed_score(root):
    rewrite_json(root, "results.json", lambda d: d["measurements"][0].update(human_percent=100.0))


def forged_failure_human(root):
    rewrite_json(root, "development/en-baseline-retry/feedback.json", lambda d: d.update(human_percent=100.0))


def bad_quote(root):
    rewrite_json(root, "fresh-check/round-0-source/ledger.json",
                 lambda d: d["findings"][0]["spans"][0].update(quote="Invented quotation"))


def bad_input_hash(root):
    rewrite_json(root, "results.json", lambda d: d["measurements"][0].update(input_sha256="0" * 64))


def changed_input_bytes(root):
    with (root / "development/ko-original.txt").open("ab") as stream:
        stream.write(b"changed source\n")


def missing_paragraph_review(root):
    rewrite_json(root, "fresh-check/round-0-source/ledger.json",
                 lambda d: d["paragraph_reviews"].pop())


def stale_validated_quote(root):
    rewrite_json(root, "fresh-check/round-0-source/validated.json",
                 lambda d: d["findings"][0]["spans"][0].update(quote="Invented validated quotation"))


cases = [("unchanged_copy", None, True), ("changed_reported_score", changed_score, False),
         ("forged_failure_human", forged_failure_human, False), ("bad_ledger_quote", bad_quote, False),
         ("bad_reported_input_hash", bad_input_hash, False), ("changed_source_bytes", changed_input_bytes, False),
         ("missing_paragraph_review_with_stale_validation", missing_paragraph_review, False),
         ("stale_validated_quote", stale_validated_quote, False)]
originals = {p: digest(p) for p in (SOURCE / "benchmarks/local-feedback").rglob("*")
             if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc"}
records = []
for name, mutation, should_pass in cases:
    with tempfile.TemporaryDirectory(prefix="humanizer-release-review-") as temporary:
        repo = Path(temporary) / "repo"
        root = repo / "benchmarks/local-feedback"
        shutil.copytree(SOURCE / "benchmarks/local-feedback", root, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        shutil.copytree(SOURCE / "skills/bilingual-humanizer", repo / "skills/bilingual-humanizer",
                        ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        verifier = repo / "benchmarks/verify_local_feedback.py"
        shutil.copy2(SOURCE / "benchmarks/verify_local_feedback.py", verifier)
        if mutation:
            mutation(root)
        captured = io.StringIO()
        try:
            with redirect_stdout(captured):
                runpy.run_path(str(verifier), run_name="__main__")
            passed, failure = True, None
        except Exception as error:
            passed = False
            failure = {"type": type(error).__name__, "message": str(error),
                       "location": traceback.extract_tb(error.__traceback__)[-1].line}
        records.append({"case": name, "expected_pass": should_pass, "actual_pass": passed,
                        "expected_outcome_observed": passed == should_pass,
                        "stdout": captured.getvalue().strip(), "failure": failure})

assert all(digest(path) == expected for path, expected in originals.items()), "Original evidence changed during this audit"
result = {"reviewed_at_utc": datetime.now(timezone.utc).isoformat(),
          "verifier_sha256": digest(SOURCE / "benchmarks/verify_local_feedback.py"),
          "method": "Each case copies evidence, current skill and verifier to a new temporary repository. Except for raw-byte integrity, mutations refresh the copied frozen-files manifest to exercise semantic consistency checks beyond a checksum mismatch. No original evidence or detector is altered; no inference is performed by these mutation checks.",
          "originals_unchanged": True, "cases": records}
if OUT.exists():
    previous = json.loads(OUT.read_text("utf-8"))
    history = previous.pop("previous_runs", [])
    result["previous_runs"] = history + [previous]
OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({k: v for k, v in result.items() if k != "previous_runs"}, ensure_ascii=False, indent=2))
