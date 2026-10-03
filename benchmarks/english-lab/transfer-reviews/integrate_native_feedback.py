"""Attach supplied source model records without running inference or changing reviews."""
import hashlib
import json
import math
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCES = ROOT.parent / 'transfer'
SCORES = ROOT.parent / 'transfer-scores'
registry = json.loads((SOURCES / 'registry.json').read_text(encoding='utf-8'))
frozen = json.loads((ROOT / 'qualitative-freeze.json').read_text(encoding='utf-8'))
interpretations = {
 'T01':'The largest deletion sensitivity is P1 (+82.86542173009366 percentage points): removing the mechanism and example changes the input substantially. This does not locate a defective phrase, explain the model\'s internals, or justify removing useful exposition. P2 and P3 deletions change the score by +0.3357914509251714 and +2.0857394440099597 points respectively. All three paragraph-level retain decisions remain unchanged.',
 'T02':'Deleting P2 or P3 changes AI-involvement by +19.75725651718676 and +17.144285747781396 percentage points. Those paragraphs carry the workflow and fallback; deleting them would remove required instructions. P1 and P4 deltas are +1.660560118034482 and +0.7406630087643862 points. Model sensitivity does not identify an editorial defect or recommend weakening any instruction. All four retain decisions remain unchanged.',
 'T03':'The complete input has a high AI-involvement class score, yet each individual deletion changes it by less than one percentage point: P1 +0.9503668014076538, P2 +0.09005309111671522, P3 +0.15645559906261042. These measurements do not single out a problematic paragraph, and a small delta does not prove neutrality or quality. All three retain decisions, including the uncertainty and unresolved ending, remain unchanged.'
}

for case in registry['cases']:
    cid=case['id']
    for suffix,digest in frozen['checksums'][cid].items():
        assert hashlib.sha256((ROOT/f'{cid}.{suffix}').read_bytes()).hexdigest()==digest
    source=(SOURCES/case['source_file']).read_bytes()
    assert hashlib.sha256(source).hexdigest()==case['source_sha256']
    text=source.decode('utf-8')
    native_path=SCORES/cid/'source'/'model-result.json'
    native_raw=native_path.read_bytes()
    native=json.loads(native_raw)
    assert native['mode']=='offline_local_model'
    assert native['text_sha256']==case['source_sha256']
    assert native['model']=='wasitaigeneratedcom/ai-text-detector-small'
    assert native['revision']=='f1795c86806e6838d4afa33d0b1427f8430c9615'
    assert native['weight_sha256']=='4a1561fadf44ec72934edd6158ff8c76e9388ade1384dbeeea6eb15f93251087'
    assert native['all_input_tokens_scored'] is True
    assert native['execution_guard']['worker_exit_code']==0
    assert native['execution_guard']['serialized_cli'] is True
    assert native['external_detector_calls']==0
    assert len(native['windows'])==1
    window=native['windows'][0]
    assert window['token_start']==0 and window['token_end']==native['token_count']
    assert text[window['start']:window['end']]==window['quote']
    assert not text[:window['start']].strip() and not text[window['end']:].strip()
    probs=native['document_class_probabilities']
    assert set(probs)=={'human','ai','ai_edited','humanized'}
    assert all(math.isfinite(v) and 0<=v<=1 for v in probs.values())
    assert abs(sum(probs.values())-1)<1e-5
    assert probs==window['class_probabilities']
    baseline=window['ai_involvement_class_score']
    assert abs(baseline-(1-probs['human']))<1e-7
    assert abs(baseline-sum(probs[k] for k in ['ai','ai_edited','humanized']))<1e-5
    qualitative=json.loads((ROOT/f'{cid}.qualitative-ledger.json').read_text(encoding='utf-8'))
    full=deepcopy(qualitative)
    end='AI/Human probabilities are unavailable here because inference was deliberately not run and no quantitative result was supplied.'
    assert full['summary'].endswith(end)
    probability_sentence=(f"Supplied unvalidated local model class outputs are Human {100*probs['human']:.8f}%, AI {100*probs['ai']:.8f}%, AI-edited {100*probs['ai_edited']:.8f}%, and Humanized {100*probs['humanized']:.8f}%. The recorded AI-involvement class score is {100*baseline:.8f}%. These are experimental model responses, not personal-authorship probabilities, word shares, or writing-quality ratings. The installed skill reports high-confidence false positives in its 36-document English pilot. The pre-score qualitative decisions remain unchanged.")
    full['summary']=full['summary'][:-len(end)]+probability_sentence+' '+interpretations[cid]
    full['document_analysis']['citations_provenance'] += ' A separately supplied native model result is bound to this exact hash and a single window covering all input tokens. Its four-class output and deletion sensitivity are separate evidence types; they do not authenticate authorship or explain internal model causation.'
    index=json.loads((ROOT/f'{cid}.index.json').read_text(encoding='utf-8'))
    para_map={p['id']:p for p in index['paragraphs']}
    occ=native['occlusion']
    assert occ['performed'] is True and occ['unmeasured_due_to_limit']==0
    assert len(occ['paragraphs'])==len(para_map)==occ['total_paragraphs']
    for number,item in enumerate(occ['paragraphs'],1):
        p=para_map[item['paragraph_id']]
        assert item['status']=='measured'
        assert all(item[k]==p[k] for k in ['start','end'])
        assert item['quote']==p['text']==text[item['start']:item['end']]
        b=item['baseline_ai_involvement']; a=item['after_removal_ai_involvement']; d=item['delta_percentage_points']
        assert all(math.isfinite(x) for x in [b,a,d]) and 0<=a<=1
        assert abs(b-baseline)<1e-7 and abs(d-(b-a)*100)<1e-7
        oid=f'O{number}'
        full['findings'].append({
          'id':oid,'basis':'local_occlusion','direction':'ai_like' if d>0 else 'human_compatible' if d<0 else 'neutral','strength':'weak',
          'spans':[{'start':p['start'],'end':p['end'],'quote':p['text'],'paragraph_id':p['id'],'line':p['line']}],
          'observation':f"For {p['id']}, the supplied model measured baseline AI-involvement {b!r}, after-removal score {a!r}, and baseline-minus-removal delta {d!r} percentage points.",
          'interpretation':'This is measured sensitivity to deleting the whole paragraph. A positive delta means the shortened input scored lower. It is not that paragraph\'s AI probability, a defective-phrase location, a causal feature attribution, or an editorial repair instruction. Qualitative strength remains weak as authorship evidence regardless of numerical magnitude.',
          'human_alternative':'Length, remaining context, disrupted argument or narrative, and ordinary genre features can change this model\'s response to human or AI prose. This particular source is already known AI-generated from the generation record, not from the deletion result.',
          'discriminating_evidence':'Controlled equal-length edits and independent validation would be needed to distinguish wording effects from context/length effects. None is claimed or authorized here. Retain the pre-score editorial decision unless independent source-fidelity or reader-quality evidence warrants a change.',
          'source_record':{'file':str(native_path.resolve()),'file_sha256':hashlib.sha256(native_raw).hexdigest(),'field':f'occlusion.paragraphs[{number-1}]','conditions':'Single-window English input; one full paragraph removed and remaining text rescored by the pinned local checkpoint; supplied result, no inference performed by this reviewer.'}
        })
        next(pv for pv in full['paragraph_reviews'] if pv['paragraph_id']==p['id'])['finding_ids'].append(oid)
    full['measurement_record']={
      'model_result_file':str(native_path.resolve()),'model_result_sha256':hashlib.sha256(native_raw).hexdigest(),
      'model':native['model'],'revision':native['revision'],'weight_sha256':native['weight_sha256'],
      'measured_at_utc':native['measured_at_utc'],'source_sha256':native['text_sha256'],
      'language':'English, manually verified','window_count':1,'token_count':native['token_count'],'all_input_tokens_scored':True,
      'class_probabilities':probs,'ai_involvement_class_score':baseline,
      'aggregation_semantics':'AI-involvement is AI + AI-edited + Humanized versus Human-only. The native score is stored as 1-Human; the class sum agrees within float rounding. Neither value is a percentage of words or a calibrated probability of personal authorship.',
      'independently_calibrated_here':False,'authorship_verified_by_model':False,
      'observed_limit':'Installed bilingual-ai-detector free-local-model.md reports high-confidence false positives on human texts in a 36-document English pilot. These three synthetic sources are not a calibration or general performance benchmark.',
      'occlusion':native['occlusion'],'editorial_interpretation':interpretations[cid]
    }
    full['review_metadata']['phase']='Supplied native results integrated after qualitative freeze; no candidate output, candidate score, or method identity seen.'
    full['review_metadata']['integrated_at_utc']=datetime.now(timezone.utc).isoformat()
    full['review_metadata']['qualitative_scores_blind_snapshot']=f'{cid}.qualitative-ledger.json'
    full['review_metadata']['detector_scores_read']=True
    full['review_metadata']['numeric_status']='Supplied one-window native result checked and attached; unvalidated class outputs only.'
    full['review_metadata']['measured_authorship_probabilities']=None
    full['review_metadata']['measurement_file']=f'{cid}.validated-full.json'
    for finding in full['findings']:
        if isinstance(finding.get('source_record'), dict):
            finding['source_record'] = json.dumps(finding['source_record'], ensure_ascii=False)
    out=ROOT/f'{cid}.full-ledger.json'
    assert not out.exists(), out
    out.write_text(json.dumps(full,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(cid, 'native result checked;', len(full['findings']), 'total anchored findings; retain decisions unchanged')
