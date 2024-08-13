
import unittest
from src.data_processing.preprocess import clean_text, tokenize_text

class TestPreprocessing(unittest.TestCase):

    def test_clean_text(self):
        sample_text = "Hello world! Visit https://localhost:5000"
        cleaned_text = clean_text(sample_text)
        self.assertEqual(cleaned_text, "hello world")

    def test_tokenize_text(self):
        sample_text = "Hello world"
        tokens = tokenize_text(sample_text)
        self.assertListEqual(tokens, ["hello", "world"])

if __name__ == "__main__":
    unittest.main()