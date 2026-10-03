"""Check exact iterative feedback records and retained release evidence, without inference."""
from pathlib import Path
import hashlib
import importlib.util
import json
import sys
from datetime import datetime

if not __debug__:
    raise RuntimeError('Run evidence verification without Python -O.')
REPO = Path(__file__).resolve().parents[1]
ROOT = REPO/'benchmarks/feedback-cycle'
CASES = ('support-email', 'reading-reflection')

def read(path): return json.loads(path.read_text('utf-8'))
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def manifest(path):
    return {p.relative_to(path).as_posix():sha(p) for p in sorted(path.rglob('*'))
            if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc'}

def verify():
    frozen = manifest(ROOT)
    frozen.pop('frozen-files.json')
    assert frozen == read(ROOT/'frozen-files.json'), 'Feedback evidence changed'
    assert manifest(ROOT/'retained-skill') == read(ROOT/'retained-skill-hashes.json')
    assert manifest(ROOT/'retained-skill') == read(REPO/'benchmarks/english-focus/release-skill-hashes.json')
    active = REPO/'skills/bilingual-humanizer'
    assert manifest(active) == read(ROOT/'release-skill-hashes.json')
    assert 'version: "1.10.0"' in (active/'SKILL.md').read_text('utf-8')
    assert sha(active/'references/korean.md') == sha(ROOT/'retained-skill/references/korean.md')
    assert sha(active/'scripts/local_feedback.py') == sha(ROOT/'retained-skill/scripts/local_feedback.py')
    sys.path.insert(0, str(active/'scripts'))
    import feedback_cycle
    results = read(ROOT/'results.json')
    assert results['release_version'] == '1.10.0'
    assert results['external_detector_calls'] == results['paid_actions'] == 0
    assert results['authorship_verified'] is results['commercial_transfer_measured'] is False
    assert set(results['cases']) == set(CASES)
    all_scores, new_scores = [], 0
    timing = read(ROOT/'scoring-readiness-notes.json')['exceptions']
    assert len(timing) == 1 and timing[0]['case'] == 'support-email' and timing[0]['round'] == 2
    timing_exceptions_seen = []
    for case in CASES:
        directory = ROOT/'cases'/case
        session = read(directory/'session.json')
        state = feedback_cycle.validate(directory/'session.json')
        assert state == read(directory/'final-status.json') == results['cases'][case]
        if case == 'support-email':
            assert state['status'] == 'complete' and not state['current_open_findings']
        else:
            assert state['status'] == 'budget' and state['revisions_used'] == 3
            assert state['rounds'][-1]['fidelity_eligible'] is False
            assert state['current_open_findings'] and state['numeric_unavailable_rounds'] == ['r3']
            assert state['selected_candidate']['id'] == 'r2'
        assert state['selected_candidate']['feedback_closed'] and state['selected_candidate']['fidelity_eligible']
        assert state['recorded_text_revisions'] >= 1, 'Only the initial draft was reviewed'
        assert session['revision_limit'] == 3
        assert session['prior_revisions_used'] == (1 if case == 'reading-reflection' else 0)
        assert (directory/'source.txt').read_bytes() == (REPO/'benchmarks/english-focus/cases'/case/'source.txt').read_bytes()
        assert (directory/'round-1.txt').read_bytes() == (REPO/'benchmarks/english-focus/cases'/case/'experimental.txt').read_bytes()
        for old_dir, new_dir in [('source-score','source-score'),('experimental-score','round-1-score')]:
            for name in ('model-result.json','feedback.json','execution.json','input.txt'):
                assert (directory/new_dir/name).read_bytes() == (REPO/'benchmarks/english-focus/cases'/case/old_dir/name).read_bytes()
        for round_no, item in enumerate(session['rounds']):
            if round_no < 2:
                continue
            candidate = directory/item['candidate']['path']
            prescore = read(directory/f'round-{round_no}-prescore.json')
            assert prescore['candidate_sha256'] == sha(candidate)
            assert prescore['source_sha256'] == sha(directory/'source.txt')
            if item['native'] is None:
                assert case == 'reading-reflection' and round_no == 3
                assert prescore['eligible_for_scoring'] is False and prescore['necessary_repairs']
                assert read(directory/item['feedback']['path'])['inference_executed'] is False
                assert not (directory/'round-3-score/model-result.json').exists()
                continue
            native = read(directory/item['native']['path'])
            assert prescore['eligible_for_scoring'] is True and not prescore['necessary_repairs']
            if datetime.fromisoformat(prescore['reviewed_at_utc']) > datetime.fromisoformat(native['measured_at_utc']):
                note = next(n for n in timing if n['case'] == case and n['round'] == round_no)
                assert note['candidate_sha256'] == sha(candidate)
                assert note['prescore_recorded_at_utc'] == prescore['reviewed_at_utc']
                assert note['native_measured_at_utc'] == native['measured_at_utc']
                assert note['basis'] and note['limitation'] and note['readiness_message_excerpt']
                timing_exceptions_seen.append((case,round_no))
            new_scores += 1
        all_scores.append(state['selected_candidate']['human_percent'])
    assert results['new_local_measurements'] == new_scores
    assert results['new_candidates_rejected_before_scoring'] == 1
    assert timing_exceptions_seen == [('support-email',2)]
    assert results['all_selected_human_ge_50_targets_met'] == all(v is not None and v >= 50 for v in all_scores)
    historical = read(ROOT/'historical-benchmarks.json')
    exceptions = {'verify_evidence.py', 'verify_english_focus.py'}
    for name, expected in historical.items():
        if name not in exceptions:
            assert sha(REPO/'benchmarks'/name) == expected, 'Historical artifact changed: ' + name
    print(f'PASS: two actual feedback continuations; {new_scores} new exact local scores; prior evidence retained.')

if __name__ == '__main__':
    verify()
