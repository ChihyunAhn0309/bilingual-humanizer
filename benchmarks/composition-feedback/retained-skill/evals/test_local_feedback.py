"""Offline adapter contract tests; English fixtures are synthetic, never model runs."""
import copy
from datetime import datetime, timedelta, timezone
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/local_feedback.py'
spec = importlib.util.spec_from_file_location('local_feedback', SCRIPT)
adapter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(adapter)
DEVELOPMENT = SCRIPT.parents[2] / 'development'
DETECTOR = Path(os.environ.get('CODEX_HOME', str(Path.home() / '.codex'))) / 'skills/bilingual-ai-detector'
RAW = '\ufeff첫 번째 문단은 원문의 줄바꿈과 한글 표현을 그대로 보존한다.\r\n\r\n둘째 문단에는 e\u0301와 é, 이모지 🧪가 함께 있다.\r\n'.encode('utf-8')


def korean_result(raw=RAW):
    return {'mode': 'offline_korean_calibrated_classifier', 'model_id': adapter.KO_MODEL,
            'model_sha256': adapter.KO_HASH, 'text_sha256': adapter.digest(raw),
            'measured_at_utc': datetime.now(timezone.utc).isoformat(),
            'characters_codepoints': len(raw.decode('utf-8')), 'all_input_scored': True,
            'class_probabilities': {'human': .2, 'ai': .8},
            'probability_semantics': 'Synthetic fixture of native two-class calibration semantics.',
            'calibration': {'method': 'held_out_regularized_sigmoid'},
            'applicability_cautions': ['Synthetic short-text caution.'],
            'known_limits': ['Synthetic population-shift limitation.'],
            'feature_explanation': {'lexical': []}, 'paragraph_sensitivity': {},
            'external_detector_calls': 0, 'authorship_verified': False}


def english_result(raw=RAW, multi=False):
    # Synthetic class outputs explicitly distinguish Human from edited/humanized.
    classes = {'human': .05, 'ai': .15, 'ai_edited': .3, 'humanized': .5}
    window = {'token_start': 0, 'token_end': 20, 'start': 0,
              'end': len(raw.decode('utf-8')), 'quote': raw.decode('utf-8'),
              'class_probabilities': classes, 'ai_involvement_class_score': .95}
    windows = [window]
    if multi:
        windows.append(dict(copy.deepcopy(window), token_start=10, token_end=30))
    return {'schema_version': 2, 'mode': 'offline_local_model', 'model': adapter.EN_MODEL,
            'revision': adapter.EN_REVISION, 'weight_sha256': adapter.EN_HASH,
            'text_sha256': adapter.digest(raw), 'measured_at_utc': datetime.now(timezone.utc).isoformat(),
            'all_input_tokens_scored': True, 'token_count': 30 if multi else 20,
            'windows': windows, 'document_class_probabilities': None if multi else copy.deepcopy(classes),
            'independently_calibrated_here': False,
            'validation_status': 'experimental_auxiliary_score_not_a_validated_authorship_detector',
            'known_limitations': 'Synthetic fixture: experimental auxiliary model; false positives occur.',
            'occlusion': {'performed': False, 'paragraphs': []},
            'execution_guard': {'worker_exit_code': 0, 'serialized_cli': True,
                                'native_runtime_stability_guaranteed': False},
            'external_detector_calls': 0, 'authorship_verified': False}


class NormalizeTests(unittest.TestCase):
    def test_korean_keeps_native_values_cautions_and_review_state(self):
        native = korean_result()
        result = adapter.normalize(native, RAW, 'ko')
        self.assertEqual(result['human_percent'], 20)
        self.assertEqual(result['native_class_probabilities'], native['class_probabilities'])
        self.assertEqual(result['cautions'], native['applicability_cautions'] + native['known_limits'])
        self.assertEqual(result['calibration'], native['calibration'])
        self.assertEqual(result['measured_evidence']['paragraph_sensitivity'], native['paragraph_sensitivity'])
        self.assertFalse(result['style_review_completed'])
        self.assertFalse(result['authorship_verified'])
        self.assertTrue(result['semantic_review_required'])

    def test_real_saved_korean_contract(self):
        result_path, source = DEVELOPMENT / 'ko-baseline.json', DEVELOPMENT / 'ko-original.txt'
        if not result_path.is_file() or not source.is_file():
            self.skipTest('Optional local development baseline is not packaged')
        native = json.loads(result_path.read_text('utf-8'))
        result = adapter.normalize(native, source.read_bytes(), 'ko')
        self.assertEqual(result['human_percent'], native['class_probabilities']['human'] * 100)
        self.assertEqual(result['measured_evidence']['lexical'], native['feature_explanation']['lexical'])

    def test_wrong_input_hash_rejected(self):
        for language, fixture in [('ko', korean_result), ('en', english_result)]:
            with self.subTest(language=language):
                result = fixture()
                result['text_sha256'] = '0' * 64
                with self.assertRaisesRegex(ValueError, 'different input'):
                    adapter.normalize(result, RAW, language)

    def test_wrong_or_nonhex_model_hash_rejected(self):
        for field, fixture, language in [('model_sha256', korean_result, 'ko'), ('weight_sha256', english_result, 'en')]:
            for bad in ['0' * 64, 'z' * 64, '', None]:
                with self.subTest(language=language, bad=bad):
                    result = fixture()
                    result[field] = bad
                    with self.assertRaises(ValueError):
                        adapter.normalize(result, RAW, language)

    def test_invalid_native_classes_rejected(self):
        for bad in [None, {}, {'human': .5, 'mixed': .5}, {'human': .2, 'ai': .7},
                    {'human': True, 'ai': 0}, {'human': -.1, 'ai': 1.1},
                    {'human': 10 ** 1000, 'ai': 0},
                    {'human': float('nan'), 'ai': 1}, {'human': float('inf'), 'ai': 0},
                    {'human': '0.2', 'ai': .8}]:
            with self.subTest(bad=bad):
                result = korean_result()
                result['class_probabilities'] = bad
                with self.assertRaises(ValueError):
                    adapter.normalize(result, RAW, 'ko')

    def test_english_edited_and_humanized_are_not_human(self):
        native = english_result()
        result = adapter.normalize(native, RAW, 'en')
        self.assertEqual(result['human_percent'], 5)
        self.assertEqual(result['native_class_probabilities'], native['document_class_probabilities'])
        self.assertEqual(set(result['native_class_probabilities']), {'human', 'ai', 'ai_edited', 'humanized'})
        self.assertIsNone(result['calibration'])

    def test_english_multiwindow_document_probability_stays_null(self):
        native = english_result(multi=True)
        result = adapter.normalize(native, RAW, 'en')
        self.assertIsNone(result['human_percent'])
        self.assertIsNone(result['native_class_probabilities'])
        self.assertEqual(result['scope'], 'windows_only')
        self.assertEqual(result['measured_evidence']['windows'], native['windows'])

    def test_multiwindow_nonnull_or_missing_document_probability_rejected(self):
        for missing in [False, True]:
            with self.subTest(missing=missing):
                result = english_result(multi=True)
                if missing:
                    del result['document_class_probabilities']
                else:
                    result['document_class_probabilities'] = result['windows'][0]['class_probabilities']
                with self.assertRaises(ValueError):
                    adapter.normalize(result, RAW, 'en')

    def test_single_window_document_mismatch_rejected(self):
        result = english_result()
        result['document_class_probabilities']['human'] = .15
        result['document_class_probabilities']['ai'] = .05
        with self.assertRaisesRegex(ValueError, 'scores differ'):
            adapter.normalize(result, RAW, 'en')

    def test_invalid_english_windows_rejected(self):
        for bad in [None, [], [None], [{'class_probabilities': {'human': 1}}]]:
            with self.subTest(bad=bad):
                result = english_result()
                result['windows'] = bad
                with self.assertRaises(ValueError):
                    adapter.normalize(result, RAW, 'en')

    def test_english_missing_native_class_rejected(self):
        result = english_result()
        del result['windows'][0]['class_probabilities']['humanized']
        with self.assertRaises(ValueError):
            adapter.normalize(result, RAW, 'en')

    def test_claimed_english_coverage_with_gap_rejected(self):
        result = english_result(multi=True)
        result['windows'][1]['token_start'] = 21
        with self.assertRaisesRegex(ValueError, 'token coverage'):
            adapter.normalize(result, RAW, 'en')

    def test_claimed_english_coverage_with_missing_tail_rejected(self):
        result = english_result()
        result['token_count'] = 21
        with self.assertRaises(ValueError):
            adapter.normalize(result, RAW, 'en')

    def test_error_or_nonobject_never_normalizes_to_success(self):
        for bad in [None, [], 1, 'text', dict(korean_result(), error='failed'),
                    dict(korean_result(), status='error')]:
            with self.subTest(bad=type(bad)):
                with self.assertRaises(ValueError):
                    adapter.normalize(bad, RAW, 'ko')

    def test_noninteger_offline_metadata_rejected(self):
        for bad in [False, 0.0, '0', 1, None]:
            with self.subTest(bad=bad):
                result = korean_result()
                result['external_detector_calls'] = bad
                with self.assertRaises(ValueError):
                    adapter.normalize(result, RAW, 'ko')

    def test_unsupported_success_metadata_rejected(self):
        cases = [('schema_version', True), ('schema_version', 3), ('revision', 'unknown'),
                 ('validation_status', 'validated_authorship'), ('independently_calibrated_here', True),
                 ('authorship_verified', True), ('all_input_tokens_scored', False), ('model', 'other')]
        for field, bad in cases:
            with self.subTest(field=field):
                result = english_result()
                result[field] = bad
                with self.assertRaises(ValueError):
                    adapter.normalize(result, RAW, 'en')

    def test_english_unsupervised_or_failed_guard_rejected(self):
        for guard in [None, {}, {'worker_exit_code': 1, 'serialized_cli': True,
                                'native_runtime_stability_guaranteed': False},
                      {'worker_exit_code': False, 'serialized_cli': True,
                       'native_runtime_stability_guaranteed': False}]:
            with self.subTest(guard=guard):
                result = english_result()
                result['execution_guard'] = guard
                with self.assertRaises(ValueError):
                    adapter.normalize(result, RAW, 'en')

    def test_missing_cautions_calibration_or_evidence_rejected(self):
        for field in ['applicability_cautions', 'known_limits', 'calibration', 'feature_explanation',
                      'paragraph_sensitivity', 'probability_semantics']:
            with self.subTest(field=field):
                result = korean_result()
                del result[field]
                with self.assertRaises(ValueError):
                    adapter.normalize(result, RAW, 'ko')

    def test_invalid_measurement_time_rejected(self):
        for timestamp in [None, '', 'yesterday', '2026-10-03T00:00:00', '2026-10-03T00:00:00+09:00']:
            with self.subTest(timestamp=timestamp):
                result = korean_result()
                result['measured_at_utc'] = timestamp
                with self.assertRaises(ValueError):
                    adapter.normalize(result, RAW, 'ko')

    def test_unsupported_language_rejected(self):
        with self.assertRaisesRegex(ValueError, 'Unsupported language'):
            adapter.normalize(english_result(), RAW, 'fr')


class RunTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.source, self.output = self.root / 'candidate.txt', self.root / 'new-run'
        self.source.write_bytes(RAW)
        self.detector = self.root / 'detector'
        (self.detector / 'scripts').mkdir(parents=True)
        for name in ['evidence.py', 'korean_model.py', 'run_english.py']:
            (self.detector / 'scripts' / name).write_text('# Synthetic fixture only.\n', encoding='utf-8')

    def invoke(self, fake, language='ko'):
        with patch.object(adapter.subprocess, 'run', side_effect=fake) as mocked:
            result = adapter.run(self.source, self.detector, language, 'unknown', self.output)
        return result, mocked

    def fake_success(self, command, **kwargs):
        self.assertEqual(kwargs['env']['HF_HUB_OFFLINE'], '1')
        self.assertEqual(kwargs['env']['TRANSFORMERS_OFFLINE'], '1')
        destination = Path(command[command.index('--out') + 1])
        self.assertEqual((self.output / 'input.txt').read_bytes(), RAW)
        if 'index' in command:
            value = {'text_sha256': adapter.digest(RAW), 'paragraphs': [{'id': 'P1'}, {'id': 'P2'}]}
        elif 'run_english.py' == Path(command[4]).name:
            self.assertIn('--explain', command)
            value = english_result()
        else:
            value = korean_result()
        destination.write_text(json.dumps(value, ensure_ascii=False), encoding='utf-8')
        return subprocess.CompletedProcess(command, 0, 'fixture stdout', '')

    def check_failure_receipts(self):
        feedback = json.loads((self.output / 'feedback.json').read_text('utf-8'))
        execution = json.loads((self.output / 'execution.json').read_text('utf-8'))
        self.assertEqual(feedback['status'], 'error')
        self.assertIsNone(feedback['human_percent'])
        self.assertIsNone(feedback['native_class_probabilities'])
        self.assertFalse(feedback['authorship_verified'])
        self.assertEqual(execution['status'], 'error')
        return execution

    def test_exact_bom_crlf_unicode_bytes_and_receipts_preserved(self):
        result, mocked = self.invoke(self.fake_success)
        self.assertEqual(mocked.call_count, 2)
        self.assertEqual(self.source.read_bytes(), RAW)
        self.assertEqual((self.output / 'input.txt').read_bytes(), RAW)
        self.assertTrue(RAW.startswith(b'\xef\xbb\xbf'))
        self.assertIn(b'\r\n', RAW)
        self.assertEqual(result['input_sha256'], adapter.digest(RAW))
        self.assertEqual(result['raw_result_sha256'], adapter.digest((self.output / 'model-result.json').read_bytes()))
        self.assertEqual(result['paragraph_review_required'], ['P1', 'P2'])
        receipt = json.loads((self.output / 'execution.json').read_text('utf-8'))
        self.assertEqual(receipt['status'], 'completed')
        self.assertEqual([call['returncode'] for call in receipt['calls']], [0, 0])

    def test_english_uses_supervised_entry_point(self):
        result, mocked = self.invoke(self.fake_success, 'en')
        self.assertEqual(Path(mocked.call_args_list[-1].args[0][4]).name, 'run_english.py')
        self.assertEqual(result['human_percent'], 5)

    def test_existing_directory_refused_without_altering_stale_files(self):
        self.output.mkdir()
        stale = self.output / 'feedback.json'
        stale.write_bytes(b'old receipt')
        with patch.object(adapter.subprocess, 'run') as mocked:
            with self.assertRaises(FileExistsError):
                adapter.run(self.source, self.detector, 'ko', 'unknown', self.output)
        mocked.assert_not_called()
        self.assertEqual(stale.read_bytes(), b'old receipt')
        self.assertEqual(list(self.output.iterdir()), [stale])

    def test_failed_score_with_valid_looking_file_never_reuses_it(self):
        def fail(command, **kwargs):
            success = self.fake_success(command, **kwargs)
            return success if 'index' in command else subprocess.CompletedProcess(command, 3221225477, '', 'native crash')
        with self.assertRaisesRegex(ValueError, 'no usable score'):
            self.invoke(fail)
        execution = self.check_failure_receipts()
        self.assertEqual(execution['calls'][-1]['returncode'], 3221225477)
        self.assertEqual(execution['calls'][-1]['stderr'], 'native crash')

    def test_failed_index_does_not_launch_model(self):
        def fail(command, **kwargs):
            return subprocess.CompletedProcess(command, 2, '', 'index failed')
        with self.assertRaises(ValueError):
            self.invoke(fail)
        execution = self.check_failure_receipts()
        self.assertEqual(len(execution['calls']), 1)
        self.assertEqual(execution['calls'][0]['stage'], 'index')

    def test_missing_result_after_zero_exit_is_error(self):
        def missing(command, **kwargs):
            if 'index' in command:
                return self.fake_success(command, **kwargs)
            return subprocess.CompletedProcess(command, 0, '', '')
        with self.assertRaisesRegex(ValueError, 'returned no result'):
            self.invoke(missing)
        self.check_failure_receipts()

    def test_spawn_failure_recorded(self):
        with self.assertRaises(OSError):
            self.invoke(lambda *args, **kwargs: (_ for _ in ()).throw(OSError('cannot start worker')))
        execution = self.check_failure_receipts()
        self.assertIsNone(execution['calls'][0]['returncode'])
        self.assertIn('cannot start worker', execution['calls'][0]['error'])

    def test_nonobject_and_invalid_json_produce_error_receipts(self):
        for malformed in ['[]', '{broken json']:
            with self.subTest(malformed=malformed):
                self.output = self.root / ('malformed-' + str(len(malformed)))
                def fake(command, **kwargs):
                    done = self.fake_success(command, **kwargs)
                    if 'index' not in command:
                        (self.output / 'model-result.json').write_text(malformed, encoding='utf-8')
                    return done
                with self.assertRaises(ValueError):
                    self.invoke(fake)
                self.check_failure_receipts()

    def test_wrong_index_hash_produces_error_receipt(self):
        def fake(command, **kwargs):
            done = self.fake_success(command, **kwargs)
            if 'index' in command:
                (self.output / 'index.json').write_text(json.dumps({'text_sha256': '0' * 64, 'paragraphs': []}), encoding='utf-8')
            return done
        with self.assertRaisesRegex(ValueError, 'different input hash'):
            self.invoke(fake)
        self.check_failure_receipts()

    def test_input_mutation_rejects_completed_model_result(self):
        for target in ['source', 'snapshot']:
            with self.subTest(target=target):
                self.output = self.root / target
                self.source.write_bytes(RAW)
                def fake(command, **kwargs):
                    done = self.fake_success(command, **kwargs)
                    if 'index' not in command:
                        path = self.source if target == 'source' else self.output / 'input.txt'
                        path.write_bytes(RAW + b'changed')
                    return done
                with self.assertRaisesRegex(ValueError, 'Input changed'):
                    self.invoke(fake)
                self.check_failure_receipts()

    def test_stale_same_input_result_rejected(self):
        def stale(command, **kwargs):
            done = self.fake_success(command, **kwargs)
            if 'index' not in command:
                result = korean_result()
                result['measured_at_utc'] = (datetime.now(timezone.utc) - timedelta(days=1)).isoformat()
                (self.output / 'model-result.json').write_text(json.dumps(result), encoding='utf-8')
            return done
        with self.assertRaisesRegex(ValueError, 'outside this scoring invocation'):
            self.invoke(stale)
        self.check_failure_receipts()

    def test_precreated_score_file_refused_before_model_launch(self):
        def stale(command, **kwargs):
            done = self.fake_success(command, **kwargs)
            (self.output / 'model-result.json').write_text(json.dumps(korean_result()), encoding='utf-8')
            return done
        with self.assertRaisesRegex(ValueError, 'existing subprocess result'):
            self.invoke(stale)
        execution = self.check_failure_receipts()
        self.assertEqual(len(execution['calls']), 1)

    def test_unavailable_detector_script_produces_error_receipt(self):
        (self.detector / 'scripts' / 'evidence.py').unlink()
        with self.assertRaisesRegex(ValueError, 'script unavailable'):
            self.invoke(self.fake_success)
        self.check_failure_receipts()

    def test_empty_review_index_rejected(self):
        def fake(command, **kwargs):
            done = self.fake_success(command, **kwargs)
            if 'index' in command:
                (self.output / 'index.json').write_text(json.dumps({'text_sha256': adapter.digest(RAW), 'paragraphs': []}), encoding='utf-8')
            return done
        with self.assertRaisesRegex(ValueError, 'paragraph review coverage'):
            self.invoke(fake)
        self.check_failure_receipts()

    def test_invalid_utf8_rejected_before_any_subprocess(self):
        self.source.write_bytes(b'\xff\xfe')
        with patch.object(adapter.subprocess, 'run') as mocked:
            with self.assertRaises(UnicodeDecodeError):
                adapter.run(self.source, self.detector, 'ko', 'unknown', self.output)
        mocked.assert_not_called()
        self.assertFalse(self.output.exists())

    def test_actual_installed_korean_pipeline_preserves_exact_input(self):
        if not (DETECTOR / 'scripts/korean_model.py').is_file():
            self.skipTest('Optional installed Korean detector is unavailable')
        result = adapter.run(self.source, DETECTOR, 'ko', 'unknown', self.output)
        self.assertEqual(result['status'], 'completed')
        self.assertEqual((self.output / 'input.txt').read_bytes(), RAW)
        self.assertEqual(result['input_sha256'], adapter.digest(RAW))
        native = json.loads((self.output / 'model-result.json').read_text('utf-8'))
        self.assertEqual(native['characters_codepoints'], len(RAW.decode('utf-8')))
        self.assertEqual(native['text_sha256'], adapter.digest(RAW))
        index = json.loads((self.output / 'index.json').read_text('utf-8'))
        self.assertTrue(index['paragraphs'][0]['text'].startswith('\ufeff'))
        self.assertEqual(result['paragraph_review_required'], ['P1', 'P2'])


if __name__ == '__main__':
    unittest.main()
