"""Record a source-bound, candidate-score-blind prose review; no inference."""
import hashlib
import json
import re
import stat
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parent
LAB=ROOT.parent
registry=json.loads((LAB/'transfer/registry.json').read_text(encoding='utf-8'))

assessment={
 'T01':{
  'A':{
   'dimensions':{
    'argument_structure':'The candidate takes the optional example-first route in P1, follows with owner approval in P2, and ends with the status-board proposal and its limits in P3. The causal progression and all original paragraph functions remain clear.',
    'reasoning_specificity':'The four benches, one electrical volunteer, alternate Saturdays, later-arriving chair, purchase approval, and both waiting labels survive. The modal may and scope word partly still qualify the queue example. There is no invented workshop policy or completion promise.',
    'voice_continuity':'The calm explanatory voice remains consistent. Work is queued partly by the repair required is slightly administrative in register, but fits the topic and is not a defect. There is no added blame, promotion, or condescension.',
    'rhythm_repetition':'P1 contains four sentences, including the general empty-bench claim after the example. P2 uses four short logical steps. P3 combines labels and their benefit into one longer sentence. The variation is readable; no sentence requires repair.',
    'language_features':'English is idiomatic. The conditional and negative phrases preserve scope. Calling it neglected may not be accurate is a legitimate paraphrase of the original caution. The wording remains somewhat formal, which is acceptable for the public article.',
    'citations_provenance':'The fictional designation is retained. No citations, real-world events, or new external evidence appear. The candidate is reviewed as an anonymous rewrite of known synthetic AI text; its generation method is unknown to this reviewer.'
   },
   'paragraph_assessments':[
    'P1 retains the entire resource-and-queue explanation. Starting with the lamp/chair contrast is a legitimate route. Four benches and the specialist schedule are explicit, and may/partly prevent universal claims. The general empty-bench sentence repeats the workshop noun but does not impair comprehension.',
    'P2 retains agreement before buying a part, possible waiting for the owner, the pause being hard for visitors to see, and the distinction between unfinished and possibly neglected. Its reordered approval-first opening is clear and does not blame the owner.',
    'P3 retains a proposed change rather than a reported policy, both example labels, comparison with a generic status, the qualified owner benefit, and no extra hours or guaranteed date. Moving the limit to the end is a legitimate choice.'
   ],
   'fidelity_notes':[
    'The lamp/chair possibility, all counts/schedule details, the empty-bench limitation, and partially work-based queue are preserved in candidate P1.',
    'Candidate P2 preserves both the procedural condition and the caution against inferring neglect; no source fact is lost by changing sentence order.',
    'Candidate P3 preserves the suggestion, both labels, their informational advantage, and all limits; giving them a better idea remains within the hypothetical would clause.'
   ]
  },
  'B':{
   'dimensions':{
    'argument_structure':'P1 starts with the same lamp/chair example and puts specialist availability immediately after it. It then combines bench count and capacity limitation. P2 and P3 retain the source progression from owner approval to a bounded communication proposal.',
    'reasoning_specificity':'All numbers, times, mechanisms, labels, and limitations survive. The work required partly determines the queue and arrival time is not the only consideration preserve the original partial rule. Does not necessarily mean it has been neglected preserves uncertainty.',
    'voice_continuity':'The explanatory voice is calm and slightly more conversational through contractions. It remains appropriate for a general public audience without becoming jokey or assigning blame.',
    'rhythm_repetition':'P1 groups the bench count with what an empty bench does not imply. P2 carries the owner wait and its invisibility in a single linked sentence. This makes the explanation flow smoothly without suppressing any qualification.',
    'language_features':'The paraphrases are idiomatic and clear. Capacity is an appropriate ordinary term here. The contractions do not change confidence, instruction strength, or agency. No colloquial phrase jars with the genre.',
    'citations_provenance':'The fictional workshop is still expressly fictional. No citation or purported observation is added. Candidate identity and method are unknown; natural phrasing does not establish human origin.'
   },
   'paragraph_assessments':[
    'P1 preserves every fact and qualifier while linking benches directly to the capacity claim. The lamp example still concerns possible ordering and does not become a universal service rule. The explanation of the queue is clear.',
    'P2 preserves owner agreement before purchase, a repair that may otherwise be ready, the hard-to-see pause, and non-necessary neglect. Linking the pause to the waiting sentence is a fluent alternative to the source layout.',
    'P3 preserves the hypothetical board improvement, exact example labels and generic-column comparison, qualified next-action benefit, and limits on hours/dates. Clearer labels is an accurate referent, not a new proposal.'
   ],
   'fidelity_notes':[
    'Candidate P1 retains every quantitative and causal detail. Doesn\'t always and partly retain the source limitations.',
    'Candidate P2 preserves the same approval condition and modal possibility. Doesn\'t necessarily mean it\'s been neglected is equivalent to may not be accurate to call it neglected.',
    'Candidate P3 retains the proposal and its strictly informational benefit. Could/would remain intact despite the contractions.'
   ]
  },
  'preference':{
   'choice':'B','strength':'slight','reason':'Both versions pass fidelity and read well. B links the bench count directly to the capacity limitation and folds the invisible pause into its cause, which produces a smoother explanatory flow. This is a small preference in organization and phrasing, not a repair finding or evidence of general method superiority.',
   'A_quotes':['The workshop has four benches, but only one volunteer handles electrical faults, and she comes on alternate Saturdays. An empty bench does not always mean a workshop can take another job.','A repair may be ready to continue but still have to wait for the owner\'s reply. Visitors cannot easily see that pause.'],
   'B_quotes':['The workshop has four benches, but an empty one doesn\'t always mean there\'s capacity for another job.','A repair may be ready to continue and still have to wait for that reply, a pause visitors cannot easily see.'],
   'counterconsideration':'A\'s shorter separate sentence about visitors may be easier for some readers to scan. Its more formal register is legitimate, so the preference is deliberately slight.'
  }
 },
 'T02':{
  'A':{
   'dimensions':{
    'argument_structure':'The candidate foregrounds the trial duration, then moves the Friday access check into its own paragraph before the return workflow. The outage fallback and later review follow. This five-paragraph order is sensible for pre-trial preparation and preserves all source functions.',
    'reasoning_specificity':'The two desks, equipment types, duration, start, unchanged limits, logging order, inspection branch, availability restriction, safety exception, deadline, paper location, Nia\'s transcription duty, and undecided outcome are all retained.',
    'voice_continuity':'The memo remains collegial and authoritative. Contractions make it more conversational, but Please don\'t still directs staff not to mark the kit available. Needn\'t is a valid permission to leave, not an instruction to leave.',
    'rhythm_repetition':'The isolated deadline is easy to find. Repeated if-conditions serve distinct operational branches. The workflow remains a longer paragraph because those actions belong together. The shorter review close is proportionate.',
    'language_features':'The English is clear and idiomatic. Can\'t, don\'t, needn\'t, and haven\'t are acceptable in an internal memo. Pronoun it has a clear kit referent in context. None of those choices weakens the operational requirements.',
    'citations_provenance':'No new workplace facts, actual dates, citations, or identities are introduced. The relative days and synthetic setting remain as supplied. The anonymous method and candidate detector scores remain unseen.'
   },
   'paragraph_assessments':[
    'P1 combines duration, next-Monday start, equipment, and both desks into one announcement and keeps borrowing limits unchanged. Only the way we record returns is changing is faithful within the announced trial scope.',
    'P2 preserves Nia as contact, the 3 p.m. Friday deadline, and the inability-to-open trigger. Separating this earlier preparation from the later outage fallback improves scanning without changing urgency.',
    'P3 preserves logging before cupboard storage, the missing-item shelf and note, the prohibition on availability during checking, and permission to leave except for an immediate safety concern. Needn\'t is a legitimate stylistic choice, not a defect.',
    'P4 retains the trial-only file-unavailability condition, the paper sheet beside the cupboard, Nia\'s next-morning transfer, and no duplicate entry by staff. Splitting the original semicolon does not change assigned responsibility.',
    'P5 preserves the writer\'s review after week two, consultation with both desks, and undecided retention. The short close is effective and does not need an added justification or motivational claim.'
   ],
   'fidelity_notes':[
    'Original P1 maps to candidate P1: every timing, scope, and non-change claim survives.',
    'Original P2 maps to candidate P3: all required actions, sequence, prohibition, permission, and exception survive. Contractions retain their force.',
    'Original P3 maps to candidate P2 and P4: the access deadline and fallback are separated without losing any trigger, person, time, location, or exemption.',
    'Original P4 maps to candidate P5: review commitment and undecided outcome both remain explicit.'
   ]
  },
  'B':{
   'dimensions':{
    'argument_structure':'The same five-paragraph organization separates pre-trial access reporting from the return workflow and outage process. The final paragraph front-loads the review timing. All stages remain easy to locate.',
    'reasoning_specificity':'All required operational details and restrictions survive. The explicit kit referent and exception-first sentence clarify the same original instructions without adding a requirement. No new process is introduced.',
    'voice_continuity':'First-person contractions in the announcement and review coexist naturally with full negative forms in instructions. That variation reflects function and does not create an inconsistent persona. The overall voice remains collegial and direct.',
    'rhythm_repetition':'The short access paragraph and separate fallback aid scanning. The safety condition comes first in its sentence, and the review timing comes first in P5. These are legitimate emphasis choices, neither inherently better nor defective.',
    'language_features':'The wording is plain and precise. Mark the kit available names the referent explicitly; does not need to wait preserves permission rather than ordering departure. No unnecessary jargon, invented formality, or changed certainty appears.',
    'citations_provenance':'The candidate adds no sources or real-world claims beyond the fictional original. No absolute dates are invented. Its method identity and scores are not known to the reviewer.'
   },
   'paragraph_assessments':[
    'P1 retains the trial duration, next-Monday start, shared log, equipment types, both desks, and unchanged borrowing limits. The phrase This trial changes how we record returns accurately describes the limited scope.',
    'P2 retains the exact contact, deadline, and access-failure condition. Cannot is simply a fuller form than can\'t and is equally suitable here.',
    'P3 retains all action sequence and missing-item requirements. Mark the kit available makes the referent explicit. Moving the safety exception to the start leaves the permission and exception unchanged.',
    'P4 retains paper fallback location, the outage trigger, Nia\'s following-morning duty, and no duplicate entry. The two sentences remain clear and actionable.',
    'P5 preserves review after the second week, both desks\' input, the usefulness question, and the undecided outcome. Fronting the time phrase is a valid emphasis choice.'
   ],
   'fidelity_notes':[
    'Original P1 maps to candidate P1 with all scope and time details unchanged.',
    'Original P2 maps to candidate P3. Explicit kit and the fronted safety condition preserve the same referent and logic.',
    'Original P3 maps to candidate P2 and P4 without omission or reassignment.',
    'Original P4 maps to candidate P5. Fronting after the second week does not change when review or consultation occurs.'
   ]
  },
  'preference':{
   'choice':'tie','strength':'no_material_preference','reason':'Both versions are clear, complete, and equally usable as an internal memo. A is slightly more conversational and compact; B makes the kit referent explicit and uses fuller negative forms. The difference does not produce a meaningful reader-quality advantage in this context.',
   'A_quotes':['Please don\'t mark it available while we\'re still checking it. The person returning it needn\'t wait at the desk unless there\'s an immediate safety concern.'],
   'B_quotes':['Please do not mark the kit available while we are still checking it. Unless there is an immediate safety concern, the person returning it does not need to wait at the desk.'],
   'counterconsideration':'A house style preferring contractions could favor A; a procedural template preferring full negatives could favor B. Neither preference is supplied, and both retain the required force.'
  }
 },
 'T03':{
  'A':{
   'dimensions':{
    'argument_structure':'P1 foregrounds the warning towel and retains the winter delay and inherited chair. P2 gives disassembly and uncertainty, with the patch before the memory gap. P3 states practical gain before the wished-for broader resolution and unresolved box. All source functions survive.',
    'reasoning_specificity':'The towel, kitchen corner, visitors, aunt, one careful pull, expected glue resistance, ambiguous patch, uneven floor, and wardrobe box all remain. The source\'s uncertainty and limited emotional claim are preserved; no tools, memories, feelings, or box contents are invented.',
    'voice_continuity':'The first-person voice remains understated and a little formal. Naming my aunt\'s things instead of her things clarifies the reference without changing emotional intensity. The source\'s refusal of closure is intact.',
    'rhythm_repetition':'Short opening and action sentences are mixed with longer reflective ones. The final sentence carries both the wish for resolution and the remaining choices. This is clear, though slightly denser than B\'s separated beats.',
    'language_features':'English is idiomatic. The semicolon joining inheritance and reluctance is legitimate. Repair or just where the finish wore off leaves both alternatives under might. I left the patch alone makes the original pronoun referent explicit.',
    'citations_provenance':'All experiences remain fictional. No authentic personal history or quotation is added. A readable anecdote is not human-authorship evidence; candidate method and scores are unknown.'
   },
   'paragraph_assessments':[
    'P1 keeps the warning system, winter-long location, visitors understanding despite repeated explanations, inheritance, and reason for not discarding the chair. The semicolon is a normal narrative choice, not an artificiality defect.',
    'P2 preserves last Sunday, the careful pull, expected resistance, uncertainty about the aunt\'s repairs, both possible causes of the pale patch, and leaving it alone. Moving the patch before the memory sentence does not resolve the uncertainty.',
    'P3 preserves practical usability, the leg catching on an uneven floor, the towel returned to the hook, modest gain, wish for a broader resolution, and the unresolved box. The final but-clause still rejects a claim of closure; no necessary repair is warranted.'
   ],
   'fidelity_notes':[
    'Original P1 maps to candidate P1. The narrator\'s personal reluctance remains a personal judgment rather than a universal rule.',
    'Original P2 maps to candidate P2. Reordering the patch and memory statements keeps both uncertainties; explicit patch is a supported pronoun resolution.',
    'Original P3 maps to candidate P3. Moving practical gain earlier retains both the wish for resolution and the statement that harder choices remain.'
   ]
  },
  'B':{
   'dimensions':{
    'argument_structure':'The towel leads P1, the repair action leads P2, and moving the towel back opens P3. The chair\'s remaining imperfection and the limited practical gain follow. The source\'s unresolved ending is retained in its own closing sentence.',
    'reasoning_specificity':'All objects, times, actions, and qualifications survive. Both explanations of the patch remain tentative. Present perfect I\'ve moved still reports the completed towel move and does not introduce a new event or meaningful timing claim.',
    'voice_continuity':'Contractions make the narrator slightly more conversational while preserving understatement. The voice never claims healing, sentimental discovery, or a moral. Her things has the same clear aunt referent as in the source.',
    'rhythm_repetition':'The longer first action sentence in P2 is followed by the short expectation sentence. P3 separates the wish for a larger meaning from the modest result, then leaves the box as a separate final beat. This supports the restrained voice without losing meaning.',
    'language_features':'The phrasing is ordinary and idiomatic. I\'d, can\'t, and there\'s are stylistic choices, not authorship signals. Mostly, though supplies the contrast that prevents the preceding wish from being read as an achieved resolution.',
    'citations_provenance':'No sources, actual experiences, dialogue, motives, or people are added. The story remains synthetic. Candidate provenance is not inferred from its conversational tone or concrete detail.'
   },
   'paragraph_assessments':[
    'P1 preserves every setting and behavioral detail, including the visitors understanding and continued explanations. The towel-first wording is concrete and relaxed. Contractions do not add emotion or alter the inherited relationship.',
    'P2 preserves last Sunday and the contrast between expected resistance and a one-pull separation. The memory gap precedes the two possible explanations as in the source. I left it alone still clearly refers to the patch in context.',
    'P3 preserves the completed towel move, usable yet imperfect chair, wished-for emotional resolution, modest actual gain, and unresolved box. The change in order and tense is legitimate narration. The short Mostly, though sentence keeps the crucial contrast explicit.'
   ],
   'fidelity_notes':[
    'Original P1 maps to candidate P1 with all details and personal judgment retained.',
    'Original P2 maps to candidate P2. The standalone expectation sentence does not invert events or make the uncertain repair history certain.',
    'Original P3 maps to candidate P3. I\'ve moved is a completed action; the wish and its limiting contrast remain separate but connected, and the choices remain unresolved.'
   ]
  },
  'preference':{
   'choice':'B','strength':'slight','reason':'Both versions retain the restrained voice and all meaning. B\'s concrete towel-first opening and separated wish/practical-result/final-box beats feel a little more natural and give the quiet ending more room. A is also good and slightly more compact in its final reflection.',
   'A_quotes':['My warning system was a folded towel on the seat of a loose chair.','The afternoon mostly gave me another place to sit. I would like to say it settled something about keeping my aunt\'s things, but the harder choices are still in the box above the wardrobe.'],
   'B_quotes':['A folded towel on the loose chair\'s seat was my warning system.','I\'d like to say that afternoon settled something about keeping her things. Mostly, though, it gave me another place to sit. The harder choices are still in the box above the wardrobe.'],
   'counterconsideration':'A\'s explicit my aunt\'s things and combined final sentence may suit a reader who prefers a more formal, compact reflection. B\'s contractions and pauses are a slight genre preference, not universal markers of quality.'
  }
 }
}

mapping={'T01':{'P1':['P1'],'P2':['P2'],'P3':['P3']},'T02':{'P1':['P1'],'P2':['P3'],'P3':['P2','P4'],'P4':['P5']},'T03':{'P1':['P1'],'P2':['P2'],'P3':['P3']}}

def paragraphs(text):
    return [{'paragraph_id':f'P{i+1}','start':m.start(),'end':m.end(),'quote':m.group(0)} for i,m in enumerate(re.finditer(r'\S[^\n]*(?:\n(?!\s*\n)[^\n]+)*',text))]

def anchor(text,quote):
    assert text.count(quote)==1,quote
    start=text.index(quote)
    return {'start':start,'end':start+len(quote),'quote':quote,'offset_unit':'zero_based_unicode_codepoints_end_exclusive'}

result={
 'schema_version':1,'round':1,'reviewed_at_utc':datetime.now(timezone.utc).isoformat(),
 'status':'frozen_before_candidate_scores_or_identities',
 'review_scope':'All three anonymous pairs, every candidate paragraph, all frozen source propositions and speech-act constraints, reader suitability, and six qualitative dimensions. No rewrites or inference.',
 'blindness_record':{'candidate_identities_read':False,'candidate_scores_read':False,'prototype_or_development_read':False,'baseline_or_prototype_output_directories_read':False,'permitted_blind_pair_files_only':True,'source_scores_previously_seen':True,'source_scores_limit':'Common source feedback was known for both methods; no candidate model output existed at release. Preference is based on prose and source fidelity.','reviewer_created_synthetic_sources':True},
 'inference_run':False,'external_uploads':False,
 'decision_rule':'A faithful alternative is not a defect. Mark only actual proposition, uncertainty, role, permission, request-strength, or material voice changes as necessary repairs. Reader preferences may be slight or tied. Do not infer method identity or model response.',
 'cases':[]
}

for source_case in registry['cases']:
    cid=source_case['id']
    source_raw=(LAB/'transfer'/source_case['source_file']).read_bytes()
    source=source_raw.decode('utf-8')
    assert hashlib.sha256(source_raw).hexdigest()==source_case['source_sha256']
    constraints_raw=(LAB/'transfer'/source_case['constraints_file']).read_bytes()
    assert hashlib.sha256(constraints_raw).hexdigest()==source_case['constraints_sha256']
    constraints=json.loads(constraints_raw)
    source_paras=paragraphs(source)
    case={'case_id':cid,'genre':source_case['genre'],'original_sha256':source_case['source_sha256'],'constraints_sha256':source_case['constraints_sha256'],'candidates':{}}
    texts={}
    for label in ['A','B']:
        p=LAB/'blind-pairs'/cid/f'{label}.txt'
        raw=p.read_bytes();text=raw.decode('utf-8');texts[label]=text
        paras=paragraphs(text)
        comments=assessment[cid][label]
        assert len(paras)==len(comments['paragraph_assessments'])
        paragraph_reviews=[]
        for para,comment in zip(paras,comments['paragraph_assessments']):
            paragraph_reviews.append({**para,'status':'reviewed','assessment':comment,'necessary_repair':False})
        coverage=[]
        assert len(comments['fidelity_notes'])==len(constraints['paragraph_constraints'])
        for original,note in zip(constraints['paragraph_constraints'],comments['fidelity_notes']):
            original_para=next(x for x in source_paras if x['paragraph_id']==original['paragraph_id'])
            covered=[next(x for x in paras if x['paragraph_id']==pid) for pid in mapping[cid][original['paragraph_id']]]
            coverage.append({
                'original_paragraph_id':original['paragraph_id'],'original_anchor':original_para,
                'candidate_paragraph_ids':mapping[cid][original['paragraph_id']],
                'candidate_anchors':covered,
                'proposition_checks':[{'constraint':item,'pass':True} for item in original['propositions']],
                'speech_act_checks':[{'constraint':item,'pass':True} for item in original['speech_acts']],
                'reason':note
            })
        case['candidates'][label]={
          'file':str(p.resolve()),'sha256':hashlib.sha256(raw).hexdigest(),'word_count_whitespace':len(text.split()),
          'fidelity_pass':True,'reader_eligible':True,'necessary_repairs':[],
          'decision':'Retain as a legitimate faithful version; no necessary repair identified.',
          'paragraph_assessments':paragraph_reviews,'six_dimension_review':comments['dimensions'],
          'full_constraint_coverage':coverage,
          'voice_constraint_checks':[{'constraint':v,'pass':True} for v in constraints['voice_constraints']],
          'coverage':{'paragraphs_total':len(paras),'reviewed':len(paras),'excluded':0,'not_reviewed':0}
        }
    pref=assessment[cid]['preference']
    case['pairwise_reader_preference']={
       'choice':pref['choice'],'strength':pref['strength'],'reason':pref['reason'],
       'exact_candidate_evidence':{label:[anchor(texts[label],q) for q in pref[f'{label}_quotes']] for label in ['A','B']},
       'counterconsideration':pref['counterconsideration'],
       'fidelity_overrides_applied':False,'method_identity_inference':None
    }
    result['cases'].append(case)

result['aggregate']={'candidate_count':6,'fidelity_pass_count':6,'reader_eligible_count':6,'necessary_repair_count':0,'paragraphs_reviewed':sum(c['candidates'][x]['coverage']['reviewed'] for c in result['cases'] for x in ['A','B']),'anonymous_preferences':{'T01':'B','T02':'tie','T03':'B'},'claim_limit':'Two slight B preferences and one tie describe these particular prose pairs only. They cannot establish a general method advantage, detector advantage, or authorship.'}
out=ROOT/'round-1.json'
assert not out.exists(),out
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
manifest={'round':1,'frozen_at_utc':datetime.now(timezone.utc).isoformat(),'review_file':'round-1.json','review_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'candidate_hashes':{c['case_id']:{label:c['candidates'][label]['sha256'] for label in ['A','B']} for c in result['cases']},'no_identity_or_candidate_score_disclosure_before_freeze':True,'amendment_rule':'Keep this review unchanged. Any later measured interpretation or corrections require a separate dated artifact and explicit rationale.'}
lock=ROOT/'round-1.freeze.json'
assert not lock.exists(),lock
lock.write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8',newline='\n')
out.chmod(stat.S_IREAD);lock.chmod(stat.S_IREAD)
print(json.dumps({'review':str(out),'sha256':manifest['review_sha256'],'aggregate':result['aggregate']},indent=2))
