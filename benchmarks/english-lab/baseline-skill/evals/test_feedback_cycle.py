"""Synthetic saved-record tests only: no model execution, API calls, or manuscript edits."""
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import feedback_cycle as cycle
from test_local_feedback import adapter, english_result, korean_result


class CycleTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.source = 'The original source preserves the notice duty.'
        self.manifest = {'schema_version': 1, 'language': 'ko',
                         'source': self.store('source.txt', self.source), 'revision_limit': 3,
                         'rounds': [], 'stop': {'reason': 'in_progress', 'detail': 'Review next candidate.'}}

    def store(self, name, value):
        raw = value.encode('utf-8') if isinstance(value, str) else json.dumps(value).encode('utf-8')
        (self.root / name).write_bytes(raw)
        return {'path': name, 'sha256': adapter.digest(raw)}

    def change_artifact(self, item, key, transform):
        path = self.root / item[key]['path']
        value = json.loads(path.read_bytes())
        transform(value)
        item[key] = self.store(path.name, value)

    def add_round(self, text=None, findings=(), human=.2, language='ko', unavailable=False,
                  faithful=True, reader=True, improvement=True, multi=False):
        index = len(self.manifest['rounds'])
        rid, text = f'r{index}', self.source if text is None else text
        raw = text.encode('utf-8')
        ps = cycle.paragraphs(text)
        entries = [{'id': fid, 'basis': 'style_observation', 'direction': 'ai_like', 'strength': 'weak',
                    'observation': 'Synthetic observation.', 'interpretation': 'Synthetic reader problem.',
                    'human_alternative': 'A person could write this.', 'discriminating_evidence': 'Review the context.',
                    'spans': [{'start': 0, 'end': len(text), 'quote': text}]} for fid in findings]
        report = {'schema_version': 2, 'mode': 'anchored_explanation', 'text_sha256': adapter.digest(raw),
                  'authorship_probabilities': None,
                  'summary': 'Synthetic full-document review.', 'document_analysis': {d: 'Reviewed.' for d in cycle.DIMENSIONS},
                  'findings': entries, 'paragraph_reviews': [
                      {'paragraph_id': pid, 'start': start, 'end': end, 'text': text[start:end],
                       'status': 'reviewed', 'assessment': 'Reviewed in context.', 'finding_ids': list(findings)}
                      for pid, start, end in ps],
                  'coverage': {'paragraphs_total': len(ps), 'paragraphs_reviewed': len(ps),
                               'paragraphs_excluded': 0, 'review_fraction': 1}}
        native_ref = None
        if unavailable:
            feedback = {'status': 'error', 'input_sha256': adapter.digest(raw), 'human_percent': None,
                        'native_class_probabilities': None, 'error': 'Synthetic runtime failure.'}
        else:
            native = korean_result(raw) if language == 'ko' else english_result(raw, multi=multi)
            if language == 'ko':
                native['class_probabilities'] = {'human': human, 'ai': 1 - human}
            native_ref = self.store(rid + '-native.json', native)
            feedback = adapter.normalize(native, raw, language)
            feedback['raw_result_sha256'] = native_ref['sha256']
        item = {'id': rid, 'candidate': self.store(rid + '.txt', text), 'native': native_ref,
                'feedback': self.store(rid + '-feedback.json', feedback),
                'review': self.store(rid + '-review.json', report),
                'fidelity': {'eligible': faithful, 'reason': 'Synthetic source comparison.',
                             'source_sha256': self.manifest['source']['sha256']},
                'reader': {'eligible': reader, 'reason': 'Synthetic reader review.'},
                'triage': [{'finding_id': fid, 'decision': 'revise', 'reason': 'Concrete synthetic issue.'} for fid in findings],
                'followup': [], 'improvement': improvement, 'improvement_reason': 'Synthetic editorial assessment.'}
        self.manifest['rounds'].append(item)
        return item

    def edge(self, child, parent, fid, status='resolved', links=()):
        before = (self.root / parent['candidate']['path']).read_bytes().decode('utf-8')
        after = (self.root / child['candidate']['path']).read_bytes().decode('utf-8')
        child['followup'].append({'parent_round': parent['id'], 'finding_id': fid, 'status': status,
                                 'reason': 'Followup whole-document review checked this change.',
                                 'before': {'start': 0, 'end': len(before), 'quote': before},
                                 'after': {'start': 0, 'end': len(after), 'quote': after}, 'finding_ids': list(links)})

    def run_record(self, stop=None):
        if stop:
            self.manifest['stop'] = {'reason': stop, 'detail': 'Explicit synthetic stopping reason.'}
        self.store('session.json', self.manifest)
        return cycle.validate(self.root / 'session.json')

    def test_new_postscore_feedback_requires_another_rewrite_and_review(self):
        r0 = self.add_round(findings=['F1'])
        r1 = self.add_round('The first draft still has a new reader issue.', ['F2'], human=.9)
        self.edge(r1, r0, 'F1')
        with self.assertRaisesRegex(ValueError, 'post-draft feedback closure'):
            self.run_record('complete')
        self.assertEqual(self.run_record('in_progress')['rounds'][-1]['open_findings'], ['F2'])
        r2 = self.add_round('The second draft preserves and clarifies the notice duty.', human=.7)
        self.edge(r2, r1, 'F2')
        result = self.run_record('complete')
        self.assertEqual(result['selected_candidate']['id'], 'r2')
        self.assertEqual(result['best_faithful_checkpoint']['id'], 'r1')
        self.assertEqual(result['best_faithful_checkpoint']['open_findings'], ['F2'])

    def test_stale_candidate_hash_rejected(self):
        r0 = self.add_round()
        (self.root / r0['candidate']['path']).write_text('Changed text', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'Stale artifact hash'):
            self.run_record()

    def test_missing_or_invented_finding_rejected(self):
        r0 = self.add_round(findings=['F1'])
        r0['triage'][0]['finding_id'] = 'invented'
        with self.assertRaisesRegex(ValueError, 'Unknown.*triage'):
            self.run_record()
        r0['triage'] = []
        with self.assertRaisesRegex(ValueError, 'vanished from triage'):
            self.run_record()

    def test_open_findings_cannot_vanish_or_close_as_applied(self):
        r0 = self.add_round(findings=['F1'])
        r1 = self.add_round('A revised complete draft.')
        with self.assertRaisesRegex(ValueError, 'vanished without followup'):
            self.run_record()
        self.edge(r1, r0, 'F1')
        r1['followup'][0]['status'] = 'applied'
        with self.assertRaisesRegex(ValueError, 'reviewed outcome'):
            self.run_record()

    def test_carry_must_point_to_current_actionable_finding(self):
        r0 = self.add_round(findings=['F1'])
        r1 = self.add_round('Revised draft still has the problem.', ['F2'])
        self.edge(r1, r0, 'F1', 'carried', ['F2'])
        self.assertEqual(self.run_record()['rounds'][-1]['open_findings'], ['F2'])
        r1['triage'][0]['decision'] = 'retain'
        with self.assertRaisesRegex(ValueError, 'must remain actionable'):
            self.run_record()

    def test_unchanged_accepted_revision_cannot_be_called_resolved(self):
        r0 = self.add_round(findings=['F1'])
        r1 = self.add_round()
        self.edge(r1, r0, 'F1')
        with self.assertRaisesRegex(ValueError, 'changed exact passage'):
            self.run_record()

    def test_identical_candidate_cannot_close_revision_by_narrowing_quote(self):
        self.add_round()
        text = 'A first draft still needs a repair.'
        r1 = self.add_round(text, ['F1'])
        r2 = self.add_round(text)
        self.edge(r2, r1, 'F1')
        r2['followup'][0]['after'] = {'start': 0, 'end': len(text) - 1, 'quote': text[:-1]}
        with self.assertRaisesRegex(ValueError, 'changed exact passage'):
            self.run_record('complete')

    def test_carried_after_span_must_overlap_every_linked_finding(self):
        self.add_round()
        text = 'First sentence. Unrelated second sentence.'
        r1 = self.add_round(text, ['F1'])
        r2 = self.add_round(text, ['F2'])
        start = text.index('Unrelated')
        self.change_artifact(r2, 'review', lambda r: r['findings'][0].update(
            spans=[{'start': start, 'end': len(text), 'quote': text[start:]}]))
        self.edge(r2, r1, 'F1', 'carried', ['F2'])
        r2['followup'][0]['after'] = {'start': 0, 'end': start - 1, 'quote': text[:start - 1]}
        with self.assertRaisesRegex(ValueError, 'misses a linked'):
            self.run_record()

    def test_review_cannot_assert_authorship_probabilities(self):
        r0 = self.add_round()
        self.change_artifact(r0, 'review', lambda r: r.update(authorship_probabilities={'human': 1}))
        with self.assertRaisesRegex(ValueError, 'explicitly null'):
            self.run_record()
        self.change_artifact(r0, 'review', lambda r: r.pop('authorship_probabilities'))
        with self.assertRaisesRegex(ValueError, 'explicitly null'):
            self.run_record()

    def test_partial_review_and_missing_review_rejected(self):
        r0 = self.add_round()
        self.change_artifact(r0, 'review', lambda r: r['paragraph_reviews'][0].update(status='not_reviewed'))
        with self.assertRaisesRegex(ValueError, 'paragraph review'):
            self.run_record()
        del r0['review']
        with self.assertRaisesRegex(ValueError, 'artifact reference'):
            self.run_record()

    def test_semantically_wrong_high_score_never_selected(self):
        self.add_round()
        self.add_round('Draft deletes a protected notice duty.', human=.99, faithful=False)
        self.add_round('Draft restores the protected notice duty.', human=.7)
        result = self.run_record('complete')
        self.assertEqual(result['selected_candidate']['id'], 'r2')
        self.assertEqual(result['best_faithful_checkpoint']['id'], 'r2')

    def test_score_regression_can_recover_closed_source(self):
        self.add_round(human=.8)
        self.add_round('Faithful draft with lower native score.', human=.4)
        self.assertEqual(self.run_record('complete')['selected_candidate']['id'], 'r0')

    def test_later_same_hash_finding_invalidates_earlier_closed_eligibility(self):
        self.add_round()
        text = 'High scoring draft later found to need repair.'
        self.add_round(text, human=.9)
        r2 = self.add_round(text, ['F1'], human=.8)
        r3 = self.add_round('Lower scoring draft repairs the actual issue.', human=.7)
        self.edge(r3, r2, 'F1')
        result = self.run_record('complete')
        self.assertEqual(result['selected_candidate']['id'], 'r3')
        checkpoint = result['best_faithful_checkpoint']
        self.assertEqual(checkpoint['id'], 'r1')
        self.assertEqual(checkpoint['human_percent'], 90)
        self.assertEqual(checkpoint['eligibility_review_round'], 'r2')
        self.assertEqual(checkpoint['open_findings'], ['F1'])
        self.assertTrue(result['rounds'][1]['feedback_closed'])  # Historical observation is preserved.

    def test_later_same_hash_fidelity_failure_invalidates_both_selection_pools(self):
        self.add_round()
        text = 'High scoring draft later found to have meaning loss.'
        self.add_round(text, human=.99)
        self.add_round(text, human=.99, faithful=False)
        self.add_round('Faithful repaired candidate.', human=.7)
        result = self.run_record('complete')
        self.assertEqual(result['selected_candidate']['id'], 'r3')
        self.assertEqual(result['best_faithful_checkpoint']['id'], 'r3')

    def test_later_same_hash_reader_failure_invalidates_delivery_only(self):
        self.add_round()
        text = 'Faithful draft later found to fail reader review.'
        self.add_round(text, human=.9)
        self.add_round(text, human=.8, reader=False)
        self.add_round('Reader-eligible repaired candidate.', human=.7)
        result = self.run_record('complete')
        self.assertEqual(result['selected_candidate']['id'], 'r3')
        checkpoint = result['best_faithful_checkpoint']
        self.assertEqual(checkpoint['id'], 'r1')
        self.assertFalse(checkpoint['reader_eligible'])
        self.assertEqual(checkpoint['eligibility_review_round'], 'r2')

    def test_unscored_rejected_revision_uses_budget_and_recovers_closed_candidate(self):
        self.manifest.update(prior_revisions_used=1, prior_revision_note='Documented earlier fidelity repair.')
        self.add_round()
        self.add_round('Initial faithful draft.', human=.3)
        self.add_round('Faithful reviewed revision.', human=.7)
        self.add_round('Rejected revision weakens a protected assertion.', faithful=False, reader=False, unavailable=True)
        result = self.run_record('budget')
        self.assertEqual(result['revisions_used'], 3)
        self.assertEqual(result['selected_candidate']['id'], 'r2')
        self.assertEqual(result['numeric_unavailable_rounds'], ['r3'])
        self.assertFalse(result['rounds'][-1]['fidelity_eligible'])

    def test_error_scores_stay_null_without_fallback(self):
        self.add_round(unavailable=True)
        r1 = self.add_round('A reviewed draft with no numerical score.', unavailable=True)
        result = self.run_record('complete')
        self.assertIsNone(result['selected_candidate']['human_percent'])
        self.assertEqual(result['numeric_unavailable_rounds'], ['r0', 'r1'])
        self.change_artifact(r1, 'feedback', lambda f: f.update(human_percent=100))
        with self.assertRaisesRegex(ValueError, 'remain null'):
            self.run_record()

    def test_english_four_classes_and_multiwindow_null_preserved(self):
        self.manifest['language'] = 'en'
        r0 = self.add_round(language='en')
        self.add_round('Different English candidate.', language='en', multi=True)
        result = self.run_record('complete')
        self.assertEqual(result['rounds'][0]['human_percent'], 5)
        self.assertEqual(set(result['rounds'][0]['native_class_probabilities']), {'human', 'ai', 'ai_edited', 'humanized'})
        self.assertIsNone(result['rounds'][1]['human_percent'])
        self.change_artifact(r0, 'feedback', lambda f: f.update(human_percent=85))
        with self.assertRaisesRegex(ValueError, 'differs from native'):
            self.run_record()

    def test_stale_attached_model_identity_rejected(self):
        r0 = self.add_round()
        self.change_artifact(r0, 'review', lambda r: r.update(measured_output={
            'class_probabilities': {'human': .2, 'ai': .8}, 'model': 'wrong-model'}))
        with self.assertRaisesRegex(ValueError, 'inconsistent numbers'):
            self.run_record()

    def test_source_only_or_unchanged_duplicate_is_not_complete(self):
        self.add_round()
        with self.assertRaisesRegex(ValueError, 'post-draft'):
            self.run_record('complete')
        self.add_round()
        with self.assertRaisesRegex(ValueError, 'post-draft'):
            self.run_record('complete')

    def test_budget_counts_initial_draft_separately(self):
        self.add_round()
        for i in range(4):
            self.add_round(f'Draft {i} retains all meaning.')
        result = self.run_record('budget')
        self.assertEqual(result['revisions_used'], 3)
        self.assertEqual(result['status'], 'budget')
        self.add_round('A forbidden fourth revision.')
        with self.assertRaisesRegex(ValueError, 'budget exceeded'):
            self.run_record()
        self.manifest['revision_limit'] = 4
        with self.assertRaisesRegex(ValueError, 'explicit user instruction'):
            self.run_record()

    def test_plateau_is_disclosed_not_complete(self):
        self.add_round()
        self.add_round('Initial draft.')
        self.add_round('First alternative.', improvement=False)
        self.add_round('Second alternative.', improvement=False)
        self.assertEqual(self.run_record('plateau')['status'], 'plateau')

    def test_unchanged_review_rounds_do_not_consume_budget_or_trigger_plateau(self):
        self.add_round()
        for _ in range(4):
            self.add_round('The same frozen draft.', improvement=False)
        self.assertEqual(self.run_record()['revisions_used'], 0)
        with self.assertRaisesRegex(ValueError, 'Budget stop does not match'):
            self.run_record('budget')
        with self.assertRaisesRegex(ValueError, 'two consecutive revisions'):
            self.run_record('plateau')

    def test_prior_repairs_use_budget_but_not_plateau_evidence(self):
        self.manifest['prior_revisions_used'] = 1
        self.add_round()
        self.add_round('Already repaired frozen initial draft.')
        with self.assertRaisesRegex(ValueError, 'provenance note'):
            self.run_record()
        self.manifest['prior_revision_note'] = 'Writer disclosed one pre-freeze fidelity repair.'
        self.add_round('One new revision.', improvement=False)
        self.assertEqual(self.run_record()['revisions_used'], 2)
        with self.assertRaisesRegex(ValueError, 'two consecutive revisions'):
            self.run_record('plateau')
        self.add_round('Second new revision.', improvement=False)
        self.assertEqual(self.run_record('budget')['revisions_used'], 3)
        self.add_round('Would exceed the existing ceiling.')
        with self.assertRaisesRegex(ValueError, 'budget exceeded'):
            self.run_record()

    def test_fidelity_source_binding_and_fresh_reviews_required(self):
        r0 = self.add_round()
        r1 = self.add_round('A new draft.')
        r1['fidelity']['source_sha256'] = '0' * 64
        with self.assertRaisesRegex(ValueError, 'different source'):
            self.run_record()
        r1['fidelity']['source_sha256'] = self.manifest['source']['sha256']
        r1['review'] = copy.deepcopy(r0['review'])
        with self.assertRaisesRegex(ValueError, 'fresh feedback/review'):
            self.run_record()

    def test_cli_handles_malformed_input_and_require_final(self):
        self.store('broken.json', '{broken')
        self.assertEqual(cycle.main([str(self.root / 'broken.json'), '--out', str(self.root / 'broken-status.json')]), 2)
        self.add_round()
        self.run_record()
        self.assertEqual(cycle.main([str(self.root / 'session.json'), '--out', str(self.root / 'status.json'), '--require-final']), 2)
        self.assertEqual(json.loads((self.root / 'status.json').read_text())['status'], 'invalid')


if __name__ == '__main__':
    unittest.main()
