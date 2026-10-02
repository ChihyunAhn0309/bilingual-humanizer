"""Validate supplied detector results for one candidate; no network or authorship test."""
from __future__ import annotations

import argparse
from datetime import datetime
import hashlib
import json
import math
from pathlib import Path
import sys


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def numeric(value):
    return type(value) is int or (type(value) is float and math.isfinite(value))


def settings_value(value):
    """Use strict JSON values: Python equality conflates booleans and numbers."""
    return json.dumps(value, sort_keys=True, ensure_ascii=False, allow_nan=False)


def evaluate(bundle: dict, candidate: bytes) -> dict:
    if not isinstance(bundle, dict) or type(bundle.get('schema_version')) is not int or bundle.get('schema_version') != 1:
        raise ValueError('Expected schema_version 1 object')
    targets, results = bundle.get('targets'), bundle.get('results')
    if not isinstance(targets, list) or not targets or not isinstance(results, list):
        raise ValueError('Nonempty targets and results arrays are required')
    plans = {}
    for target in targets:
        if not isinstance(target, dict) or not nonempty(target.get('id')):
            raise ValueError('Each target needs an id')
        key = target['id']
        if key in plans:
            raise ValueError('Duplicate target id: ' + key)
        if type(target.get('required')) is not bool:
            raise ValueError('Each target requires an explicit required boolean')
        if not all(nonempty(target.get(k)) for k in ('service', 'model', 'metric')):
            raise ValueError('Each target needs service, model (unknown allowed), and metric')
        if not isinstance(target.get('settings'), dict):
            raise ValueError('Each target needs settings object')
        settings_value(target['settings'])
        unit, op, value = target.get('unit'), target.get('operator'), target.get('value')
        if unit == 'label':
            if op != 'eq' or not nonempty(value):
                raise ValueError('Label targets need eq and a nonempty string value')
        elif unit in ('fraction', 'percent'):
            if op not in ('lte', 'gte') or not numeric(value) or not 0 <= value <= (1 if unit == 'fraction' else 100):
                raise ValueError('Invalid numerical target')
        else:
            raise ValueError('Unit must be label, fraction, or percent')
        plans[key] = target
    if not any(t['required'] for t in targets):
        raise ValueError('At least one required target is needed')
    receipts = {}
    for result in results:
        if not isinstance(result, dict) or not nonempty(result.get('target_id')) or result['target_id'] not in plans:
            raise ValueError('Result has unknown target_id')
        key = result['target_id']
        if key in receipts:
            raise ValueError('Use one result per target for this candidate; duplicate: ' + key)
        if result.get('status') not in ('ok', 'error', 'unsupported', 'pending'):
            raise ValueError('Unknown result status')
        receipts[key] = result
    digest = hashlib.sha256(candidate).hexdigest()
    rows = []
    for key, target in plans.items():
        result = receipts.get(key)
        reasons = []
        state = 'incomplete'
        if result is None:
            reasons.append('missing_result')
        elif result['status'] != 'ok':
            reasons.append(result['status'])
        else:
            if result.get('input_sha256') != digest:
                reasons.append('candidate_hash_mismatch')
            if result.get('scope') != 'whole_document' or result.get('eligible') is not True:
                reasons.append('whole_document_eligibility_unconfirmed')
            for field in ('service', 'model', 'settings', 'metric', 'unit'):
                equal = settings_value(result.get(field)) == settings_value(target[field]) if field == 'settings' else result.get(field) == target[field]
                if not equal:
                    reasons.append(field + '_mismatch')
            if result.get('origin') not in ('user_report', 'tool_result') or not nonempty(result.get('evidence')):
                reasons.append('missing_evidence_provenance')
            try:
                timestamp = datetime.fromisoformat(result.get('checked_at', '').replace('Z', '+00:00'))
                if timestamp.tzinfo is None:
                    raise ValueError('timezone missing')
            except (TypeError, AttributeError, ValueError):
                reasons.append('invalid_timestamp')
            value = result.get('value')
            if target['unit'] == 'label':
                if not nonempty(value):
                    reasons.append('invalid_label')
            elif not numeric(value) or not 0 <= value <= (1 if target['unit'] == 'fraction' else 100):
                reasons.append('invalid_score')
            elif result.get('value_is_exact') is not True:
                reasons.append('numeric_precision_unconfirmed')
            if not reasons:
                op = target['operator']
                passed = value == target['value'] if op == 'eq' else value <= target['value'] if op == 'lte' else value >= target['value']
                state = 'met' if passed else 'unmet'
                if not passed:
                    reasons.append('target_not_met')
        rows.append({'id': key, 'required': target['required'], 'status': state, 'reasons': reasons})
    required = [r for r in rows if r['required']]
    overall = 'configured_targets_met' if all(r['status'] == 'met' for r in required) else 'incomplete' if any(r['status'] == 'incomplete' for r in required) else 'targets_unmet'
    return {'status': overall, 'candidate_sha256': digest, 'targets': rows,
            'authorship_assessed': False, 'receipt_authenticity_verified': False,
            'semantic_review_required': True,
            'limitation': 'Checks consistency of supplied data only; does not authenticate receipts, query detectors, prove authorship, or evaluate prose.'}


def same_file(a: Path, b: Path) -> bool:
    return a.resolve() == b.resolve() or (a.exists() and b.exists() and a.samefile(b))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('report', type=Path)
    parser.add_argument('candidate', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    try:
        result = evaluate(json.loads(args.report.read_text(encoding='utf-8-sig')), args.candidate.read_bytes())
        output = json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False) + '\n'
        if args.output:
            if any(same_file(args.output, p) for p in (args.report, args.candidate)):
                raise ValueError('Output must not overwrite an input, including links')
            args.output.write_text(output, encoding='utf-8')
        else:
            if hasattr(sys.stdout, 'reconfigure'):
                sys.stdout.reconfigure(encoding='utf-8')
            sys.stdout.write(output)
        return 0 if result['status'] == 'configured_targets_met' else 1
    except (OSError, UnicodeError, ValueError) as exc:
        parser.exit(2, f'Input/output error: {exc}\n')


if __name__ == '__main__':
    raise SystemExit(main())
