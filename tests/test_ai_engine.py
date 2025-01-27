import unittest
from ai_engine.models.personality_analysis import generate_personality

class TestAIEngine(unittest.TestCase):
    """
    Unit tests for the AI personality analysis engine.
    """

    def setUp(self):
        """
        Set up test data for consistent use across multiple test cases.
        """
        self.transactions = [
            {"transaction_value": 100, "transaction_frequency": 5, "date": "2023-01-01"},
            {"transaction_value": 200, "transaction_frequency": 10, "date": "2023-01-02"},
        ]

    def test_generate_personality_structure(self):
        """
        Test that the personality profile contains the expected keys.
        """
        profile = generate_personality(self.transactions)
        # Verify the existence of key personality attributes
        self.assertIn("risk_tolerance", profile, "Profile should include risk_tolerance.")
        self.assertIn("active_days", profile, "Profile should include active_days.")
        self.assertIn("average_transaction_value", profile, "Profile should include average_transaction_value.")

    def test_generate_personality_values(self):
        """
        Test that the calculated personality attributes have plausible values.
        """
        profile = generate_personality(self.transactions)
        # Check that risk_tolerance falls within an expected range
        self.assertGreaterEqual(profile["risk_tolerance"], 0.0, "Risk tolerance should be non-negative.")
        self.assertLessEqual(profile["risk_tolerance"], 1.0, "Risk tolerance should not exceed 1.0.")
        # Check that active_days is correctly calculated
        self.assertEqual(profile["active_days"], 2, "Active days should match the number of unique transaction dates.")

    def test_generate_personality_edge_cases(self):
        """
        Test the function's behavior with edge case inputs.
        """
        # Test with an empty transaction list
        empty_transactions = []
        profile = generate_personality(empty_transactions)
        self.assertEqual(profile["active_days"], 0, "Active days should be 0 for empty transaction data.")
        self.assertEqual(profile["risk_tolerance"], 0.0, "Risk tolerance should be 0 for no transactions.")

        # Test with transactions having zero values
        zero_value_transactions = [
            {"transaction_value": 0, "transaction_frequency": 0, "date": "2023-01-01"}
        ]
        profile = generate_personality(zero_value_transactions)
        self.assertEqual(profile["average_transaction_value"], 0, "Average transaction value should be 0.")
        self.assertEqual(profile["risk_tolerance"], 0.0, "Risk tolerance should be 0 for zero-value transactions.")

if __name__ == "__main__":
    unittest.main()
