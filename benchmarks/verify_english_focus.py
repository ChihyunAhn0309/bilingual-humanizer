"""Verify native measurements, blinded inputs and exact English release evidence."""
from pathlib import Path
import hashlib
import importlib.util
import json
from datetime import datetime

if not __debug__:
    raise RuntimeError('Run evidence verification without Python -O; validation assertions are required.')

REPO = Path(__file__).resolve().parents[1]
ROOT = REPO/'benchmarks/english-focus'

def read(path):
    return json.loads(path.read_text('utf-8'))

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def files(root):
    return {p.relative_to(root).as_posix():sha(p) for p in sorted(root.rglob('*'))
            if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc'}

def safe(relative):
    path = (ROOT/relative).resolve()
    assert path.is_relative_to(ROOT.resolve()), relative
    return path

def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result

def verify():
    frozen = files(ROOT)
    frozen.pop('frozen-files.json')
    assert frozen == read(ROOT/'frozen-files.json'), 'Experiment evidence changed'
    assert files(ROOT/'retained-skill') == read(ROOT/'baseline-skill-hashes.json')
    assert files(ROOT/'retained-skill') == read(REPO/'benchmarks/composition-feedback/release-skill-hashes.json')
    active = REPO/'benchmarks/feedback-cycle/retained-skill'
    assert files(active) == read(ROOT/'release-skill-hashes.json')
    assert files(active) == read(ROOT/'experimental-skill-hashes.json')
    assert 'version: "1.9.0"' in (active/'SKILL.md').read_text('utf-8')
    assert sha(active/'references/korean.md') == sha(ROOT/'retained-skill/references/korean.md')

    assignment = read(ROOT/'assignment.json')
    blind = read(ROOT/'blind-review.json')
    for field in ('assignment_read','method_labels_read','scores_read','writer_reviews_read','other_experiment_artifacts_read','candidate_method_guesses_made'):
        assert blind['blinding'][field] is False
    gate = read(ROOT/'scoring-authorized.json')
    assert gate['review_sha256'] == sha(ROOT/'blind-review.json')
    assert len(gate['candidates']) == 6
    assert {r['path'] for r in gate['candidates']} == {f'cases/{c}/{a}.txt' for c in ('support-email','reading-reflection','technical-update') for a in ('baseline','experimental')}
    for candidate in gate['candidates']:
        assert candidate['eligible'] is True and sha(safe(candidate['path'])) == candidate['sha256']
    assert {r['case'] for r in assignment['cases']} == {'support-email','reading-reflection','technical-update'}
    assert len(assignment['cases']) == len(blind['cases']) == 3
    for item in assignment['cases']:
        case = item['case']
        review = next(r for r in blind['cases'] if r['case'] == case)
        assert sha(safe(f'cases/{case}/source.txt')) == item['source_sha256'] == review['source_sha256']
        assert set(item['labels']) == set(review['candidates']) == {'A','B'}
        assert {r['arm'] for r in item['labels'].values()} == {'baseline','experimental'}
        for label, mapping in item['labels'].items():
            candidate = safe(f'cases/{case}/{mapping["arm"]}.txt')
            judged = review['candidates'][label]
            assert sha(candidate) == mapping['sha256'] == judged['sha256']
            assert candidate.read_bytes() == safe(f'blind-pairs/{case}/{label}.txt').read_bytes()
            assert judged['fidelity_pass'] is judged['eligible_for_scoring'] is True
            assert not judged['required_repairs']
        assert safe(f'blind-pairs/{case}/source.txt').read_bytes() == safe(f'cases/{case}/source.txt').read_bytes()
        assert review['coverage']
        for constraint in review['coverage']:
            original = safe(f'cases/{case}/source.txt').read_text('utf-8')
            assert constraint['source_quotes'] and all(q in original for q in constraint['source_quotes'])
            assert set(constraint['candidate_quotes']) == {'A','B'}
            for label, quotes in constraint['candidate_quotes'].items():
                candidate_text = safe(f'blind-pairs/{case}/{label}.txt').read_text('utf-8')
                assert quotes and all(q in candidate_text for q in quotes)

    adapter = module('english_focus_adapter', active/'scripts/local_feedback.py')
    checker = module('english_focus_review_checker', REPO/'benchmarks/verify_composition_feedback.py')
    checker.ROOT = ROOT
    results = read(ROOT/'results.json')
    assert results['release_version'] == '1.9.0'
    assert results['external_detector_calls'] == results['paid_actions'] == 0
    assert type(results['all_selected_human_ge_50_targets_met']) is bool
    assert results['authorship_verified'] is results['commercial_transfer_measured'] is False
    expected = {f'cases/{case}/{arm}-score' for case in ('support-email','reading-reflection','technical-update')
                for arm in ('baseline','experimental')}
    expected |= {'cases/support-email/source-score','cases/reading-reflection/source-score',
                 'cases/technical-update/source-score-recovered'}
    assert {r['directory'] for r in results['measurements']} == expected
    assert len(results['measurements']) == 9
    measured = {}
    for item in results['measurements']:
        directory = safe(item['directory'])
        case = directory.parent.name
        arm = directory.name.split('-score',1)[0]
        assert item['case'] == case and item['arm'] == arm and item['language'] == 'en'
        assert item['candidate'] == f'cases/{case}/{arm}.txt'
        native, feedback, execution = (read(directory/name) for name in ('model-result.json','feedback.json','execution.json'))
        raw = (directory/'input.txt').read_bytes()
        normalized = adapter.normalize(native,raw,'en')
        assert execution['status'] == feedback['status'] == 'completed'
        assert execution['input_sha256'] == normalized['input_sha256'] == item['input_sha256']
        started = datetime.fromisoformat(execution['started_at_utc'].replace('Z','+00:00'))
        measured_at = datetime.fromisoformat(native['measured_at_utc'].replace('Z','+00:00'))
        assert measured_at >= started
        if arm != 'source':
            assert started >= datetime.fromisoformat(gate['authorized_at_utc'].replace('Z','+00:00'))
        assert [c['stage'] for c in execution['calls']] == ['index','score']
        assert all(type(c['returncode']) is int and c['returncode'] == 0 for c in execution['calls'])
        assert [c['script_sha256'] for c in execution['calls']] == [
            'e39f5672ad47ec0bb95bd4d7ee83f9833b3d16ef795cfb6f2d27d5946f5df705',
            'd2abfb56ec052f6e96779cc1f9d5b86a4d28e91c5dd59e23f7cf092482876bd0']
        assert all(feedback.get(k) == v for k,v in normalized.items())
        assert feedback['raw_result_sha256'] == sha(directory/'model-result.json')
        for key in ('human_percent','native_class_probabilities','scope','measured_at_utc'):
            assert item[key] == normalized[key]
        assert item['scope'] == 'whole_document' and native['weight_loading_backend'] == 'pread'
        candidate = safe(item['candidate'])
        assert raw == candidate.read_bytes()
        measured[sha(candidate)] = normalized | {'_native_receipt':native}
    assert len(results['reviews']) == 9
    assert {r['input'] for r in results['reviews']} == {m['candidate'] for m in results['measurements']}
    assert {sha(safe(r['input'])) for r in results['reviews']} == set(measured)
    for item in results['reviews']:
        measurement = next(m for m in results['measurements'] if m['candidate'] == item['input'])
        review_dir = measurement['directory'].replace('-score','-review')
        assert {k:item[k] for k in ('ledger','validated','index')} == {
            'ledger':review_dir+'/ledger.json','validated':review_dir+'/validated.json','index':review_dir+'/index.json'}
        checker.verify_review(item,measured)

    for directory in ('cases/technical-update/source-score','cases/technical-update/source-score-retry'):
        feedback, execution = (read(safe(directory+'/'+n)) for n in ('feedback.json','execution.json'))
        assert feedback['status'] == execution['status'] == 'error'
        assert feedback['human_percent'] is feedback['native_class_probabilities'] is None
        assert feedback['input_sha256'] == execution['input_sha256'] == sha(safe('cases/technical-update/source.txt'))
        assert not safe(directory+'/model-result.json').exists()

    assert len(results['selections']) == 3
    assert {r['case'] for r in results['selections']} == {'support-email','reading-reflection','technical-update'}
    for item in results['selections']:
        candidates = [r for r in results['measurements'] if r['case'] == item['case']]
        selected = next(r for r in candidates if r['candidate'] == item['native_checkpoint'])
        assert item['human_percent'] == selected['human_percent'] == max(r['human_percent'] for r in candidates)
        assert item['sha256'] == sha(safe(item['native_checkpoint']))
        review = next(r for r in blind['cases'] if r['case'] == item['case'])
        assert item['blind_editorial_winner'] == review['editorial_winner']
        winner = review['editorial_winner']
        assert winner in ('A','B','source','tie')
        mapping = next(r for r in assignment['cases'] if r['case'] == item['case'])
        editorial = mapping['labels'][winner]['arm'] if winner in ('A','B') else ('baseline' if winner=='tie' else 'source')
        assert item['editorial_choice'] == f'cases/{item["case"]}/{editorial}.txt'
    assert results['all_selected_human_ge_50_targets_met'] == all(r['human_percent'] >= 50 for r in results['selections'])
    print('PASS: English focus: 9 exact native measurements, 9 complete reviews, blinded pairs, retained v1.8 and v1.9 integrity.')

if __name__ == '__main__':
    verify()
