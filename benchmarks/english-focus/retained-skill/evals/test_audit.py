"""Checks real preservation defects and documents important blind spots."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts' / 'audit_preservation.py'
spec = importlib.util.spec_from_file_location('audit_preservation', SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class PreservationTests(unittest.TestCase):
    def categories(self, source, rewrite, protected=None):
        return {x['category'] for x in module.audit(source, rewrite, protected)['review_candidates']}

    def test_clean_korean_rewrite(self):
        self.assertFalse(self.categories('시험은 12회 진행했습니다. 평균은 2.5 ms입니다.', '12회 시험했습니다. 평균은 2.5 ms입니다.'))

    def test_changed_number(self):
        self.assertIn('numbers', self.categories('The rate is 12.5%.', 'The rate is 15.2%.'))

    def test_changed_unit(self):
        self.assertIn('quantities', self.categories('The dose is 2 mg.', 'The dose is 2 g.'))

    def test_sign_and_scientific_notation(self):
        self.assertIn('numbers', self.categories('Change: -3.2e-4.', 'Change: 3.2e-4.'))

    def test_percent_point_difference(self):
        self.assertIn('quantities', self.categories('It rose 20%.', 'It rose 20 percentage points.'))

    def test_range_endpoint(self):
        self.assertIn('numbers', self.categories('참가자는 30~40명입니다.', '참가자는 30~50명입니다.'))

    def test_quote(self):
        self.assertIn('quoted_spans', self.categories('She said “not proven”.', 'She said “proven”.'))

    def test_blockquote(self):
        self.assertIn('blockquote_lines', self.categories('> Keep my words.', '> Keep our words.'))

    def test_code_and_inline(self):
        source = '~~~python\ncall(2)\n~~~\nUse `dry_run`.'
        rewrite = '~~~python\ncall(3)\n~~~\nUse `run`.'
        self.assertTrue({'fenced_code', 'inline_code'} <= self.categories(source, rewrite))

    def test_nested_url_preserved(self):
        source = '[doc](https://example.org/a_(b))'
        self.assertEqual(module.url_values(source), ['https://example.org/a_(b)'])
        self.assertFalse(self.categories(source, 'Read ' + source))

    def test_url_target_changed(self):
        self.assertIn('urls', self.categories('[A](https://example.org/a)', '[A](https://example.org/b)'))

    def test_citation_removed(self):
        self.assertIn('citations', self.categories('Prior work [@kim2025].', 'Prior work.'))

    def test_named_entity_protection(self):
        self.assertIn('protected_text', self.categories('Mina led the review.', 'Jin led the review.', ['Mina']))

    def test_missing_protection_is_flagged(self):
        self.assertIn('protection_not_in_source', self.categories('Hi.', 'Hi.', ['Mina']))

    def test_invisible_insertion(self):
        self.assertIn('added_control_characters', self.categories('human', 'hu\u200bman'))

    def test_real_emoji_not_flagged_as_invisible(self):
        self.assertNotIn('added_control_characters', self.categories('Hi', 'Hi 👩\u200d💻'))

    def test_reordering_is_not_a_numeric_error(self):
        self.assertNotIn('numbers', self.categories('A has 2; B has 3.', 'B has 3; A has 2.'))

    def test_semantic_blind_spot_is_explicit(self):
        result = module.audit('A has 2; B has 3.', 'A has 3; B has 2.')
        self.assertEqual(result['status'], 'no_surface_change_found')
        self.assertTrue(result['semantic_review_required'])
        self.assertFalse(result['authorship_assessed'])

    def test_negation_blind_spot_is_explicit(self):
        result = module.audit('The effect is not proven.', 'The effect is proven.')
        self.assertTrue(result['semantic_review_required'])
        self.assertFalse(result['authorship_assessed'])

    def test_cli_utf8_and_exit_codes(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            a, b, out = root/'a.md', root/'b.md', root/'audit.json'
            a.write_text('값은 2 ms입니다.', encoding='utf-8-sig')
            b.write_text('값은 3 ms입니다.', encoding='utf-8')
            result = subprocess.run([sys.executable, str(SCRIPT), str(a), str(b), '--output', str(out)], capture_output=True)
            self.assertEqual(result.returncode, 1)
            self.assertEqual(json.loads(out.read_text(encoding='utf-8'))['status'], 'review_required')

    def test_cli_refuses_input_overwrite(self):
        with tempfile.TemporaryDirectory() as td:
            a = Path(td)/'a.md'
            a.write_text('Keep this.', encoding='utf-8')
            result = subprocess.run([sys.executable, str(SCRIPT), str(a), str(a), '--output', str(a)], capture_output=True)
            self.assertEqual(result.returncode, 2)
            self.assertEqual(a.read_text(encoding='utf-8'), 'Keep this.')

    def test_cli_missing_input_is_not_success(self):
        with tempfile.TemporaryDirectory() as td:
            path = str(Path(td)/'missing.md')
            result = subprocess.run([sys.executable, str(SCRIPT), path, path], capture_output=True)
            self.assertEqual(result.returncode, 2)


if __name__ == '__main__':
    unittest.main()
