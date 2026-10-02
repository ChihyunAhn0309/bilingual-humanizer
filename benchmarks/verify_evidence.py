"""Check local evidence integrity, not vendor authenticity or authorship."""
from pathlib import Path
import json, hashlib

BASE=Path(__file__).resolve().parent/'2026-10-02'
data=json.loads((BASE/'results.json').read_text(encoding='utf-8'))
seen=set()
for record in data['records']:
    key=(record['service'],record['case'],record['variant'])
    assert key not in seen, f'Duplicate observation: {key}'
    seen.add(key)
    assert record['status']=='completed'
    assert 0 <= record['displayed_ai_percent'] <= 100
    assert record.get('truncated') is not True
    for field, hashfield in [('input_file','input_sha256'),('receipt','receipt_sha256')]:
        path=(BASE/record[field]).resolve()
        assert path.is_relative_to(BASE.resolve())
        assert hashlib.sha256(path.read_bytes()).hexdigest()==record[hashfield], str(path)
    if record['service']=='GPTZero' and record.get('transport')=='authenticated Basic Scan UI':
        receipt=(BASE/record['receipt']).read_text(encoding='utf-8')
        assert 'Text up-to-date' in receipt
        assert f'AI {record["displayed_ai_percent"]}%' in receipt
print(f'PASS: {len(seen)} unique observations; input and receipt hashes match.')

