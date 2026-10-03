"""Read-only checks of the frozen first comparison; never runs inference."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
OUT = Path(__file__).resolve().parent
checks = []


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def check(label, condition):
    checks.append({"check": label, "passed": bool(condition)})


def pointers(obj, root, prefix):
    if isinstance(obj, dict):
        if "path" in obj and "sha256" in obj:
            p = Path(obj["path"])
            if not p.is_absolute():
                p = root / p
            check(prefix + " pointer " + str(obj["path"]), p.is_file() and digest(p) == obj["sha256"])
        for key, value in obj.items():
            pointers(value, root, prefix + "/" + key)
    elif isinstance(obj, list):
        for i, value in enumerate(obj):
            pointers(value, root, prefix + "/" + str(i))


def ledger_check(path, text_path, native_path=None):
    doc = load(path)
    text = text_path.read_text(encoding="utf-8")
    label = str(path.relative_to(BASE))
    check(label + " exact input", doc["text_sha256"] == digest(text_path))
    coverage = doc["coverage"]
    check(label + " all paragraphs reviewed", coverage["paragraphs_total"] == coverage["paragraphs_reviewed"] and coverage["paragraphs_excluded"] == 0)
    check(label + " six dimensions", len(doc["document_analysis"]) == 6 and all(doc["document_analysis"].values()))
    check(label + " history unauthenticated", doc["authorship_probabilities"] is None)
    for p in doc["paragraph_reviews"]:
        check(label + " paragraph " + p["paragraph_id"], p["status"] == "reviewed" and text[p["start"]:p["end"]] == p["text"])
    for f in doc["findings"]:
        check(label + " finding fields " + f["id"], all(f.get(k) for k in ("observation", "interpretation", "human_alternative", "discriminating_evidence", "basis")))
        for i, span in enumerate(f["spans"]):
            check(label + " span " + f["id"] + "/" + str(i), text[span["start"]:span["end"]] == span["quote"])
    if native_path:
        native = load(native_path)
        check(label + " actual four classes", doc["measured_output"]["class_probabilities"] == native["document_class_probabilities"])
    return {"file": label, "paragraphs": coverage["paragraphs_total"], "findings": len(doc["findings"])}


def measurement_check(score_dir, text_path):
    native = load(score_dir / "model-result.json")
    adapter = load(score_dir / "feedback.json")
    execution = load(score_dir / "execution.json")
    label = str(score_dir.relative_to(BASE))
    expected = digest(text_path)
    check(label + " exact original/input/native/adapter/execution", expected == digest(score_dir / "input.txt") == native["text_sha256"] == adapter["input_sha256"] == execution["input_sha256"])
    check(label + " completed subprocesses", execution["status"] == "completed" and all(c["returncode"] == 0 for c in execution["calls"]))
    check(label + " serialized successful worker", native["execution_guard"]["worker_exit_code"] == 0 and native["execution_guard"]["serialized_cli"])
    check(label + " complete one-window coverage", native["all_input_tokens_scored"] and len(native["windows"]) == 1)
    check(label + " four classes unchanged", native["document_class_probabilities"] == adapter["native_class_probabilities"])
    check(label + " Human percent exact", 100 * native["document_class_probabilities"]["human"] == adapter["human_percent"])
    check(label + " raw result binding", adapter["raw_result_sha256"] == digest(score_dir / "model-result.json"))
    check(label + " zero external calls", native["external_detector_calls"] == 0 and adapter["external_detector_calls"] == 0)
    return {"file": label, "input_sha256": expected, "Human_percent": adapter["human_percent"], "model": native["model"], "revision": native["revision"], "weight_sha256": native["weight_sha256"], "at": native["measured_at_utc"]}


manifests = {}
for name, directory in [("baseline-skill-hashes.json", "baseline-skill"), ("prototype-skill-hashes.json", "skill")]:
    manifest = load(BASE / name)
    manifests[directory] = manifest
    for file, value in manifest.items():
        check(directory + "/" + file, digest(BASE / directory / file) == value)
    check(directory + " manifest covers all files", {p.relative_to(BASE / directory).as_posix() for p in (BASE / directory).rglob("*") if p.is_file()} == set(manifest))

changed = [p for p, h in manifests["baseline-skill"].items() if manifests["skill"].get(p) != h]
check("only intended three skill files changed", set(changed) == {"SKILL.md", "references/english-composition.md", "references/english-reference-review.md"})
freeze = load(BASE / "METHOD-FREEZE.json")
check("prototype manifest freeze", digest(BASE / "prototype-skill-hashes.json") == freeze["manifest_sha256"])

comparison = load(BASE / "transfer-comparison.json")
pointers(comparison, BASE, "comparison")
for name, directory in [("complete-feedback-manifest.json", "candidate-feedback")]:
    for file, value in load(BASE / directory / name)["files"].items():
        check(directory + " manifest " + file, digest(BASE / directory / file) == value)

measurements = []
ledgers = []
for case in comparison["cases"]:
    cid = case["case"]
    for arm in ("source", "baseline", "prototype"):
        record = case[arm]
        text_path = BASE / record["candidate"]["path"]
        score_dir = (BASE / record["native"]["path"]).parent
        measurements.append(measurement_check(score_dir, text_path))
        check(cid + "/" + arm + " summary classes", record["classes"] == load(score_dir / "model-result.json")["document_class_probabilities"])
        if arm == "source":
            ledger_path = BASE / "transfer-reviews" / (cid + ".validated-full.json")
        else:
            alias = record["alias"]
            ledger_path = BASE / "candidate-feedback" / cid / alias / "validated-full.json"
            check(cid + "/" + arm + " blind pair bytes", digest(text_path) == digest(BASE / "blind-pairs" / cid / (alias + ".txt")))
            triage = load(ledger_path.parent / "triage.json")
            check(cid + "/" + arm + " all findings triaged", {f["id"] for f in triage["findings"]} == {f["id"] for f in load(ledger_path)["findings"]})
            check(cid + "/" + arm + " no accepted repair hidden", all(f["action"] == "retain" for f in triage["findings"]))
        ledgers.append(ledger_check(ledger_path, text_path, score_dir / "model-result.json"))
    check(cid + " delta arithmetic", case["prototype_minus_baseline_pp"] == case["prototype"]["human_percent"] - case["baseline"]["human_percent"])

for case in ("policy-note", "exhibition-review"):
    root = BASE / "development" / case
    session = load(root / "session.json")
    pointers(session, root, "development/" + case)
    for rnd in session["rounds"]:
        if rnd["native"]:
            native_path = root / rnd["native"]["path"]
            text_path = root / rnd["candidate"]["path"]
            measurements.append(measurement_check(native_path.parent, text_path))
            ledgers.append(ledger_check(root / rnd["review"]["path"], text_path, native_path))

check("one model and pinned weights across 15 frozen document submissions", len({(m["model"], m["revision"], m["weight_sha256"]) for m in measurements}) == 1 and len(measurements) == 15)
blind = load(BASE / "blind-review/round-1.json")
candidate_times = [m["at"] for m in measurements if m["file"].startswith("transfer-scores") and not m["file"].endswith("source")]
check("blind review timestamp before all candidate scores", all(blind["reviewed_at_utc"] < t for t in candidate_times))

result = {"audited_at_utc": datetime.now(timezone.utc).isoformat(), "scope": "Frozen development and first eligible transfer comparison only. No inference or later continuation evaluation.", "checks_passed": sum(c["passed"] for c in checks), "checks_total": len(checks), "failures": [c for c in checks if not c["passed"]], "changed_skill_files": changed, "measurements": measurements, "ledgers": ledgers, "all_checks": checks, "limits": "Hash, field and anchor consistency do not authenticate a run independently or prove semantic judgments. Source/candidate semantics were separately reviewed by the auditor."}
(OUT / "frozen-integrity-checks.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({k: result[k] for k in ("checks_passed", "checks_total", "failures", "changed_skill_files")}, indent=2))
