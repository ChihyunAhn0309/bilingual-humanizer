#!/usr/bin/env python3
"""Offline identity and experiment-structure checks for continuation G."""
from __future__ import annotations
import hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent / "continuation-g"

def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main() -> None:
    manifest = json.loads((ROOT / "frozen-inputs.json").read_text(encoding="utf-8"))
    assert manifest["schema_version"] == 1
    listed = set()
    for item in manifest["files"]:
        path = ROOT / item["path"]
        assert path.is_file(), item["path"]
        assert len(path.read_bytes()) == item["bytes"], item["path"]
        assert digest(path) == item["sha256"], item["path"]
        listed.add(item["path"])
    expected = {
        f"{group}/{name}.txt"
        for group in ("sources", "baseline", "challenger", "final")
        for name in ("ko-neighborhood", "ko-review", "en-incident", "en-letter")
    } | {"drafts/en-incident-g-v1.txt"}
    expected |= {f"final/{name}.txt" for name in ("ko-neighborhood", "ko-review", "en-incident", "en-letter")}
    assert listed == expected
    for name in ("ko-neighborhood", "ko-review", "en-incident", "en-letter"):
        hashes = {digest(ROOT / group / f"{name}.txt") for group in ("sources", "baseline", "challenger")}
        assert len(hashes) == 3, f"arms unexpectedly identical: {name}"
    # Protected numeric and proper-name surface checks supplement, but do not replace,
    # semantic review.
    protected = {
        "ko-neighborhood": ["토요일", "오전 9시", "11시", "금요일", "오후 6시", "세 구역", "네 명"],
        "ko-review": ["열두 장", "첫", "두 번째", "두 번", "세 단계", "마지막"],
        "en-incident": ["14:20", "10,000", "14:47", "15:05", "Monday", "16:10", "25", "16:35", "Friday"],
        "en-letter": ["Programme Committee", "Small Archives, Shared Tools", "June", "May 12", "autumn", "Mara Ellis"],
    }
    for name, tokens in protected.items():
        for group in ("baseline", "challenger", "final"):
            text = (ROOT / group / f"{name}.txt").read_text(encoding="utf-8")
            for token in tokens:
                assert token in text, (group, name, token)
    print("PASS: 17 frozen source/candidate/final/history files; 4 paired holdouts; protected surfaces present.")

if __name__ == "__main__":
    main()
