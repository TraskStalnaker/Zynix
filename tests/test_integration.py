import unittest
from core.blockchain.wallet_management import generate_wallet, get_balance
from core.blockchain.transaction_fetcher import fetch_transactions, clean_transactions
from ai_engine.models.personality_analysis import generate_personality

class TestIntegration(unittest.TestCase):
    def test_full_pipeline(self):
        # Generate a wallet
        wallet = generate_wallet()
        self.assertIn("public_key", wallet)

        # Fetch transactions
        raw_transactions = fetch_transactions(wallet["public_key"])
        self.assertIsInstance(raw_transactions, list)

        # Clean transactions
        cleaned_transactions = clean_transactions(raw_transactions)
        self.assertFalse(cleaned_transactions.empty)

        # Generate personality
        personality = generate_personality(cleaned_transactions.to_dict(orient="records"))
        self.assertIn("risk_tolerance", personality)
        self.assertIn("active_days", personality)

    def test_api_integration(self):
        from flask import Flask
        from frontend.api.app import app

        # Test Flask API endpoint
        with app.test_client() as client:
            response = client.get("/api/personality?wallet_address=TestWalletAddress")
            self.assertEqual(response.status_code, 200)
            self.assertIn("risk_tolerance", response.get_json())

if __name__ == "__main__":
    unittest.main()
