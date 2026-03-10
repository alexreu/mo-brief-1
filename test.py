import unittest
from fastapi.testclient import TestClient
from api import app

class TestSentimentAnalysis(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_analyse_sentiment(self):
        response = self.client.post("/analyse_sentiment/", json={"text": "I love this product!"})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("pos", data)
        self.assertIn("neg", data)
        self.assertIn("neu", data)
        self.assertIn("compound", data)

if __name__ == '__main__':
    unittest.main()