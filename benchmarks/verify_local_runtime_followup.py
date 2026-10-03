"""Verify the later successful English receipts without changing the earlier failures."""
from pathlib import Path
import hashlib
import importlib.util
import json

REPO = Path(__file__).resolve().parents[1]
ROOT = REPO / 'benchmarks/local-runtime-followup'
spec = importlib.util.spec_from_file_location('local_feedback', REPO / 'skills/bilingual-humanizer/scripts/local_feedback.py')
adapter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(adapter)


def read(path):
    return json.loads(path.read_text('utf-8'))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify():
    manifest = read(ROOT / 'frozen-files.json')
    for relative, expected in manifest.items():
        path = (ROOT / relative).resolve()
        assert path.is_relative_to(ROOT.resolve()) and sha(path) == expected, relative
    results = read(ROOT / 'results.json')
    assert results['external_detector_calls'] == results['paid_actions'] == 0
    assert results['commercial_transfer_measured'] is False
    assert results['detector_version'] == '3.1.2'
    assert len(results['measurements']) == 3
    assert {r['directory'] for r in results['measurements']} == {'en-original', 'en-revision-1', 'adapter-en-final'}
    assert results['authorship_verified'] is False
    assert results['all_selected_human_ge_50_targets_met'] == all(r['human_percent'] >= 50 for r in results['measurements'])
    scores = {}
    for record in results['measurements']:
        root = ROOT / record['directory']
        source, native = root / 'input.txt', read(root / 'model-result.json')
        normalized = adapter.normalize(native, source.read_bytes(), 'en')
        feedback = read(root / 'feedback.json')
        assert record['has_review'] == (record['directory'] != 'adapter-en-final')
        assert normalized['scope'] == 'whole_document'
        assert normalized['native_class_probabilities'] == feedback['native_class_probabilities'] == record['native_class_probabilities']
        assert normalized['human_percent'] == feedback['human_percent'] == record['human_percent']
        assert normalized['input_sha256'] == record['input_sha256'] == feedback['input_sha256']
        assert normalized['measured_at_utc'] == record['measured_at_utc'] == feedback['measured_at_utc']
        assert native['weight_loading_backend'] == 'pread'
        assert feedback['raw_result_sha256'] == sha(root / 'model-result.json')
        if record['producer'] == 'humanizer_adapter':
            execution = read(root / 'execution.json')
            assert execution['status'] == 'completed' and execution['input_sha256'] == record['input_sha256']
            assert all(call['returncode'] == 0 for call in execution['calls'])
        else:
            assert record['producer'] == 'detector_repair_session'
            execution = read(root / 'execution-from-detector-session.json')
            assert feedback['execution_record_sha256'] == sha(root / 'execution-from-detector-session.json')
            assert execution['exit_code'] == 0 and execution['original_unchanged'] is True
            assert execution['input_sha256'] == record['input_sha256']
            assert execution['four_class_probabilities'] == normalized['native_class_probabilities']
        scores[record['directory']] = normalized['native_class_probabilities']
        if not record['has_review']:
            continue
        ledger, validated, index = (read(root / name) for name in ('ledger.json', 'validated-final.json', 'index.json'))
        assert ledger['text_sha256'] == validated['text_sha256'] == index['text_sha256'] == sha(source)
        text, cursor = source.read_bytes().decode('utf-8'), 0
        paragraphs = index['paragraphs']
        assert len(ledger['paragraph_reviews']) == len(validated['paragraph_reviews']) == len(paragraphs) == 4
        for number, (paragraph, original, checked) in enumerate(zip(paragraphs, ledger['paragraph_reviews'], validated['paragraph_reviews']), 1):
            assert paragraph['id'] == original['paragraph_id'] == checked['paragraph_id'] == f'P{number}'
            start, end = paragraph['start'], paragraph['end']
            assert cursor <= start < end <= len(text) and not text[cursor:start].strip()
            assert text[start:end] == paragraph['text'] and original['status'] == 'reviewed'
            assert all(checked.get(k) == v for k, v in original.items())
            assert all(checked.get(k) == v for k, v in paragraph.items())
            cursor = end
        assert not text[cursor:].strip()
        assert validated['coverage']['paragraphs_total'] == validated['coverage']['paragraphs_reviewed'] == 4
        assert len(ledger['findings']) == len(validated['findings'])
        assert len({f['id'] for f in ledger['findings']}) == len(ledger['findings'])
        for original, checked in zip(ledger['findings'], validated['findings']):
            assert all(checked.get(k) == v for k, v in original.items() if k != 'spans')
            assert len(original['spans']) == len(checked['spans'])
            for span, checked_span in zip(original['spans'], checked['spans']):
                assert all(checked_span.get(k) == v for k, v in span.items())
                assert 0 <= span['start'] < span['end'] <= len(text)
                assert text[span['start']:span['end']] == span['quote']
        assert validated['measured_output']['class_probabilities'] == normalized['native_class_probabilities']
    assert scores['en-revision-1'] == scores['adapter-en-final']
    prior = read(REPO / 'benchmarks/local-feedback/development/en-baseline-retry/feedback.json')
    assert prior['status'] == 'error' and prior['human_percent'] is None
    print('PASS: 3 English successful measurements on 2 texts, 2 complete reviews, adapter compatibility and unchanged earlier failure.')


if __name__ == '__main__':
    verify()
