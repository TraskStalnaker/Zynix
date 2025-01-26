import unittest
from frontend.api.risk_alerts import app

class TestRiskAlertsAPI(unittest.TestCase):
    def test_get_risk_alerts(self):
        with app.test_client() as client:
            response = client.get("/api/risk_alerts?wallet_address=TestWalletAddress")
            self.assertEqual(response.status_code, 200)
            data = response.get_json()
            self.assertIn("alerts", data)
            self.assertIn("advice", data)

if __name__ == "__main__":
    unittest.main()
