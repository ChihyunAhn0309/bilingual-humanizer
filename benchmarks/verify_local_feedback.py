"""Check frozen local measurements and review anchors, not authorship or prose quality."""
from pathlib import Path
from datetime import datetime
import hashlib
import json
import math

ROOT = Path(__file__).resolve().parent / 'local-feedback'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def safe(relative):
    path = (ROOT / relative).resolve()
    assert path.is_relative_to(ROOT.resolve()), relative
    return path


def read(relative):
    return json.loads(safe(relative).read_text('utf-8'))


def verify():
    data = read('results.json')
    frozen = read('frozen-files.json')
    for relative, expected in frozen.items():
        assert digest(safe(relative)) == expected, relative
    seen = set()
    for record in data['measurements']:
        assert record['id'] not in seen
        seen.add(record['id'])
        source = safe(record['input'])
        assert digest(source) == record['input_sha256']
        native = read(record['native_result'])
        assert native['text_sha256'] == record['input_sha256']
        assert native['mode'] == 'offline_korean_calibrated_classifier'
        assert native['model_sha256'] == data['korean_model_sha256']
        assert native['external_detector_calls'] == 0 and native['authorship_verified'] is False
        assert native['all_input_scored'] is True
        assert native['genre_requested'] == record['genre'] == 'unknown'
        datetime.fromisoformat(native['measured_at_utc'])
        probs = native['class_probabilities']
        assert set(probs) == {'human', 'ai'}
        assert all(type(p) in (int, float) and math.isfinite(p) and 0 <= p <= 1 for p in probs.values())
        assert math.isclose(sum(probs.values()), 1)
        assert record['human_percent'] == probs['human'] * 100
        if record.get('feedback'):
            feedback = read(record['feedback'])
            assert feedback['status'] == 'completed' and feedback['input_sha256'] == record['input_sha256']
            assert feedback['human_percent'] == record['human_percent']
            assert feedback['native_class_probabilities'] == probs
            assert feedback['raw_result_sha256'] == digest(safe(record['native_result']))
    for failure in data['failures']:
        result = read(failure['feedback'])
        execution = read(failure['execution'])
        assert digest(safe(failure['input'])) == result['input_sha256'] == execution['input_sha256']
        assert result['status'] == execution['status'] == 'error'
        assert result['human_percent'] is None and result['native_class_probabilities'] is None
        assert any(call['returncode'] != 0 for call in execution['calls'])
    for review in data['reviews']:
        text = safe(review['input']).read_bytes().decode('utf-8')
        ledger = read(review['ledger'])
        validated = read(review['validated'])
        index = read((Path(review['ledger']).parent / 'index.json').as_posix())
        expected = hashlib.sha256(text.encode('utf-8')).hexdigest()
        assert ledger['text_sha256'] == validated['text_sha256'] == index['text_sha256'] == expected
        paragraph_ids = []
        cursor = 0
        for number, paragraph in enumerate(index['paragraphs'], 1):
            start, end = paragraph['start'], paragraph['end']
            assert paragraph['id'] == f'P{number}'
            assert cursor <= start < end <= len(text) and not text[cursor:start].strip()
            assert text[start:end] == paragraph['text'] and paragraph['text'].strip()
            assert paragraph['line'] == text[:start].count('\n') + 1
            paragraph_ids.append(paragraph['id'])
            cursor = end
        assert paragraph_ids and not text[cursor:].strip(), 'Index omits source text'
        ledger_reviews = {p['paragraph_id']: p for p in ledger['paragraph_reviews']}
        checked_reviews = {p['paragraph_id']: p for p in validated['paragraph_reviews']}
        assert len(ledger_reviews) == len(ledger['paragraph_reviews']) == len(paragraph_ids)
        assert len(checked_reviews) == len(validated['paragraph_reviews']) == len(paragraph_ids)
        assert set(ledger_reviews) == set(checked_reviews) == set(paragraph_ids)
        finding_ids = {f['id'] for f in ledger['findings']}
        checked_findings = {f['id']: f for f in validated['findings']}
        assert len(finding_ids) == len(ledger['findings']) == len(checked_findings) == len(validated['findings'])
        assert finding_ids == set(checked_findings)
        for paragraph in index['paragraphs']:
            original_review = ledger_reviews[paragraph['id']]
            checked_review = checked_reviews[paragraph['id']]
            assert original_review['status'] == 'reviewed' and original_review['assessment'].strip()
            assert set(original_review['finding_ids']) <= finding_ids
            assert all(checked_review.get(k) == v for k, v in original_review.items())
            assert all(checked_review.get(k) == v for k, v in paragraph.items())
        coverage = validated['coverage']
        assert coverage['paragraphs_reviewed'] == coverage['paragraphs_total'] == len(paragraph_ids)
        assert coverage['paragraphs_excluded'] == 0 and coverage['review_fraction'] == 1.0
        for finding in ledger['findings']:
            checked = checked_findings[finding['id']]
            assert all(checked.get(k) == v for k, v in finding.items() if k != 'spans')
            assert len(checked['spans']) == len(finding['spans'])
            assert finding['human_alternative'] and finding['interpretation']
            for span, checked_span in zip(finding['spans'], checked['spans']):
                assert all(checked_span.get(k) == v for k, v in span.items())
                assert 0 <= span['start'] < span['end'] <= len(text)
                assert text[span['start']:span['end']] == span['quote']
        measured = validated.get('measured_output')
        matches = [r for r in data['measurements'] if r['input_sha256'] == expected]
        if measured is None:
            assert not matches, 'A measured Korean review dropped its numeric context'
            assert validated['authorship_probabilities'] is None
        else:
            assert matches and measured['model_sha256'] == data['korean_model_sha256']
            assert any(measured['class_probabilities'] == read(r['native_result'])['class_probabilities']
                       and measured['measured_at_utc'] == r['measured_at_utc'] for r in matches)
    for checkpoint in data['checkpoints']:
        assert digest(safe(checkpoint['input'])) == checkpoint['input_sha256']
        if checkpoint['measurement_id'] is None:
            assert checkpoint['human_percent'] is None
        else:
            rec = next(r for r in data['measurements'] if r['id'] == checkpoint['measurement_id'])
            assert checkpoint['input_sha256'] == rec['input_sha256']
            assert checkpoint['human_percent'] == rec['human_percent']
    skill = ROOT.parents[1] / 'skills/bilingual-humanizer'
    release = read('release-skill-hashes.json')
    actual = {p.relative_to(skill).as_posix(): digest(p) for p in skill.rglob('*')
              if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc'}
    assert actual == release
    assert 'version: "1.7.0"' in (skill / 'SKILL.md').read_text('utf-8')
    assert data['external_detector_calls'] == 0 and data['paid_actions'] == 0
    assert data['authorship_verified'] is False and data['commercial_transfer_measured'] is False
    print(f'PASS: {len(seen)} local Korean measurements, {len(data["reviews"])} complete anchored reviews, English failure and v1.7.0 integrity.')


if __name__ == '__main__':
    verify()
