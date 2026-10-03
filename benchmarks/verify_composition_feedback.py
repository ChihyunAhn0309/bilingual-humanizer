"""Check exact inputs, native scores, review coverage and the recorded selection."""
from pathlib import Path
import hashlib
import importlib.util
import json

REPO = Path(__file__).resolve().parents[1]
ROOT = REPO / 'benchmarks/composition-feedback'


def read(path):
    return json.loads(path.read_text('utf-8'))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def safe(relative):
    path = (ROOT / relative).resolve()
    assert path.is_relative_to(ROOT.resolve()), relative
    return path


def verify_review(record, measured):
    source = safe(record['input'])
    text = source.read_bytes().decode('utf-8')
    ledger, checked, index = (read(safe(record[k])) for k in ('ledger', 'validated', 'index'))
    assert ledger['text_sha256'] == checked['text_sha256'] == index['text_sha256'] == sha(source)
    paragraphs = index['paragraphs']
    originals = ledger['paragraph_reviews']
    reviews = checked['paragraph_reviews']
    assert len(paragraphs) == len(originals) == len(reviews) > 0
    cursor = 0
    for number, (paragraph, original, review) in enumerate(zip(paragraphs, originals, reviews), 1):
        assert paragraph['id'] == original['paragraph_id'] == review['paragraph_id'] == f'P{number}'
        start, end = paragraph['start'], paragraph['end']
        assert cursor <= start < end <= len(text) and not text[cursor:start].strip()
        assert text[start:end] == paragraph['text'] and paragraph['text'].strip()
        assert paragraph['line'] == text[:start].count('\n') + 1
        assert original['status'] == 'reviewed' and original['assessment'].strip()
        assert all(review.get(k) == v for k, v in original.items())
        assert all(review.get(k) == v for k, v in paragraph.items())
        cursor = end
    assert not text[cursor:].strip()
    coverage = checked['coverage']
    assert coverage['paragraphs_total'] == coverage['paragraphs_reviewed'] == len(paragraphs)
    assert coverage['paragraphs_excluded'] == 0 and coverage['review_fraction'] == 1
    findings = ledger['findings']
    assert len(findings) == len(checked['findings']) == len({f['id'] for f in findings})
    ids = {f['id'] for f in findings}
    assert all(set(r['finding_ids']) <= ids for r in originals)
    for original, review in zip(findings, checked['findings']):
        assert original['human_alternative'] and original['interpretation']
        assert all(review.get(k) == v for k, v in original.items() if k != 'spans')
        assert len(original['spans']) == len(review['spans'])
        for span, validated_span in zip(original['spans'], review['spans']):
            assert all(validated_span.get(k) == v for k, v in span.items())
            assert 0 <= span['start'] < span['end'] <= len(text)
            assert text[span['start']:span['end']] == span['quote']
    normalized = measured[sha(source)]
    native = normalized['_native_receipt']
    expected_measurement = {
        'mode': native['mode'], 'model': normalized['model'],
        'measured_at_utc': normalized['measured_at_utc'],
        'class_probabilities': normalized['native_class_probabilities'],
        'model_sha256': normalized['model_sha256'],
        'calibration': native.get('calibration'),
        'applicability_cautions': native.get('applicability_cautions', []),
        'revision': native.get('revision'), 'language_scope': native.get('language_scope'),
        'independently_calibrated_here': native.get('independently_calibrated_here'),
        'validation_status': native.get('validation_status'),
        'known_limitations': native.get('known_limitations', native.get('known_limits', [])),
        'semantics': 'Model-estimated class probabilities, not verified writing history; exact input hash matched.'}
    assert checked['measured_output'] == expected_measurement
    assert ledger.get('authorship_probabilities') is None and checked.get('authorship_probabilities') is None


def verify():
    manifest = read(ROOT / 'frozen-files.json')
    actual = {p.relative_to(ROOT).as_posix(): sha(p) for p in ROOT.rglob('*')
              if p.is_file() and p.name != 'frozen-files.json' and '__pycache__' not in p.parts}
    assert actual == manifest, 'Frozen experiment evidence changed'
    spec = importlib.util.spec_from_file_location('composition_adapter', REPO / 'skills/bilingual-humanizer/scripts/local_feedback.py')
    adapter = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(adapter)
    results = read(ROOT / 'results.json')
    assert results['detector_version'] == '3.1.2'
    assert {r['directory'] for r in results['measurements']} == {
        'en-archive/candidate-a-score', 'en-archive/candidate-b-score',
        'ko-library/candidate-a-score', 'fresh-en/source-score', 'fresh-en/candidate-a-score'}
    assert len(results['measurements']) == 5
    assert results['external_detector_calls'] == results['paid_actions'] == 0
    assert results['authorship_verified'] is results['commercial_transfer_measured'] is False
    manifest = read(ROOT / 'release-skill-hashes.json')
    active = REPO / 'benchmarks/english-focus/retained-skill'
    assert {p.relative_to(active).as_posix(): sha(p) for p in active.rglob('*')
            if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc'} == manifest
    assert f'version: "{results["release_version"]}"' in (active / 'SKILL.md').read_text('utf-8')
    eligibility = read(ROOT / 'independent-candidate-review.json')
    assert eligibility['blinding']['new_candidate_scores_read'] is False
    for candidate in eligibility['candidate_reviews']:
        candidate_path = safe(candidate['candidate_path'].split('work/composition-feedback/', 1)[1])
        source_path = safe(candidate['source_path'].split('work/composition-feedback/', 1)[1])
        assert sha(candidate_path) == candidate['candidate_sha256']
        assert sha(source_path) == candidate['source_sha256']
        assert candidate['eligible_for_scoring'] is True and candidate['requires_repair_before_scoring'] is False
        for check in candidate['fidelity_checks']:
            for label, path in [('source_spans', source_path), ('candidate_spans', candidate_path)]:
                text = path.read_bytes().decode('utf-8')
                for span in check.get(label, []):
                    assert 0 <= span['start'] < span['end'] <= len(text)
                    assert text[span['start']:span['end']] == span['quote']
    fresh_review = read(ROOT / 'fresh-independent-review.json')
    assert fresh_review['eligibility_for_scoring']['eligible'] is True
    assert not fresh_review['eligibility_for_scoring']['required_repairs']
    assert fresh_review['blinding']['status'] == 'maintained'
    for key in ('source', 'candidate'):
        item = fresh_review[key]
        path = safe(item['path'].split('work/composition-feedback/', 1)[1])
        assert sha(path) == item['sha256'].lower()
    measured = {}
    for record in results['measurements']:
        directory = safe(record['directory'])
        source = directory / 'input.txt'
        native = read(directory / 'model-result.json')
        feedback = read(directory / 'feedback.json')
        execution = read(directory / 'execution.json')
        normalized = adapter.normalize(native, source.read_bytes(), record['language'])
        assert all(feedback.get(key) == value for key, value in normalized.items()), record['directory']
        assert feedback['status'] == execution['status'] == 'completed'
        assert execution['input_sha256'] == sha(source) == record['input_sha256']
        assert all(call['returncode'] == 0 for call in execution['calls'])
        for key in ('input_sha256', 'native_class_probabilities', 'human_percent', 'measured_at_utc', 'scope'):
            assert normalized[key] == feedback[key] == record[key], (record['directory'], key)
        assert feedback['raw_result_sha256'] == sha(directory / 'model-result.json')
        assert feedback['cautions'] == normalized['cautions'] and feedback['authorship_verified'] is False
        assert record['scope'] == 'whole_document'
        if record['language'] == 'en':
            assert native['weight_loading_backend'] == 'pread'
        measured[sha(source)] = normalized | {'_native_receipt': native}
    for record in results['reviews']:
        verify_review(record, measured)
    assert {sha(safe(r['input'])) for r in results['reviews']} == set(measured)
    for record in results['selections']:
        source = safe(record['selected_input'])
        assert sha(source) == record['selected_sha256']
        evidence = (REPO / record['score_record']).resolve()
        assert evidence.is_relative_to(REPO.resolve())
        feedback = read(evidence)
        assert feedback['input_sha256'] == sha(source)
        assert feedback['human_percent'] == record['human_percent']
    assert results['all_selected_human_ge_50_targets_met'] == all(r['human_percent'] >= 50 for r in results['selections'])
    print(f'PASS: {len(measured)} new exact local measurements, complete reviews, frozen experiment and selected checkpoint scores.')


if __name__ == '__main__':
    verify()
