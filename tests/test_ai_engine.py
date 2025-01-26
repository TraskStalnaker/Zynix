import unittest
from ai_engine.models.personality_analysis import generate_personality

class TestAIEngine(unittest.TestCase):
    def test_generate_personality(self):
        transactions = [
            {"transaction_value": 100, "transaction_frequency": 5, "date": "2023-01-01"},
            {"transaction_value": 200, "transaction_frequency": 10, "date": "2023-01-02"},
        ]
        profile = generate_personality(transactions)
        self.assertIn("risk_tolerance", profile)
        self.assertIn("active_days", profile)

if __name__ == "__main__":
    unittest.main()
