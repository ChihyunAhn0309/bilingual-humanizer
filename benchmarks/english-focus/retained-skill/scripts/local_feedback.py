"""Run the installed bilingual-ai-detector offline and preserve a per-candidate receipt.

This is a transport/identity adapter, not a rewriting engine or authorship certificate.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
import os
from pathlib import Path
import re
import subprocess
import sys


# Supported installed detector contract. A changed release needs an explicit review.
KO_MODEL = 'korean-char-style-logistic-v1'
KO_HASH = 'f3048088269f293b5f54b131a26571eefcdb9ffd57d86acfd41b4d8d71d41e1f'
EN_MODEL = 'wasitaigeneratedcom/ai-text-detector-small'
EN_REVISION = 'f1795c86806e6838d4afa33d0b1427f8430c9615'
EN_HASH = '4a1561fadf44ec72934edd6158ff8c76e9388ade1384dbeeea6eb15f93251087'


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def write(path, value):
    with path.open('x', encoding='utf-8', newline='\n') as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2, allow_nan=False)
        stream.write('\n')


def probabilities(value, labels):
    if (not isinstance(value, dict) or set(value) != set(labels)
            or any(type(p) not in (int, float) or not 0 <= p <= 1 or not math.isfinite(p) for p in value.values())
            or not math.isclose(sum(value.values()), 1, abs_tol=1e-5, rel_tol=0)):
        raise ValueError('Missing or invalid native class probabilities')
    return value


def required_metadata(value, expected):
    if not isinstance(value, dict) or any(type(value.get(k)) is not type(v) or value[k] != v
                                          for k, v in expected.items()):
        raise ValueError('Missing or unsupported detector metadata')


def string_list(value):
    if not isinstance(value, list) or any(not isinstance(item, str) or not item.strip() for item in value):
        raise ValueError('Missing or invalid detector cautions')
    return value


def normalize(result, raw, language):
    """Keep model semantics and missing document scores; never turn an error into Human."""
    if language not in ('ko', 'en'):
        raise ValueError('Unsupported language')
    if not isinstance(result, dict) or 'error' in result or result.get('status', 'completed') != 'completed':
        raise ValueError('Expected a completed detector result object')
    if result.get('text_sha256') != digest(raw):
        raise ValueError('Result belongs to a different input')
    required_metadata(result, {'external_detector_calls': 0, 'authorship_verified': False})
    measured = result.get('measured_at_utc')
    if not isinstance(measured, str) or datetime.fromisoformat(measured).utcoffset() != timezone.utc.utcoffset(None):
        raise ValueError('Missing UTC measurement time')
    if language == 'ko':
        required_metadata(result, {'mode': 'offline_korean_calibrated_classifier', 'all_input_scored': True,
                                   'characters_codepoints': len(raw.decode('utf-8')),
                                   'model_id': KO_MODEL, 'model_sha256': KO_HASH})
        classes = probabilities(result.get('class_probabilities'), ['human', 'ai'])
        model, model_hash = result.get('model_id'), result.get('model_sha256')
        cautions = string_list(result.get('applicability_cautions')) + string_list(result.get('known_limits'))
        if not result['known_limits']:
            raise ValueError('Missing Korean model limitations')
        semantics = result.get('probability_semantics')
        calibration = result.get('calibration')
        required_metadata(calibration, {'method': 'held_out_regularized_sigmoid'})
        features, sensitivity = result.get('feature_explanation'), result.get('paragraph_sensitivity')
        if (not isinstance(features, dict) or not isinstance(features.get('lexical'), list)
                or not isinstance(sensitivity, dict)):
            raise ValueError('Missing Korean measured-evidence metadata')
        evidence = {'lexical': features['lexical'], 'paragraph_sensitivity': sensitivity}
        scope = 'whole_document'
    else:
        required_metadata(result, {'schema_version': 2, 'mode': 'offline_local_model',
                                   'model': EN_MODEL, 'revision': EN_REVISION, 'weight_sha256': EN_HASH,
                                   'all_input_tokens_scored': True, 'independently_calibrated_here': False,
                                   'validation_status': 'experimental_auxiliary_score_not_a_validated_authorship_detector'})
        required_metadata(result.get('execution_guard'), {'worker_exit_code': 0, 'serialized_cli': True,
                                                         'native_runtime_stability_guaranteed': False})
        windows = result.get('windows')
        total = result.get('token_count')
        if type(total) is not int or total <= 0 or not isinstance(windows, list) or not windows:
            raise ValueError('English token coverage unavailable')
        covered, previous_start = 0, -1
        for window in windows:
            if not isinstance(window, dict):
                raise ValueError('Invalid English window')
            start, end = window.get('token_start'), window.get('token_end')
            if (type(start) is not int or type(end) is not int or not previous_start < start <= covered
                    or not covered < end <= total or end - start > 766):
                raise ValueError('Incomplete or invalid English token coverage')
            covered, previous_start = end, start
            probabilities(window.get('class_probabilities'), ['human', 'ai', 'ai_edited', 'humanized'])
        if covered != total or 'document_class_probabilities' not in result:
            raise ValueError('Missing English coverage or document probability metadata')
        classes = result.get('document_class_probabilities')
        if len(windows) == 1:
            probabilities(classes, ['human', 'ai', 'ai_edited', 'humanized'])
            if classes != windows[0]['class_probabilities']:
                raise ValueError('Document and window scores differ')
        elif classes is not None:
            raise ValueError('Multi-window document probability must be unavailable')
        model, model_hash = result.get('model'), result.get('weight_sha256')
        if not isinstance(result.get('known_limitations'), str) or not result['known_limitations'].strip():
            raise ValueError('Missing English model limitations')
        cautions = [result.get('known_limitations'), 'English four-class outputs are uncalibrated experimental auxiliary scores.']
        semantics = 'Native Human/AI/AI-edited/Humanized classes; not word shares or verified writing history.'
        occlusion = result.get('occlusion')
        if (not isinstance(occlusion, dict) or type(occlusion.get('performed')) is not bool
                or not isinstance(occlusion.get('paragraphs'), list)):
            raise ValueError('Missing English measured-evidence metadata')
        evidence = {'windows': windows, 'occlusion': occlusion}
        calibration = None
        scope = 'whole_document' if len(windows) == 1 else 'windows_only'
    if (not isinstance(model, str) or not model.strip() or not isinstance(model_hash, str)
            or not re.fullmatch('[0-9a-f]{64}', model_hash)
            or not isinstance(semantics, str) or not semantics.strip()):
        raise ValueError('Missing model identity or score semantics')
    return {'status': 'completed', 'language': language, 'input_sha256': digest(raw),
            'measured_at_utc': measured, 'model': model, 'model_sha256': model_hash,
            'scope': scope, 'native_class_probabilities': classes,
            'human_percent': None if classes is None else classes['human'] * 100,
            'probability_semantics': semantics, 'calibration': calibration,
            'cautions': cautions, 'measured_evidence': evidence,
            'authorship_verified': False, 'semantic_review_required': True,
            'style_review_completed': False, 'external_detector_calls': 0}


def run(input_path, detector, language, genre, output_dir):
    if language not in ('ko', 'en') or genre not in ('essay', 'abstract', 'poetry', 'unknown'):
        raise ValueError('Unsupported language or genre')
    source, detector, output = Path(input_path).resolve(), Path(detector).resolve(), Path(output_dir).resolve()
    raw = source.read_bytes()
    raw.decode('utf-8')  # Exact BOM/CRLF/Unicode bytes are preserved, not normalised.
    output.mkdir(parents=True, exist_ok=False)
    snapshot = output / 'input.txt'
    snapshot.write_bytes(raw)
    metadata = {'schema_version': 1, 'input_sha256': digest(raw), 'language': language,
                'started_at_utc': datetime.now(timezone.utc).isoformat(),
                'detector_skill': str(detector), 'adapter': 'local_feedback_v1'}
    steps = [('index', ['evidence.py', 'index', str(snapshot), '--out', str(output / 'index.json')])]
    if language == 'ko':
        steps.append(('score', ['korean_model.py', str(snapshot), '--genre', genre, '--out', str(output / 'model-result.json')]))
    else:
        steps.append(('score', ['run_english.py', str(snapshot), '--language', 'en', '--explain', '--out', str(output / 'model-result.json')]))
    calls = []
    try:
        for stage, args in steps:
            script = detector / 'scripts' / args[0]
            if not script.is_file():
                raise ValueError('Detector script unavailable: ' + str(script))
            destination = Path(args[-1])
            if destination.exists():
                raise ValueError('Refusing an existing subprocess result: ' + str(destination))
            stage_started = datetime.now(timezone.utc)
            script_hash = digest(script.read_bytes())
            env = dict(os.environ, HF_HUB_OFFLINE='1', TRANSFORMERS_OFFLINE='1')
            try:
                proc = subprocess.run([sys.executable, '-B', '-X', 'utf8', str(script), *args[1:]],
                                      capture_output=True, text=True, encoding='utf-8', errors='replace', env=env)
            except OSError as exc:
                calls.append({'stage': stage, 'script_sha256': script_hash, 'returncode': None, 'error': str(exc)})
                raise
            calls.append({'stage': stage, 'script_sha256': script_hash,
                          'returncode': proc.returncode, 'stdout': proc.stdout, 'stderr': proc.stderr})
            if proc.returncode:
                raise ValueError(f'{stage} failed with exit code {proc.returncode}; no usable score')
            if not destination.is_file():
                raise ValueError(f'{stage} returned no result; no usable score')
        if source.read_bytes() != raw or snapshot.read_bytes() != raw:
            raise ValueError('Input changed during scoring')
        index = json.loads((output / 'index.json').read_text('utf-8'))
        if not isinstance(index, dict) or index.get('text_sha256') != digest(raw):
            raise ValueError('Paragraph index has a different input hash')
        paragraphs = index.get('paragraphs')
        if (not isinstance(paragraphs, list) or not paragraphs
                or any(not isinstance(p, dict) or p.get('id') != f'P{i}' for i, p in enumerate(paragraphs, 1))):
            raise ValueError('Missing or invalid paragraph review coverage')
        result_raw = (output / 'model-result.json').read_bytes()
        feedback = normalize(json.loads(result_raw), raw, language)
        measured = datetime.fromisoformat(feedback['measured_at_utc'])
        if not stage_started <= measured <= datetime.now(timezone.utc):
            raise ValueError('Result measurement is outside this scoring invocation')
        feedback['raw_result_sha256'] = digest(result_raw)
        feedback['paragraph_review_required'] = [p['id'] for p in paragraphs]
        write(output / 'feedback.json', feedback)
        write(output / 'execution.json', metadata | {'status': 'completed', 'calls': calls})
        return feedback
    except (ValueError, OSError, KeyError, TypeError) as exc:
        write(output / 'execution.json', metadata | {'status': 'error', 'error': str(exc), 'calls': calls})
        write(output / 'feedback.json', {'status': 'error', 'input_sha256': digest(raw),
              'human_percent': None, 'native_class_probabilities': None, 'error': str(exc),
              'authorship_verified': False, 'semantic_review_required': True})
        raise


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input')
    parser.add_argument('--language', choices=['ko', 'en'], required=True)
    parser.add_argument('--genre', choices=['essay', 'abstract', 'poetry', 'unknown'], default='unknown')
    default = Path(os.environ.get('CODEX_HOME', str(Path.home() / '.codex'))) / 'skills/bilingual-ai-detector'
    parser.add_argument('--detector-skill', default=str(default))
    parser.add_argument('--out-dir', required=True, help='New directory per input/cycle; existing directories are refused')
    args = parser.parse_args()
    try:
        feedback = run(args.input, args.detector_skill, args.language, args.genre, args.out_dir)
        print(json.dumps({k: feedback[k] for k in ['status', 'scope', 'human_percent', 'cautions']}, ensure_ascii=False))
        return 0
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print(json.dumps({'status': 'error', 'human_percent': None, 'error': str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
