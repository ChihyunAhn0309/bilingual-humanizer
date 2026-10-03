"""Build source-only qualitative ledgers. No model, network, or rewrite calls."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCES = HERE.parent / 'transfer'
registry = json.loads((SOURCES / 'registry.json').read_text(encoding='utf-8'))
freeze = json.loads((SOURCES / 'FREEZE.json').read_text(encoding='utf-8'))
assert hashlib.sha256((SOURCES / 'registry.json').read_bytes()).hexdigest() == freeze['registry_sha256']

reviews = {
 'T01': {
  'summary': 'A coherent hypothetical explanation of workshop delays, followed by a limited communication proposal. The prose uses several tidy contrasts, but each serves the explanation. Concrete mechanisms and careful qualifications counter an interpretation based only on generic polish. Known AI origin comes from the generation record, not these stylistic observations. AI/Human probabilities are unavailable here because inference was deliberately not run and no quantitative result was supplied.',
  'document_analysis': {
   'structure': 'P1 separates bench availability from the availability of a relevant specialist; P2 adds owner approval as a second source of delay; P3 proposes status labels and specifies their limits. This progression is deliberately orderly. It is also a sensible explanatory sequence, so orderliness alone carries little authorship information.',
   'reasoning_specificity': 'P1 gives four benches, one electrical volunteer attending on alternate Saturdays, and a later-arriving chair as a causal counterexample to a simple arrival queue. P2 identifies approval before purchasing a part as another necessary condition. P3 only claims improved information; it does not promise more labour or faster completion. These are specific internal premises of a fictional example, not verified observations of a real workshop.',
   'voice_consistency': 'The calm public-facing explanatory voice is sustained throughout P1-P3. The article explains why a visitor might misread a delay without accusing visitors or volunteers. P2\'s unfinished/neglected distinction is a slightly more pointed rhetorical moment, but it remains consistent with that explanatory purpose.',
   'rhythm_repetition': 'P1 contains the short sentence "She comes on alternate Saturdays." within longer causal sentences. P2 ends with a balanced unfinished/neglected contrast. P3 has two consecutive sentences beginning "They would"; the first limits expectations and the second names the benefit. That local repetition is real, but it is not document-wide uniformity. The profiler reports 13 rough sentences; these counts are descriptive, not an authorship threshold.',
   'language_features': 'English is directly readable and idiomatic. "rather than simply", the repeated "calling", and "They would" make distinctions explicit. "may", "could", "would", and "if anything" preserve scope and uncertainty. Generic phrases such as "move forward" could be tightened editorially, but in P2 they refer to a concrete blocked repair. No word or punctuation mark is treated as diagnostic.',
   'citations_provenance': 'No citations, quotations from real people, or externally checkable claims are offered. P1 expressly calls Bell Street fictional; the registry identifies the entire source as generated synthetic material. Status-board labels are invented example labels. The source hash matches the frozen registry. This verifies input identity, not external authorship authentication; the local session record supplies known AI origin.'
  },
  'findings': [
   {
    'id':'E1','basis':'style_observation','direction':'ai_like','strength':'weak',
    'quotes':['The queue is organized partly by the work required, rather than simply by arrival time.','Calling that job unfinished is accurate; calling it neglected may not be.'],
    'observation':'P1 and P2 each finish by explicitly contrasting two ways of interpreting the same repair delay. The second contrast repeats "calling" across a semicolon.',
    'interpretation':'The repeated explanatory wrap-up creates a polished, planned cadence that can occur in generated exposition. The claim is about visible rhetoric, not a model feature or proof of origin.',
    'human_alternative':'A human explainer could use these contrasts to correct two plausible misunderstandings: first-come service and neglect. Both endings add a distinction rather than merely restating a slogan.',
    'discriminating_evidence':'Draft history could show whether the contrasts were drafted, edited, or generated. No stylistic comparison corpus or detector attribution has been supplied.'
   },
   {
    'id':'E2','basis':'style_observation','direction':'human_compatible','strength':'weak',
    'quotes':['She comes on alternate Saturdays.','A lamp waiting for her may therefore stay on the shelf while a chair, brought in later, goes straight to someone who works with wood.'],
    'observation':'The schedule and the lamp/chair comparison give a concrete mechanism for unequal waits; they are not disconnected decorative detail.',
    'interpretation':'These details counter a characterization of the source as vague or padded and are compatible with careful explanatory writing. They do not indicate human origin: the case is known to be synthetic.',
    'human_alternative':'A human author could construct this same hypothetical to make a resource bottleneck accessible to visitors.',
    'discriminating_evidence':'Observed workshop records would be needed if the example were claimed as real. Here the fictional premise is explicit, and provenance comes from the generation record.'
   },
   {
    'id':'E3','basis':'style_observation','direction':'neutral','strength':'weak',
    'quotes':["Volunteers need an owner's agreement before buying a replacement part.",'Until the owner replies, a repair may be ready to continue but unable to move forward.'],
    'observation':'The second sentence states the practical consequence of the approval requirement in the first. "move forward" is conventional wording, but the dependency is explicit.',
    'interpretation':'A generated explanation can use this condition-and-consequence pair. Its conventional phrasing alone gives no directional authorship evidence in this context.',
    'human_alternative':'A human service writer could spell out the dependency because readers may assume that every unfinished repair is actively being worked on.',
    'discriminating_evidence':'Earlier drafts or an audience comprehension test would distinguish unnecessary restatement from useful clarification; neither is available.'
   },
   {
    'id':'E4','basis':'style_observation','direction':'ai_like','strength':'weak',
    'quotes':['They would not create extra volunteer hours or guarantee a completion date.','They would at least give owners a better idea of what, if anything, they can do next.'],
    'observation':'P3 ends with two consecutive "They would" sentences, first denying a capacity benefit and then asserting an information benefit.',
    'interpretation':'The symmetrical close is compatible with generated explanatory prose, although this observation overlaps with E1 and must not count as an independent authorship vote.',
    'human_alternative':'Parallel wording efficiently keeps the same subject while distinguishing a limited communication improvement from an operational promise.',
    'discriminating_evidence':'A local deletion or model attribution experiment would be needed to claim a measured model response. None was run. Editorial preference can be judged separately without such a claim.'
   },
   {
    'id':'E5','basis':'style_observation','direction':'human_compatible','strength':'weak',
    'quotes':['The workshop could make these distinctions clearer on its status board.','what, if anything, they can do next.'],
    'observation':'The proposal is marked by "could", and the final qualification allows for the owner to have no available action.',
    'interpretation':'The limited recommendation counters an allegation of inflated certainty or an obligatory upbeat ending. It is compatible with attentive human editing and equally reproducible by AI.',
    'human_alternative':'A knowledgeable human writer could avoid promising action or faster repairs when better labels cannot supply specialist time.',
    'discriminating_evidence':'Writing history is needed to identify the process. The qualifiers themselves establish only the scope of the claim.'
   }
  ],
  'paragraph_reviews': [
   {'paragraph_id':'P1','status':'reviewed','assessment':'Role: explain the first bottleneck. The alternate-Saturday schedule and lamp/chair comparison make the reasoning accessible. The explicit closing contrast is mildly polished but appropriate to the purpose. Counterexplanation: a human explainer would reasonably correct first-come assumptions in this way. No strong style-only authorship inference. Preserve four benches, the one relevant volunteer, her schedule, and the partly/possibly qualified queue claim.','finding_ids':['E1','E2']},
   {'paragraph_id':'P2','status':'reviewed','assessment':'Role: add a separate approval bottleneck. The condition and its consequence are coherent. The semicolon contrast is rhetorically neat, not evidence of a universal AI formula. Counterexplanation: it distinguishes unfinished work from possible neglect without denying that neglect could ever happen. Preserve owner agreement before purchase and the "may not" qualification.','finding_ids':['E1','E3']},
   {'paragraph_id':'P3','status':'reviewed','assessment':'Role: suggest status labels and limit the claimed benefit. Two "They would" openings produce local parallelism, while the lack of extra hours or guaranteed dates prevents overclaiming. Counterexplanation: deliberate parallelism makes the proposal easier to assess. Preserve the hypothetical suggestion, both types of waiting, and the possibility that an owner can do nothing next.','finding_ids':['E4','E5']}
  ]
 },
 'T02': {
  'summary': 'A clear operational memo that announces a temporary trial, assigns concrete actions, gives an outage fallback, and leaves the permanent decision open. Procedural repetition and neat paragraph functions follow the genre. There is little useful style-only evidence of authorship. The known AI origin is recorded separately. AI/Human probabilities are unavailable here because inference was deliberately not run and no quantitative result was supplied.',
  'document_analysis': {
   'structure':'P1 defines the trial; P2 gives the normal return workflow and the missing-item branch; P3 covers file access and an outage fallback; P4 commits to review without assuming retention. All four paragraphs contribute different operational information. The systematic structure is useful for desk staff, not intrinsically suspicious.',
   'reasoning_specificity':'The equipment types, two desks, two-week period, kit number and return time, inspection shelf, 3 p.m. Friday deadline, named responsibility, and following-morning transcription are concrete. The safety exception and exemption from duplicate entry prevent two plausible workflow mistakes. The source does not supply calendar dates or actual organizational records because the setting is fictional.',
   'voice_consistency':'The writer uses a collegial but authoritative internal voice: "we will try" for the trial, imperatives for desk duties, "please" for direct requests, and "I will" for the writer\'s review commitment. The shift from we to I distinguishes shared operations from individual accountability rather than changing persona.',
   'rhythm_repetition':'P2 and P3 contain conditional openings with "If", plus repeated references to the file, log, and kit. The repetition keeps referents stable for a procedure. P4 is shorter than the process paragraphs. Manual reading yields 12 sentences; the profiler\'s rough count of 14 splits the abbreviation "p.m." and must not be treated as a reliable sentence measurement or a detector feature.',
   'language_features':'Plain English imperatives, clear time phrases, and explicit permissions suit a work memo. "does not need to wait" and "There is no need to enter them again" identify exemptions rather than filler. The P1 contrast limits the policy scope. Good grammar, ordinary vocabulary, repeated conditional grammar, and politeness are not diagnostic.',
   'citations_provenance':'The memo supplies no sources and needs none for its fictional internal instructions. Nia, the desks, the dates relative to the memo, and the pilot are synthetic, not verified workplace facts. The source hash matches the frozen registry. Known AI origin comes from this session\'s generation record; a matching hash alone does not authenticate authorship.'
  },
  'findings': [
   {
    'id':'E1','basis':'style_observation','direction':'neutral','strength':'weak',
    'quotes':['Starting next Monday, we will try a shared return log for borrowed projectors and audio kits.','This is a change to how we record returns, not a change to the borrowing limits.'],
    'observation':'P1 announces a trial and explicitly separates the changed record-keeping process from unchanged borrowing limits.',
    'interpretation':'The clear scope contrast could be generated, but it serves an operational distinction. It does not justify an authorship-direction flag by itself.',
    'human_alternative':'A human manager could anticipate confusion about loan policy and use the contrast to prevent it.',
    'discriminating_evidence':'Actual internal policy or draft history would distinguish the origin of these instructions; no such real-world source is claimed here.'
   },
   {
    'id':'E2','basis':'style_observation','direction':'neutral','strength':'weak',
    'quotes':['If anything is missing, leave the kit on the inspection shelf and add a short note in the log.','If the file is unavailable during the trial, use the paper sheet beside the cupboard; Nia will transfer those entries the following morning.'],
    'observation':'P2 and P3 each use an if-condition followed by an action. The first handles missing equipment; the second handles an unavailable file and assigns follow-up responsibility.',
    'interpretation':'This is repeated syntax, but the repeated structure maps distinct decision branches. Calling it an AI template would ignore the genre function.',
    'human_alternative':'A human procedure writer could deliberately standardize condition/action wording so staff can find the right response quickly.',
    'discriminating_evidence':'Staff usability feedback could assess the repetition\'s usefulness. It would not, by itself, identify the authoring process.'
   },
   {
    'id':'E3','basis':'style_observation','direction':'human_compatible','strength':'weak',
    'quotes':['Please do not mark it available while we are still checking it.','The person returning it does not need to wait at the desk unless there is an immediate safety concern.'],
    'observation':'P2 distinguishes equipment availability from whether the person returning it must remain, with a narrow safety exception.',
    'interpretation':'The distinction is practical specificity rather than generic business phrasing. It counters a claim that the prose is empty or interchangeable, but not the known AI provenance.',
    'human_alternative':'A human desk supervisor could clarify these separate states after observing staff unnecessarily detain borrowers or reissue unchecked kits. That possible motivation is not asserted as an event in this synthetic source.',
    'discriminating_evidence':'Real workflow records would be needed to establish that experience-based explanation. The text alone supplies only the policy distinction.'
   },
   {
    'id':'E4','basis':'style_observation','direction':'human_compatible','strength':'weak',
    'quotes':['By 3 p.m. this Friday, please tell Nia if you cannot open the shared file.','There is no need to enter them again yourself.'],
    'observation':'P3 gives a precise access-reporting deadline and tells desk staff not to duplicate the transcription assigned to Nia in the preceding sentence.',
    'interpretation':'These details anchor the memo to an actionable workflow and reduce ambiguity. Detail can also be generated, so it is counterevidence to vagueness, not proof of a human author.',
    'human_alternative':'A human colleague could name a contact and avoid double entry to make a small pilot workable during normal desk duties.',
    'discriminating_evidence':'The planned pilot or source notes could establish where the details came from; no real pilot is claimed.'
   },
   {
    'id':'E5','basis':'style_observation','direction':'neutral','strength':'weak',
    'quotes':['I will review the logs after the second week and ask both desks whether the extra step was useful.','We have not decided whether to keep it.'],
    'observation':'P4 assigns review responsibility and explicitly withholds a permanent decision. It does not add a generic claim of future efficiency or success.',
    'interpretation':'The ending is concise and calibrated to a trial. Either a human or AI can write this; the absence of promotional language is not an authorship test.',
    'human_alternative':'A human manager could avoid prejudging the pilot while giving staff a concrete commitment to consultation.',
    'discriminating_evidence':'An edit trail would be needed to establish the process. Subsequent real actions would test the commitment only if this were an actual memo.'
   }
  ],
  'paragraph_reviews': [
   {'paragraph_id':'P1','status':'reviewed','assessment':'Role: announce scope and timing. It is readable and complete; the contrast between logging and borrowing limits prevents a substantive misunderstanding. Neutral authorship assessment because concise scope statements are normal workplace writing. Preserve the next-Monday start, two weeks, both equipment classes, both desks, and unchanged borrowing limits.','finding_ids':['E1']},
   {'paragraph_id':'P2','status':'reviewed','assessment':'Role: specify return actions and exceptions. Conditional and negative instructions are necessary, not gratuitous formality. Practical distinctions support clarity but do not establish origin. Counterexplanation: a human procedure writer would also spell out inspection and the borrower\'s permission to leave. Preserve action order and the immediate-safety exception.','finding_ids':['E2','E3']},
   {'paragraph_id':'P3','status':'reviewed','assessment':'Role: prevent file-access trouble and define the fallback. The conditional form recurs because the situation branches. Names, times, and the no-duplicate-entry sentence matter operationally. Counterexplanation: a human colleague would reduce confusion by assigning transcription to one person. Preserve Nia\'s responsibility, following-morning timing, and the Friday deadline.','finding_ids':['E2','E4']},
   {'paragraph_id':'P4','status':'reviewed','assessment':'Role: promise review and keep the outcome undecided. The short ending fits the memo and gives an accountable next step. No forced stylistic flag is warranted. Preserve review after the second week, consultation with both desks, and the absence of a retention decision.','finding_ids':['E5']}
  ]
 },
 'T03': {
  'summary':'An understated fictional first-person reflection moves from a towel used as a warning, through a repair and uncertain memory, to a useful chair without emotional closure. Concrete details and sentence variation make the narration readable. The crafted circular object detail and refusal of a moral are still literary devices that AI can produce. Known AI origin comes from generation history. AI/Human probabilities are unavailable here because inference was deliberately not run and no quantitative result was supplied.',
  'document_analysis': {
   'structure':'P1 establishes the stalled decision and the chair\'s connection to the aunt. P2 narrates taking it apart and leaves the pale mark unexplained. P3 returns the towel to its hook, records an imperfect practical result, and leaves the broader inheritance choices open. The return of the towel supplies a modest arc without asserting emotional resolution.',
   'reasoning_specificity':'The folded towel, the old glue, one careful pull, a pale patch, an uneven floor, and a box above the wardrobe are concrete and internally connected. The text distinguishes expected resistance from easy separation and explicitly offers two explanations for the patch. These are fictional details; they are not testimony or proof of lived experience.',
   'voice_consistency':'The narrator remains matter-of-fact, mildly self-aware, and reluctant to inflate the significance of the repair. "That was my warning system" and "mostly it gave me another place to sit" share that restrained register. The aunt is not given invented speech or motives, and uncertainty is not resolved into a consoling memory.',
   'rhythm_repetition':'Short sentences such as "That was my warning system." and "I left it alone." interrupt longer sentences with subordinate clauses. The towel appears in P1 and returns in P3, giving continuity. First-person forms recur because this is a first-person reflection. The profiler reports 13 rough sentences, but no comparison distribution supports calling the rhythm more or less human.',
   'language_features':'The English is idiomatic, with ordinary material nouns and qualified statements: "seemed", "cannot remember", "might", and "mostly". The final "I would like to say ... but" construction is a recognizable essay device; its presence permits an editorial observation about a crafted ending, not an inference that the experience or writer is real.',
   'citations_provenance':'There are no external citations or attributed quotations. Every memory, relative, action, and object belongs to a synthetic scenario. The source hash matches the frozen registry, whose generation record documents AI origin. The reviewer also created this source; source-origin blinding is therefore absent. This does not expose the reviewer to candidate identities or detector scores.'
  },
  'findings': [
   {
    'id':'E1','basis':'style_observation','direction':'human_compatible','strength':'weak',
    'quotes':['with a folded towel on its seat. That was my warning system.','Visitors understood it, although I still explained the wobble every time someone came over.'],
    'observation':'P1 gives a small practical arrangement and then notes that the narrator kept explaining it despite the visitors\' understanding.',
    'interpretation':'The imperfectly efficient habit gives the narrator a specific attitude and counters a description of the prose as generic emotional exposition. It remains an invented detail, not evidence of human experience.',
    'human_alternative':'A human memoir writer could remember such a mundane warning and the redundant explanation because it shows how long the repair was deferred.',
    'discriminating_evidence':'Independent writing history or authentic personal records would be required to support lived experience; no such claim is made for this synthetic source.'
   },
   {
    'id':'E2','basis':'style_observation','direction':'human_compatible','strength':'weak',
    'quotes':['I cannot remember whether my aunt ever repaired it herself.','There is a pale patch underneath that might be a repair, or might just be where the finish wore off.'],
    'observation':'P2 explicitly separates a gap in memory from two tentative explanations of a physical mark.',
    'interpretation':'The uncertainty is specific rather than an all-purpose hedge and prevents an invented sentimental connection from being asserted. AI can intentionally write this restraint, so it is counterevidence to overconfident narration, not to documented AI origin.',
    'human_alternative':'A human narrator could honestly resist claiming an aunt\'s handiwork when the patch does not identify its cause.',
    'discriminating_evidence':'Reliable records of the object\'s history could resolve the repair question in a real case. They would still not identify who drafted this prose.'
   },
   {
    'id':'E3','basis':'style_observation','direction':'neutral','strength':'weak',
    'quotes':['That was my warning system.','I had expected the old glue to resist, but the back came away with one careful pull.','I left it alone.'],
    'observation':'The four-word and five-word sentences quoted here sit alongside a longer expectation-and-result sentence. Rhythm varies at the sentence level.',
    'interpretation':'This contradicts a blanket claim that every sentence has the same structure or length. It does not establish a human rhythm or a model\'s response to rhythm.',
    'human_alternative':'A human writer could use short sentences to mark small decisions and longer ones to carry narrative detail.',
    'discriminating_evidence':'A stated comparison corpus would be required for population claims about rhythm. No such comparison or model attribution is available.'
   },
   {
    'id':'E4','basis':'style_observation','direction':'ai_like','strength':'weak',
    'quotes':['I would like to say the afternoon settled something about keeping her things, but mostly it gave me another place to sit.','The harder choices are still in the box above the wardrobe.'],
    'observation':'P3 explicitly raises the possibility of a reflective lesson and declines it, then ends on an object that carries the unresolved choices.',
    'interpretation':'This carefully managed anti-resolution can be generated as readily as a conventional moral. It makes the ending feel composed, but it is a single literary device, not strong authorship evidence.',
    'human_alternative':'A human essayist could revise toward exactly this ending to avoid claiming a repair settled a difficult question about possessions.',
    'discriminating_evidence':'Drafts could show whether this ending developed from events or a writing prompt. Neither the emotional effect nor the absence of closure supplies that history.'
   },
   {
    'id':'E5','basis':'style_observation','direction':'neutral','strength':'weak',
    'quotes':['with a folded towel on its seat.','I moved the towel back to its hook.'],
    'observation':'A towel introduced as a warning in P1 is returned to its hook in P3, showing practical completion through the same object.',
    'interpretation':'The callback is a visible craft choice and helps continuity. Human and generated prose can both use it; it should not be counted as independent confirmation of E4.',
    'human_alternative':'A human writer might preserve the towel detail because its change of place says more economically that the chair is usable again.',
    'discriminating_evidence':'Revision history could identify how the callback was selected. The frozen text only establishes that it is present.'
   }
  ],
  'paragraph_reviews': [
   {'paragraph_id':'P1','status':'reviewed','assessment':'Role: establish delay, the towel warning, and reluctance to discard an inherited chair. Concrete detail conveys the narrator\'s attitude without naming a large emotion. Counterexplanation to an AI-style reading: a human personal essay can select the same small domestic detail. No origin claim follows. Preserve the visitors\' understanding, repeated explanation, inheritance from the aunt, and the narrator\'s limited reason for keeping it.','finding_ids':['E1','E3','E5']},
   {'paragraph_id':'P2','status':'reviewed','assessment':'Role: describe disassembly and an uncertain trace of earlier work. The expectation/result contrast is coherent, and the memory gap remains unresolved. Counterexplanation: a careful human narrator could distinguish observation from wishful inference in exactly this way. Preserve last Sunday, the one careful pull, both explanations of the patch, and leaving it alone.','finding_ids':['E2','E3']},
   {'paragraph_id':'P3','status':'reviewed','assessment':'Role: record practical success with a remaining imperfection and no broader closure. The towel callback and anti-resolution are crafted but compatible with ordinary essay revision. Counterexplanation: the writer may deliberately avoid a neat moral. Preserve the leg catching on an uneven floor, the towel\'s return, the limited gain of another seat, and the unexamined box; do not invent its contents.','finding_ids':['E4','E5']}
  ]
 }
}

for case in registry['cases']:
    case_id = case['id']
    raw = (SOURCES / case['source_file']).read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    assert digest == case['source_sha256']
    assert hashlib.sha256((SOURCES / case['constraints_file']).read_bytes()).hexdigest() == case['constraints_sha256']
    source = raw.decode('utf-8')
    index = json.loads((HERE / f'{case_id}.index.json').read_text(encoding='utf-8'))
    assert index['text_sha256'] == digest
    review = reviews[case_id]
    for finding in review['findings']:
        finding['spans'] = []
        for quote in finding.pop('quotes'):
            assert source.count(quote) == 1, (case_id, quote)
            start = source.index(quote)
            end = start + len(quote)
            para = next(p for p in index['paragraphs'] if p['start'] <= start and end <= p['end'])
            finding['spans'].append({'start':start,'end':end,'quote':quote,'paragraph_id':para['id'],'line':source.count('\n',0,start)+1})
    ledger = {
      'text_sha256':digest,
      **review,
      'review_metadata':{
        'case_id':case_id,'language':'English','genre':case['genre'],
        'created_at_utc':datetime.now(timezone.utc).isoformat(),
        'review_type':'Independent-of-candidates qualitative source review; source origin is known.',
        'reviewer_created_source':True,
        'prototype_or_development_read':False,'candidate_outputs_read':False,'detector_scores_read':False,
        'inference_run':False,'external_uploads':False,
        'measured_authorship_probabilities':None,
        'numeric_status':'Unavailable: no inference authorized in this task; quantitative results have not yet been provided.',
        'surface_measurement_source':f'{case_id}.profile.json',
        'surface_measurement_limit':'Counts are descriptive observations, not detector scores, model attributions, or population norms.',
        'known_origin':'AI-generated synthetic source in this evaluation session. Not human ground truth; no real people, events, or personal memories are claimed.',
        'provenance_record':'../transfer/registry.json',
        'coverage':{'reviewed':case['paragraph_count'],'excluded':0,'not_reviewed':0},
        'future_integration':'Preserve this pre-score ledger. Attach subsequently supplied quantitative results only after exact source-hash, schema, model-identity, coverage, and score-semantics checks. Record any later interpretation separately.'
      }
    }
    out = HERE / f'{case_id}.qualitative-ledger.json'
    assert not out.exists(), out
    out.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(case_id, len(ledger['findings']), len(ledger['paragraph_reviews']), digest)
