"""Bind manually written development reviews to exact text; no model or prose generation."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys

case, name = Path(sys.argv[1]), sys.argv[2]
score = case / (name + '-score')
review = case / (name + '-review')
plan = json.loads((case / (name + '-review-plan.json')).read_text(encoding='utf-8'))
text = (score / 'input.txt').read_bytes().decode('utf-8')
index = json.loads((score / 'index.json').read_text(encoding='utf-8'))
feedback = json.loads((score / 'feedback.json').read_text(encoding='utf-8'))
paragraphs = {p['id']: p for p in index['paragraphs']}
review.mkdir(exist_ok=False)

def span(quote):
    if quote in paragraphs:
        p = paragraphs[quote]
        return {'start': p['start'], 'end': p['end'], 'quote': p['text']}
    assert text.count(quote) == 1, ('ambiguous or absent quote', quote)
    start = text.index(quote)
    return {'start': start, 'end': start + len(quote), 'quote': quote}

findings, triage = [], []
for f in plan['findings']:
    item = {k: v for k, v in f.items() if k not in ('quotes', 'decision', 'reason')}
    item['spans'] = [span(q) for q in f['quotes']]
    findings.append(item)
    triage.append({'finding_id': f['id'], 'decision': f['decision'], 'reason': f['reason']})
occlusion = feedback.get('measured_evidence', {}).get('occlusion', {})
measured = [p for p in occlusion.get('paragraphs', []) if p.get('status') == 'measured']
if measured:
    p = max(measured, key=lambda p: abs(p['delta_percentage_points']))
    findings.append({'id': 'M', 'basis': 'local_occlusion', 'direction': 'neutral', 'strength': 'weak',
        'spans': [span(p['paragraph_id'])],
        'observation': f"Largest absolute paragraph-deletion sensitivity: {p['paragraph_id']}. Baseline AI-involvement={p['baseline_ai_involvement']}; after deletion={p['after_removal_ai_involvement']}; delta={p['delta_percentage_points']} percentage points.",
        'interpretation': 'Measured context/length sensitivity, not paragraph authorship probability or proof of a defective phrase. Reviewed this paragraph in the whole document.',
        'human_alternative': 'Conventional human prose can receive high-confidence false positives on this experimental model; deleting text also changes context and length.',
        'discriminating_evidence': 'A complete faithful alternative can test model response but cannot authenticate writing history.',
        'source_record': str((score / 'model-result.json').resolve())})
    triage.append({'finding_id': 'M', 'decision': 'retain', 'reason': 'Retain the complete information; inspect sensitivity without deleting the paragraph or inventing a defect.'})
findings.append({'id': 'H', 'basis': 'documented_history', 'direction': 'ai_like', 'strength': 'moderate',
    'spans': [span('P1')], 'observation': 'New AI-origin synthetic source and AI-authored development rewrites, created for this experiment.',
    'interpretation': 'Known generation history is separate from naturalness and the uncalibrated native classes.',
    'human_alternative': 'A human could write similar prose; that possibility does not change this fixture creation record.',
    'discriminating_evidence': 'No claim is made that the described events occurred. Hashes identify exact artifacts, not authorship.',
    'source_record': str((case.parent / 'PROTOCOL.md').resolve())})
triage.append({'finding_id': 'H', 'decision': 'retain', 'reason': 'Preserve known AI-origin provenance regardless of scores.'})
ledger = {'text_sha256': index['text_sha256'], 'summary': plan['summary'], 'document_analysis': plan['document_analysis'],
          'findings': findings, 'paragraph_reviews': plan['paragraph_reviews'], 'review_method': 'Distinct same-context self-review by the writer; parent pre-score review saved separately where available.'}
ledger['paragraph_reviews'][0]['finding_ids'].append('H')
if measured:
    next(p for p in ledger['paragraph_reviews'] if p['paragraph_id'] == measured[max(range(len(measured)), key=lambda i: abs(measured[i]['delta_percentage_points']))]['paragraph_id'])['finding_ids'].append('M')
for filename, value in [('ledger.json', ledger), ('triage.json', triage)]:
    (review / filename).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
cmd = [sys.executable, '-B', '-X', 'utf8', str(Path.home()/'.codex/skills/bilingual-ai-detector/scripts/evidence.py'), 'validate', str(score/'input.txt'), str(review/'ledger.json'), '--out', str(review/'validated.json'), '--html', str(review/'analysis.html')]
if (score/'model-result.json').exists():
    cmd.extend(['--model-result', str(score/'model-result.json')])
subprocess.run(cmd, check=True)
print(json.dumps({'candidate_sha256': hashlib.sha256(text.encode('utf-8')).hexdigest(), 'review': str(review), 'human_percent': feedback['human_percent']}))
