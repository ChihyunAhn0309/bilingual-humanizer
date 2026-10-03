"""Validate saved rewrite/feedback records, not semantic truth or authorship. No inference."""
import argparse
import json
from pathlib import Path
import re
import sys

from local_feedback import digest, normalize


DIMENSIONS = ('structure', 'reasoning_specificity', 'voice_consistency',
              'rhythm_repetition', 'language_features', 'citations_provenance')


def require(condition, message):
    if not condition:
        raise ValueError(message)


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def read_ref(root, ref):
    require(isinstance(ref, dict) and nonempty(ref.get('path')), 'Missing artifact reference')
    path = (root / ref['path']).resolve()
    require(path.is_relative_to(root), 'Artifact escapes the session workspace')
    raw = path.read_bytes()
    require(ref.get('sha256') == digest(raw), 'Stale artifact hash: ' + ref['path'])
    return raw


def json_ref(root, ref):
    value = json.loads(read_ref(root, ref))
    require(isinstance(value, dict), 'Expected a JSON object artifact')
    return value


def anchor(text, span):
    require(isinstance(span, dict), 'Missing exact span')
    start, end = span.get('start'), span.get('end')
    require(type(start) is int and type(end) is int and 0 <= start < end <= len(text),
            'Invalid Unicode codepoint span')
    require(span.get('quote') == text[start:end], 'Stale or invented exact quote')
    return start, end


def paragraphs(text):
    # Same blank-line/codepoint convention as detector evidence.py.
    spans, cursor = [], 0
    for match in list(re.finditer(r'(?:\r?\n)[ \t]*(?:\r?\n)+', text)) + [None]:
        end = match.start() if match else len(text)
        start = cursor
        while start < end and text[start].isspace():
            start += 1
        while end > start and text[end - 1].isspace():
            end -= 1
        if start < end:
            spans.append((f'P{len(spans) + 1}', start, end))
        cursor = match.end() if match else len(text)
    return spans


def review_findings(report, raw):
    text = raw.decode('utf-8')
    require(report.get('schema_version') == 2 and report.get('mode') == 'anchored_explanation'
            and report.get('text_sha256') == digest(raw), 'Missing or stale validated review')
    require(nonempty(report.get('summary')), 'Missing review summary')
    require('authorship_probabilities' in report and report['authorship_probabilities'] is None,
            'Validated review authorship probabilities must be explicitly null')
    dimensions = report.get('document_analysis', {})
    require(isinstance(dimensions, dict) and all(nonempty(dimensions.get(d))
            and not dimensions[d].startswith('Not assessed') for d in DIMENSIONS), 'Incomplete document analysis')
    findings = report.get('findings')
    require(isinstance(findings, list), 'Missing review findings')
    by_id = {}
    for finding in findings:
        require(isinstance(finding, dict) and nonempty(finding.get('id'))
                and finding['id'] not in by_id, 'Invalid or duplicate finding ID')
        require(all(nonempty(finding.get(k)) for k in ('observation', 'interpretation',
                    'human_alternative', 'discriminating_evidence')), 'Incomplete finding evidence')
        require(finding.get('basis') in ('style_observation', 'provider_highlight', 'local_occlusion',
                    'local_feature_contribution', 'documented_history')
                and finding.get('direction') in ('ai_like', 'human_compatible', 'neutral')
                and finding.get('strength') in ('weak', 'moderate', 'strong'), 'Invalid finding evidence type')
        require(finding['basis'] == 'style_observation' or nonempty(finding.get('source_record')),
                'Missing finding source record')
        require(isinstance(finding.get('spans'), list) and finding['spans'], 'Missing finding spans')
        for span in finding['spans']:
            anchor(text, span)
        by_id[finding['id']] = finding
    expected, reviews = paragraphs(text), report.get('paragraph_reviews')
    require(expected and isinstance(reviews, list) and len(reviews) == len(expected), 'Incomplete paragraph review')
    for (pid, start, end), review in zip(expected, reviews):
        require(isinstance(review, dict) and review.get('paragraph_id') == pid
                and review.get('start') == start and review.get('end') == end
                and review.get('text') == text[start:end] and review.get('status') == 'reviewed'
                and nonempty(review.get('assessment')), 'Incomplete or stale paragraph review')
        links = review.get('finding_ids')
        require(isinstance(links, list) and all(fid in by_id for fid in links), 'Unknown paragraph finding')
        require(all(any(s['start'] < end and start < s['end'] for s in by_id[fid]['spans'])
                    for fid in links), 'Paragraph finding does not overlap its paragraph')
    coverage = report.get('coverage', {})
    require(coverage.get('paragraphs_total') == len(expected)
            and coverage.get('paragraphs_reviewed') == len(expected)
            and coverage.get('paragraphs_excluded') == 0 and coverage.get('review_fraction') == 1,
            'Review does not cover the whole document')
    return by_id


def validate(path):
    path = Path(path).resolve()
    root = path.parent
    session = json.loads(path.read_bytes())
    require(isinstance(session, dict) and type(session.get('schema_version')) is int
            and session['schema_version'] == 1, 'Invalid session schema')
    language = session.get('language')
    require(language in ('ko', 'en'), 'Unsupported language')
    original = read_ref(root, session.get('source'))
    original.decode('utf-8')
    limit = session.get('revision_limit', 3)
    require(type(limit) is int and limit >= 0, 'Invalid revision budget')
    require(limit <= 3 or nonempty(session.get('budget_authorization')), 'Higher budget needs explicit user instruction')
    prior = session.get('prior_revisions_used', 0)
    require(type(prior) is int and prior >= 0, 'Invalid prior revision count')
    require(prior == 0 or nonempty(session.get('prior_revision_note')), 'Prior revisions need a provenance note')
    rounds = session.get('rounds')
    require(isinstance(rounds, list) and rounds, 'Missing source review round')
    checked, previous, ids, artifacts = [], None, set(), set()
    for index, item in enumerate(rounds):
        require(isinstance(item, dict) and nonempty(item.get('id')) and item['id'] not in ids,
                'Invalid or duplicate round ID')
        ids.add(item['id'])
        raw = read_ref(root, item.get('candidate'))
        text = raw.decode('utf-8')
        require(index != 0 or raw == original, 'First round must review the immutable source')
        for key in ('feedback', 'review', 'native'):
            ref = item.get(key)
            if ref is not None:
                artifact = (root / ref['path']).resolve()
                require(artifact not in artifacts, 'Every round needs fresh feedback/review artifacts')
                artifacts.add(artifact)
        feedback = json_ref(root, item.get('feedback'))
        native = None
        require(feedback.get('input_sha256') == digest(raw), 'Feedback belongs to another candidate')
        if feedback.get('status') == 'completed':
            native = json_ref(root, item.get('native'))
            normalized = normalize(native, raw, language)
            require(all(feedback.get(k) == v for k, v in normalized.items()), 'Feedback differs from native result')
            require(feedback.get('raw_result_sha256') == item['native']['sha256'], 'Native receipt binding missing')
        else:
            require(feedback.get('status') in ('error', 'unavailable')
                    and 'human_percent' in feedback and feedback['human_percent'] is None
                    and 'native_class_probabilities' in feedback and feedback['native_class_probabilities'] is None
                    and nonempty(feedback.get('error', feedback.get('reason'))), 'Unavailable score must remain null')
            if item.get('native') is not None:
                read_ref(root, item['native'])  # Retain a failed artifact, never reinterpret it as a score.
            normalized = {'human_percent': None, 'native_class_probabilities': None, 'scope': 'unavailable'}
        report = json_ref(root, item.get('review'))
        findings = review_findings(report, raw)
        if 'measured_output' in report:
            require(native is not None and normalized['native_class_probabilities'] is not None,
                    'Review includes unavailable numbers')
            measured = {'mode': native.get('mode'), 'model': normalized['model'],
                        'model_sha256': normalized['model_sha256'], 'measured_at_utc': normalized['measured_at_utc'],
                        'class_probabilities': normalized['native_class_probabilities'],
                        'known_limitations': native.get('known_limitations', native.get('known_limits', [])),
                        'applicability_cautions': native.get('applicability_cautions', [])}
            measured.update({k: native.get(k) for k in ('revision', 'calibration', 'language_scope',
                                                      'independently_calibrated_here', 'validation_status')})
            require(isinstance(report['measured_output'], dict)
                    and all(report['measured_output'].get(k) == v for k, v in measured.items()),
                    'Review includes unverified or inconsistent numbers')
        triage = item.get('triage')
        require(isinstance(triage, list), 'Missing finding triage')
        decisions = {}
        for decision in triage:
            require(isinstance(decision, dict) and decision.get('finding_id') in findings
                    and decision['finding_id'] not in decisions, 'Unknown or duplicate triage finding')
            require(decision.get('decision') in ('revise', 'retain', 'unresolved')
                    and nonempty(decision.get('reason')), 'Missing triage decision or reason')
            decisions[decision['finding_id']] = decision['decision']
        require(set(decisions) == set(findings), 'Finding vanished from triage')
        followup = item.get('followup', [])
        require(isinstance(followup, list), 'Invalid followup list')
        expected = {} if previous is None else {fid: decision for fid, decision in previous['decisions'].items()
                                               if decision != 'retain'}
        seen = set()
        for edge in followup:
            require(isinstance(edge, dict) and previous is not None
                    and edge.get('parent_round') == previous['id'] and edge.get('finding_id') in expected
                    and edge['finding_id'] not in seen, 'Unknown or duplicate parent finding')
            fid = edge['finding_id']
            seen.add(fid)
            before = anchor(previous['text'], edge.get('before'))
            after = anchor(text, edge.get('after'))
            require(any(s['start'] < before[1] and before[0] < s['end']
                        for s in previous['findings'][fid]['spans']), 'Before span misses parent finding')
            require(edge.get('status') in ('resolved', 'carried') and nonempty(edge.get('reason')),
                    'Followup needs a reviewed outcome and reason')
            links = edge.get('finding_ids')
            require(isinstance(links, list) and all(f in findings for f in links), 'Unknown followup finding')
            if edge['status'] == 'carried':
                require(links and all(decisions[f] != 'retain' for f in links), 'Carried finding must remain actionable')
                require(all(any(s['start'] < after[1] and after[0] < s['end'] for s in findings[f]['spans'])
                            for f in links), 'After span misses a linked carried finding')
            else:
                require(not links, 'Resolved finding cannot link to open findings')
                require(expected[fid] != 'revise' or (raw != previous['raw']
                        and edge['before']['quote'] != edge['after']['quote']),
                        'Accepted revision needs a changed exact passage and followup review')
        require(seen == set(expected), 'Open parent finding vanished without followup')
        for gate in ('fidelity', 'reader'):
            require(isinstance(item.get(gate), dict) and type(item[gate].get('eligible')) is bool
                    and nonempty(item[gate].get('reason')), 'Missing fidelity or reader review')
        require(item['fidelity'].get('source_sha256') == digest(original), 'Fidelity review has a different source')
        require(type(item.get('improvement')) is bool and nonempty(item.get('improvement_reason')),
                'Missing reader improvement assessment or reason')
        open_ids = [fid for fid, decision in decisions.items() if decision != 'retain']
        prior_human = checked[-1]['human_percent'] if checked else None
        human = normalized['human_percent']
        checked.append({'id': item['id'], 'candidate': item['candidate'], 'human_percent': normalized['human_percent'],
                        'native_class_probabilities': normalized['native_class_probabilities'], 'scope': normalized['scope'],
                        'fidelity_eligible': item['fidelity']['eligible'], 'reader_eligible': item['reader']['eligible'],
                        'open_findings': open_ids, 'feedback_closed': not open_ids,
                        'is_revision': index > 1 and raw != previous['raw'],
                        'declared_reader_improvement': item['improvement'],
                        'human_change_percentage_points': None if prior_human is None or human is None else human - prior_human,
                        'improvement_reason': item['improvement_reason']})
        previous = {'id': item['id'], 'text': text, 'raw': raw, 'findings': findings, 'decisions': decisions}
    drafts = checked[1:]
    revisions = [r for r in checked if r['is_revision']]
    used = prior + len(revisions)
    require(used <= limit, 'Revision budget exceeded')
    latest = {r['candidate']['sha256']: r for r in checked}
    pool = []
    for receipt in checked:
        review = latest[receipt['candidate']['sha256']]
        pool.append(receipt | {key: review[key] for key in
                    ('fidelity_eligible', 'reader_eligible', 'open_findings', 'feedback_closed')}
                    | {'eligibility_review_round': review['id']})
    eligible = [r for r in pool if r['fidelity_eligible'] and r['reader_eligible'] and r['feedback_closed']]
    faithful = [r for r in pool if r['fidelity_eligible']]

    def best(pool):
        scored = [r for r in pool if r['human_percent'] is not None]
        return max(scored, key=lambda r: r['human_percent']) if scored else (pool[-1] if pool else None)

    selected, historical = best(eligible), best(faithful)
    stop = session.get('stop', {})
    reason = stop.get('reason', 'in_progress')
    require(reason in ('in_progress', 'complete', 'plateau', 'budget', 'resource'), 'Invalid stop reason')
    require(nonempty(stop.get('detail')), 'Stop/resume detail required')
    last = checked[-1]
    if reason == 'complete':
        require(drafts and any(r['candidate']['sha256'] != digest(original) for r in drafts)
                and selected is not None and last['feedback_closed'] and last['fidelity_eligible']
                and last['reader_eligible'], 'Cannot complete without post-draft feedback closure and eligibility')
    if reason == 'budget':
        require(drafts and used == limit, 'Budget stop does not match revision use')
    if reason == 'plateau':
        require(len(revisions) >= 2 and not any(r['declared_reader_improvement'] for r in revisions[-2:]),
                'Plateau needs two consecutive revisions without defensible improvement')
    return {'schema_version': 1, 'status': reason, 'stop_detail': stop['detail'], 'revision_limit': limit,
            'revisions_used': used, 'prior_revisions_used': prior, 'recorded_text_revisions': len(revisions),
            'prior_revision_note': session.get('prior_revision_note'), 'selected_candidate': selected,
            'selection_basis': ('highest_native_document_human' if selected and selected['human_percent'] is not None
                                else 'latest_eligible_numeric_unavailable' if selected else 'none'),
            'best_faithful_checkpoint': historical, 'rounds': checked,
            'current_open_findings': [{'parent_round': last['id'], 'finding_id': fid} for fid in last['open_findings']],
            'numeric_unavailable_rounds': [r['id'] for r in checked if r['human_percent'] is None],
            'validation_scope': 'Saved records, exact hashes/spans, coverage, native values and followup links; '
                                'not semantic truth, reviewer independence, execution authenticity or authorship.'}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('manifest')
    parser.add_argument('--out', required=True, help='New JSON file inside the manifest workspace')
    parser.add_argument('--require-final', action='store_true')
    args = parser.parse_args(argv)
    try:
        root = Path(args.manifest).resolve().parent
        output = Path(args.out).resolve()
        require(output.is_relative_to(root), 'Output escapes the session workspace')
        require(not output.exists(), 'Refusing to overwrite an existing output')
        try:
            result = validate(args.manifest)
            require(not args.require_final or result['status'] != 'in_progress', 'Session is still in progress')
        except (ValueError, OSError, KeyError, TypeError, AttributeError, OverflowError) as exc:
            result = {'status': 'invalid', 'human_percent': None, 'error': str(exc)}
        with output.open('x', encoding='utf-8', newline='\n') as stream:
            json.dump(result, stream, ensure_ascii=False, indent=2, allow_nan=False)
            stream.write('\n')
        print(json.dumps({'status': result['status'], 'out': str(output)}, ensure_ascii=False))
        return 2 if result['status'] == 'invalid' else 0
    except (ValueError, OSError) as exc:
        print(json.dumps({'status': 'invalid', 'error': str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
