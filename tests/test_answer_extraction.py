import unittest

from src.evaluation.answer import extract_final_answer


class FinalAnswerExtractionTest(unittest.TestCase):
    def test_markdown_heading_does_not_override_boxed_answer(self):
        text = "#### Step 1: Expand\nSo the answer is \\boxed{7}."
        self.assertEqual(extract_final_answer(text), "7")

    def test_trailing_markdown_heading_does_not_override_boxed_answer(self):
        text = "Work.\n\\boxed{7}\n#### Final check"
        self.assertEqual(extract_final_answer(text), "7")

    def test_gsm8k_reference_marker_on_last_line(self):
        text = "Natalia sold 48/2 = 24 clips in May.\n48+24 = 72\n#### 72"
        self.assertEqual(extract_final_answer(text), "72")

    def test_gsm8k_marker_with_trailing_whitespace(self):
        self.assertEqual(extract_final_answer("Total 5,600\n#### 5,600\n\n"), "5,600")

    def test_heading_without_boxed_falls_through_to_final_answer_patterns(self):
        text = "#### Step 1\nCompute the sum.\nFinal answer: 12"
        self.assertEqual(extract_final_answer(text), "12")


if __name__ == "__main__":
    unittest.main()
