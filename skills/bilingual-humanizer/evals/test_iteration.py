import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/check_detector_report.py'
AUDIT = SCRIPT.with_name('audit_preservation.py')
spec = importlib.util.spec_from_file_location('detector_report', SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class DetectorReportTests(unittest.TestCase):
    def setUp(self):
        self.candidate = '검토한 최종본입니다.\n'.encode('utf-8')
        target = {'id': 'synthetic-a', 'required': True, 'service': 'Synthetic',
                  'model': 'test-only', 'settings': {'language': 'ko'},
                  'metric': 'ai_probability', 'unit': 'fraction', 'operator': 'lte', 'value': 0.1}
        result = {**target, 'target_id': target['id'], 'status': 'ok',
                  'input_sha256': hashlib.sha256(self.candidate).hexdigest(),
                  'scope': 'whole_document', 'eligible': True,
                  'origin': 'user_report', 'evidence': 'synthetic unit-test fixture, not a real scan',
                  'checked_at': '2026-10-02T12:00:00+09:00', 'value': 0.05, 'value_is_exact': True}
        self.bundle = {'schema_version': 1, 'targets': [target], 'results': [result]}

    def check(self):
        return module.evaluate(self.bundle, self.candidate)

    def test_matching_bundle_does_not_certify_authorship(self):
        result = self.check()
        self.assertEqual(result['status'], 'configured_targets_met')
        self.assertFalse(result['authorship_assessed'])
        self.assertFalse(result['receipt_authenticity_verified'])
        self.assertTrue(result['semantic_review_required'])

    def test_old_candidate_score_is_incomplete(self):
        self.candidate += b'changed'
        self.assertEqual(self.check()['status'], 'incomplete')

    def test_any_missing_required_service_prevents_success(self):
        second = {**self.bundle['targets'][0], 'id': 'synthetic-b'}
        self.bundle['targets'].append(second)
        self.assertEqual(self.check()['status'], 'incomplete')

    def test_optional_missing_service_is_visible(self):
        self.bundle['targets'].append({**self.bundle['targets'][0], 'id': 'optional', 'required': False})
        result = self.check()
        self.assertEqual(result['status'], 'configured_targets_met')
        self.assertEqual(result['targets'][1]['status'], 'incomplete')

    def test_failure_is_not_averaged_away(self):
        self.bundle['results'][0]['value'] = 0.9
        self.assertEqual(self.check()['status'], 'targets_unmet')

    def test_unavailable_and_unsupported_are_not_passes(self):
        for status in ('error', 'unsupported', 'pending'):
            with self.subTest(status=status):
                self.bundle['results'][0]['status'] = status
                self.assertEqual(self.check()['status'], 'incomplete')

    def test_setting_metric_scope_and_eligibility_mismatch(self):
        original = copy.deepcopy(self.bundle['results'][0])
        for field, value in [('settings', {'language': 'en'}), ('metric', 'human_probability'),
                             ('unit', 'percent'), ('scope', 'segment'), ('eligible', False),
                             ('model', 'changed')]:
            with self.subTest(field=field):
                self.bundle['results'][0] = {**original, field: value}
                self.assertEqual(self.check()['status'], 'incomplete')

    def test_rounded_zero_not_exact_zero(self):
        self.bundle['targets'][0]['value'] = 0
        self.bundle['results'][0].update(value=0, value_is_exact=False)
        self.assertEqual(self.check()['status'], 'incomplete')

    def test_label_acceptance(self):
        for obj in [self.bundle['targets'][0], self.bundle['results'][0]]:
            obj.update(metric='classification', unit='label', operator='eq', value='Human')
        self.assertEqual(self.check()['status'], 'configured_targets_met')
        self.bundle['results'][0]['value'] = 'Mixed'
        self.assertEqual(self.check()['status'], 'targets_unmet')

    def test_human_percent_direction(self):
        for obj in [self.bundle['targets'][0], self.bundle['results'][0]]:
            obj.update(metric='human_score', unit='percent', operator='gte', value=90)
        self.bundle['results'][0]['value'] = 95
        self.assertEqual(self.check()['status'], 'configured_targets_met')
        self.bundle['results'][0]['value'] = 5
        self.assertEqual(self.check()['status'], 'targets_unmet')

    def test_missing_evidence_and_timezone_block_result(self):
        for field in ('evidence', 'checked_at', 'origin'):
            original = self.bundle['results'][0].pop(field)
            self.assertEqual(self.check()['status'], 'incomplete')
            self.bundle['results'][0][field] = original

    def test_invalid_score_data(self):
        for value in (True, float('nan'), float('inf'), -1, 1.1, '0.01'):
            with self.subTest(value=value):
                self.bundle['results'][0]['value'] = value
                self.assertEqual(self.check()['status'], 'incomplete')

    def test_duplicate_result_and_target_rejected(self):
        self.bundle['results'].append(copy.deepcopy(self.bundle['results'][0]))
        with self.assertRaises(ValueError):
            self.check()
        self.bundle['results'].pop()
        self.bundle['targets'].append(copy.deepcopy(self.bundle['targets'][0]))
        with self.assertRaises(ValueError):
            self.check()

    def test_no_required_target_rejected(self):
        self.bundle['targets'][0]['required'] = False
        with self.assertRaises(ValueError):
            self.check()

    def test_boolean_and_number_settings_are_distinct(self):
        for a, b in [({'exclude_quotes': False}, {'exclude_quotes': 0}),
                     ({'nested': [True]}, {'nested': [1]})]:
            self.bundle['targets'][0]['settings'] = a
            self.bundle['results'][0]['settings'] = b
            self.assertEqual(self.check()['status'], 'incomplete')

    def test_non_string_target_id_is_malformed(self):
        for target_id in ([], {}, True, 1):
            self.bundle['results'][0]['target_id'] = target_id
            with self.assertRaises(ValueError):
                self.check()

    def test_extremely_large_numbers_are_not_finite_floats(self):
        huge = 10 ** 400
        self.bundle['results'][0]['value'] = huge
        self.assertEqual(self.check()['status'], 'incomplete')
        self.bundle['targets'][0]['value'] = huge
        with self.assertRaises(ValueError):
            self.check()

    def test_cli_does_not_overwrite_hardlinked_candidate(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            candidate, report, output = root/'candidate.txt', root/'report.json', root/'alias.txt'
            candidate.write_bytes(self.candidate)
            report.write_text(json.dumps(self.bundle), encoding='utf-8')
            os.link(candidate, output)
            run = subprocess.run([sys.executable, '-B', str(SCRIPT), str(report), str(candidate), '--output', str(output)], capture_output=True)
            self.assertEqual(run.returncode, 2)
            self.assertEqual(candidate.read_bytes(), self.candidate)


class PreservationRegressions(unittest.TestCase):
    def test_leading_dot_decimal_and_sign_changes(self):
        spec = importlib.util.spec_from_file_location('audit_regression', AUDIT)
        audit = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(audit)
        for source, rewrite in [('p=.048', 'p=.084'), ('−.43', '.43'), ('-.43', '.43'),
                                ('.006 ms', '.009 ms'), ('.4e-2', '.5e-2')]:
            with self.subTest(source=source):
                self.assertEqual(audit.audit(source, rewrite)['status'], 'review_required')

    def test_report_cannot_overwrite_hardlinked_inputs(self):
        for target in ('source', 'rewrite', 'protected'):
            with self.subTest(target=target), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                paths = {k: root/(k+'.txt') for k in ('source', 'rewrite', 'protected')}
                paths['source'].write_text('Value 1.', encoding='utf-8')
                paths['rewrite'].write_text('Value 1.', encoding='utf-8')
                paths['protected'].write_text('["Value"]', encoding='utf-8')
                original = {k:p.read_bytes() for k,p in paths.items()}
                output = root/'alias.txt'
                os.link(paths[target], output)
                run = subprocess.run([sys.executable, '-B', str(AUDIT), str(paths['source']), str(paths['rewrite']),
                                      '--protect-json', str(paths['protected']), '--output', str(output)], capture_output=True)
                self.assertEqual(run.returncode, 2)
                self.assertEqual({k:p.read_bytes() for k,p in paths.items()}, original)


if __name__ == '__main__':
    unittest.main()
