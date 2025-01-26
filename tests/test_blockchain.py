import unittest
from core.blockchain.wallet_management import generate_wallet, get_balance

class TestBlockchainFunctions(unittest.TestCase):
    def test_generate_wallet(self):
        wallet = generate_wallet()
        self.assertIn("public_key", wallet)
        self.assertIn("secret_key", wallet)

    def test_get_balance(self):
        wallet = generate_wallet()
        balance = get_balance(wallet["public_key"])
        self.assertIsInstance(balance, (float, int))

if __name__ == "__main__":
    unittest.main()
