import json
import os
import unittest
from pathlib import Path


class AICConfigTests(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(__file__).resolve().parents[1]
        self.ai_dir = self.root / ".ai"

    def test_readme_ai_is_short(self) -> None:
        readme = self.ai_dir / "README.ai"
        self.assertTrue(readme.exists(), "README.ai should exist")
        with readme.open("r", encoding="utf-8") as handle:
            lines = [line.strip() for line in handle if line.strip()]
        self.assertLessEqual(len(lines), 3, "README.ai should be no more than three non-empty lines")

    def test_index_json_is_single_line_compact_json(self) -> None:
        index = self.ai_dir / "index.json"
        self.assertTrue(index.exists(), "index.json should exist")
        payload = index.read_text(encoding="utf-8")
        self.assertEqual(payload.count("\n"), 0, "index.json should be compact single-line JSON")
        json.loads(payload)

    def test_policies_include_required_fields(self) -> None:
        policies = self.ai_dir / "policies.yaml"
        self.assertTrue(policies.exists(), "policies.yaml should exist")
        payload = policies.read_text(encoding="utf-8")
        required = [
            "history_retention_days:",
            "required_for:",
            "token_budget:",
            "memory:",
            "secrets:",
        ]
        for item in required:
            self.assertIn(item, payload, f"policies.yaml should include {item}")


if __name__ == "__main__":
    unittest.main()
