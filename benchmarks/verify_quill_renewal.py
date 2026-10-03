"""Check saved UI observations and exact inputs; not vendor-signed authorship proof."""
from datetime import datetime
from pathlib import Path
import hashlib
import json
import re

BASE = Path(__file__).resolve().parent
ROOT = BASE / 'quill-renewal'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normal(text):
    return re.sub(r'\s+', ' ', text).strip()


def path_in(root, relative):
    path = (root / relative).resolve()
    assert path.is_relative_to(root.resolve()), relative
    return path


def verify():
    data = json.loads((ROOT / 'results.json').read_text('utf-8'))
    records = data['records']
    assert len({r['id'] for r in records}) == len(records) == data['new_observation_count']
    for rec in records:
        assert rec['status'] == 'completed' and rec['input_verified_in_dom'] is True
        when = datetime.fromisoformat(rec['observed_at'].replace('Z', '+00:00'))
        source = path_in(ROOT, rec['input_path'])
        receipt = path_in(ROOT, rec['receipt'])
        assert digest(source) == rec['input_sha256']
        assert digest(receipt) == rec['receipt_sha256']
        submitted = source.read_text('utf-8').strip()
        assert hashlib.sha256(submitted.encode()).hexdigest() == rec['submitted_sha256']
        observation = json.loads((ROOT / 'observations' / (rec['id'] + '.json')).read_text('utf-8'))
        derived = {'status', 'receipt_sha256', 'input_dom_receipt_sha256'}
        assert observation == {k: v for k, v in rec.items() if k not in derived}
        raw = receipt.read_text('utf-8')
        if rec['vendor'] == 'QuillBot':
            assert 'Outdated score' not in raw and 'Detect AI' in raw
            for field, label in [('ai', 'AI-generated'), ('refined', 'Human-written & AI-refined'), ('human', 'Human-written')]:
                assert int(re.search(re.escape(label) + r'\s+(\d+)%', raw)[1]) == rec[field]
            assert rec['ai'] + rec['human'] + rec['refined'] == 100
            assert rec['metric'] == 'Human-written text percentage'
            assert re.search(r'Model (v[\d.]+)', raw)[1] == rec['model']
            quota = re.search(r'got (\d+) AI scans? left', raw)
            assert (int(quota[1]) if quota else 0) == rec['remaining_scans']
            if not quota:
                assert 'No free AI scans left' in raw
            dompath = path_in(ROOT, rec['input_dom_receipt'])
            assert digest(dompath) == rec['input_dom_receipt_sha256']
            dom = json.loads(dompath.read_text('utf-8'))
            for phase in ['before', 'after']:
                assert normal(dom[phase]['text']) == normal(submitted), (rec['id'], phase)
            before = datetime.fromisoformat(dom['before']['observed_at'].replace('Z', '+00:00'))
            after = datetime.fromisoformat(dom['after']['observed_at'].replace('Z', '+00:00'))
            assert before <= when == after
        elif rec['vendor'] == 'GPTZero':
            assert 'Text up-to-date' in raw and 'heading Basic Scan' in raw
            for field, label in [('ai', 'AI'), ('human', 'Human'), ('mixed', 'Mixed')]:
                assert int(re.search(r'button ' + label + r' (\d+)%', raw)[1]) == rec[field]
            assert rec['ai'] + rec['human'] + rec['mixed'] == 100
            assert rec['metric'] == 'Human document probability'
            assert re.search(r'Model\s+(\S+)', raw)[1] == rec['model']
        else:
            raise AssertionError(rec['vendor'])
        assert rec['score'] == rec['human'] and 0 <= rec['score'] <= 100

    # Link each displayed pair to its own exact text and original observation date.
    for doc in data['documents']:
        assert digest(path_in(ROOT, doc['input_path'])) == doc['sha256']
        outcomes = []
        for key, vendor in [('gptzero', 'GPTZero'), ('quillbot', 'QuillBot')]:
            result = doc[key]
            result_path = path_in(BASE, result['results_path'])
            linked = json.loads(result_path.read_text('utf-8'))['records']
            rec = next(r for r in linked if r['id'] == result['record_id'])
            assert rec['vendor'] == vendor and rec['input_sha256'] == doc['sha256']
            assert digest(path_in(result_path.parent, rec['input_path'])) == doc['sha256']
            for field in ['score', 'model', 'metric', 'observed_at', 'status']:
                assert rec[field] == result[field], (doc['id'], key, field)
            assert result['target_met'] == (rec['score'] >= 50)
            if vendor == 'GPTZero':
                raw = path_in(result_path.parent, rec['receipt']).read_text('utf-8')
                assert doc['gptzero_short_text_warning'] == ('This text is under 100 words' in raw)
            outcomes.append(result['target_met'])
        assert doc['both_selected_targets_met'] == all(outcomes)
    assert data['all_selected_targets_met'] == all(d['both_selected_targets_met'] for d in data['documents'])
    assert data['production_release'] == '1.6.0' and data['skill_changed'] is False
    prior_phases = ['2026-10-02', '2026-10-02-v15', 'additional-trial', 'deeper-trial',
                    'renewal-trial', 'continuation-e', 'continuation-g', 'feature-trial']
    prior_count = 0
    for phase in prior_phases:
        previous = json.loads((BASE / phase / 'results.json').read_text('utf-8'))['records']
        assert all(r['status'] == 'completed' for r in previous)
        prior_count += len(previous)
    assert data['prior_observation_count'] == prior_count == 166
    assert data['cumulative_observation_count'] == prior_count + len(records)
    hashes = json.loads((BASE / 'feature-trial/release-skill-hashes.json').read_text('utf-8'))
    skill = BASE.parent / 'skills/bilingual-humanizer'
    actual = {p.relative_to(skill).as_posix(): digest(p) for p in skill.rglob('*')
              if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc'}
    assert actual == hashes
    frozen = json.loads((ROOT / 'frozen-inputs.json').read_text('utf-8'))
    for relative, expected in frozen.items():
        assert digest(path_in(ROOT, relative)) == expected, relative
    vendor = ROOT / 'vendor'
    ud = json.loads((vendor / 'undetectable-observation.json').read_text('utf-8'))
    for field, hashfield in [('source_path', 'source_sha256'), ('output_path', 'output_sha256')]:
        path = (vendor / ud[field]).resolve()
        assert path.is_relative_to(ROOT.resolve()) and digest(path) == ud[hashfield]
    assert ud['independent_detector_score'] is None and ud['paid_action'] is False
    assert ud['mode'] == 'Basic / General Writing / Undetectable switch off'
    raw = (vendor / 'undetectable-ko-library-receipt.txt').read_text('utf-8')
    assert 'button Basic' in raw and 'button General Writing' in raw and 'switch 0' in raw
    selfscore = re.search(r'text (\d+) %\s*\n\s*\d+ text AI / GPT', raw)
    assert ud['vendor_self_score'] == {'metric': 'AI / GPT', 'value': int(selfscore[1])}
    assert normal((vendor / ud['output_path']).read_text('utf-8')) in normal(raw)
    limit = json.loads((vendor / 'quillbot-limit-observation.json').read_text('utf-8'))
    limit_source = (vendor / limit['source_path']).resolve()
    assert limit_source.is_relative_to(ROOT.resolve()) and digest(limit_source) == limit['source_sha256']
    assert limit['status'] == 'blocked_word_limit' and limit['output_accepted'] is False and limit['paid_action'] is False
    assert limit['displayed_limit'] in (vendor / 'quillbot-limit-receipt.txt').read_text('utf-8')
    assert limit['language'] in (vendor / 'quillbot-language-receipt.txt').read_text('utf-8')
    assert not any(r['input_sha256'] == ud['output_sha256'] for r in records)
    print(f'PASS: {len(records)} new QuillBot/GPTZero observations, {len(data["documents"])} exact-text pairs, DOM inputs and retained v1.6.0.')


if __name__ == '__main__':
    verify()
