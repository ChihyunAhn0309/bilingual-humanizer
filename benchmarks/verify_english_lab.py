"""Verify archived English lab evidence without model inference or external access."""
from pathlib import Path
from datetime import datetime
import hashlib, json, sys
if not __debug__:
    raise RuntimeError('Run evidence verification without Python -O.')
REPO=Path(__file__).resolve().parents[1]
ROOT=REPO/'benchmarks/english-lab'
read=lambda p:json.loads(p.read_text('utf-8'))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def manifest(p):
    return {f.relative_to(p).as_posix():sha(f) for f in sorted(p.rglob('*')) if f.is_file() and '__pycache__' not in f.parts and f.suffix!='.pyc'}
def bound(ref):
    p=ROOT/ref['path']
    assert sha(p)==ref['sha256'], 'Broken artifact reference: '+str(p)
    return p
def verify():
    actual=manifest(ROOT)
    actual.pop('frozen-files.json')
    assert actual==read(ROOT/'frozen-files.json'),'English lab evidence changed'
    baseline=read(ROOT/'baseline-skill-hashes.json')
    assert manifest(ROOT/'baseline-skill')==baseline==manifest(REPO/'skills/bilingual-humanizer')
    assert baseline==read(REPO/'benchmarks/feedback-cycle/release-skill-hashes.json')
    prototype=read(ROOT/'prototype-skill-hashes.json')
    assert manifest(ROOT/'skill')==prototype
    changed={k for k in baseline if baseline[k]!=prototype[k]}
    assert changed=={'SKILL.md','references/english-composition.md','references/english-reference-review.md'}
    assert 'version: "1.10.0"' in (REPO/'skills/bilingual-humanizer/SKILL.md').read_text('utf-8')
    assert 'version: "1.11.0-dev"' in (ROOT/'skill/SKILL.md').read_text('utf-8')
    results=read(ROOT/'results.json')
    assert results['release_decision']=='retain_production_and_archive_experiment'
    assert results['production_version']=='1.10.0'
    assert results['commercial_detector_calls']==results['paid_actions']==results['failed_model_submissions']==0
    assert results['model_or_calibration_changes'] is results['authorship_verified'] is results['commercial_transfer_measured'] is False
    assert results['target_human_ge_50_met'] is False
    native_paths=[p for d in ('development','transfer-scores','continuation-scores') for p in (ROOT/d).rglob('model-result.json')]
    assert len(native_paths)==results['new_local_document_submissions']==17
    for p in native_paths:
        d=read(p);f=read(p.with_name('feedback.json'))
        assert d['text_sha256']==sha(p.with_name('input.txt'))==f['input_sha256']
        assert d['weight_sha256']=='4a1561fadf44ec72934edd6158ff8c76e9388ade1384dbeeea6eb15f93251087'
        assert d['revision']=='f1795c86806e6838d4afa33d0b1427f8430c9615'
        assert d['model']=='wasitaigeneratedcom/ai-text-detector-small'
        assert d['all_input_tokens_scored'] and d['authorship_verified'] is False
        assert f['status']=='completed' and f['scope']=='whole_document'
        assert f['human_percent']==100*d['document_class_probabilities']['human']
        assert d['external_detector_calls']==0
    comparison=read(ROOT/'transfer-comparison.json')
    blind=read(bound(comparison['blind_review']))
    bound(comparison['method_freeze']);bound(comparison['source_registry']);bound(comparison['identity_mapping'])
    assert len(comparison['cases'])==3
    for c in comparison['cases']:
        for arm in ('source','baseline','prototype'):
            s=c[arm]
            candidate=bound(s['candidate']); native=read(bound(s['native']))
            bound(s['feedback']);bound(s['execution'])
            assert sha(candidate)==native['text_sha256']
            assert s['classes']==native['document_class_probabilities']
            assert s['human_percent']==100*s['classes']['human']
            if arm!='source':
                assert datetime.fromisoformat(blind['reviewed_at_utc'])<datetime.fromisoformat(native['measured_at_utc'])
                verdict=next(x for x in blind['cases'] if x['case_id']==c['case'])['candidates'][s['alias']]
                assert verdict['sha256']==sha(candidate) and verdict['fidelity_pass'] and verdict['reader_eligible'] and not verdict['necessary_repairs']
        assert c['prototype_minus_baseline_pp']==c['prototype']['human_percent']-c['baseline']['human_percent']
        assert c['prototype_minus_source_pp']==c['prototype']['human_percent']-c['source']['human_percent']
    assert comparison['prototype_human_wins']==sum(c['prototype_minus_baseline_pp']>0 for c in comparison['cases'])==2
    sys.path.insert(0,str(ROOT/'skill/scripts'))
    import feedback_cycle
    for p in sorted(ROOT.glob('*-initial-session.json')):
        state=feedback_cycle.validate(p)
        assert state==read(ROOT/'cycle-status'/p.name.replace('-initial-session.json','-initial.json'))
        assert state['status']=='complete' and state['revisions_used']==0
    for cid in ('T01','T02'):
        state=feedback_cycle.validate(ROOT/f'{cid}-prototype-final-session.json')
        assert state==read(ROOT/'cycle-status'/f'{cid}-prototype-final.json')
        assert state['status']=='complete' and state['revisions_used']==1
        prescore=read(ROOT/'prototype-output'/cid/'draft-2-prescore.json')
        native=read(ROOT/'continuation-scores'/cid/'model-result.json')
        assert prescore['candidate_sha256']==native['text_sha256'] and prescore['eligible_for_scoring'] and not prescore['necessary_repairs']
        assert datetime.fromisoformat(prescore['reviewed_at_utc'])<datetime.fromisoformat(native['measured_at_utc'])
        assert state['selected_candidate']['id']==('draft-1' if cid=='T01' else 'source')
    dev=read(ROOT/'development/RESULTS.json')
    assert dev['actual_detector_calls']==6 and dev['protocol_deviation']
    for cid in ('policy-note','exhibition-review'):
        state=feedback_cycle.validate(ROOT/'development'/cid/'session.json')
        assert state==read(ROOT/'development'/cid/'final-status.json')
        assert state['status']=='complete'
    assert (ROOT/'baseline-output/feedback-closure.json').exists()
    assert (ROOT/'prototype-output/final-feedback-closure.json').exists()
    for name,expected in read(ROOT/'historical-benchmarks.json').items():
        if name!='verify_evidence.py':
            assert sha(REPO/'benchmarks'/name)==expected,'Historical evidence changed: '+name
    print('PASS: English lab; 17 exact local submissions, frozen comparison, real feedback cycles, prior production/evidence retained.')
if __name__=='__main__':
    verify()
