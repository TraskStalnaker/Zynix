from flask import Flask, request, jsonify
from core.blockchain.transaction_fetcher import fetch_transactions, clean_transactions
from ai_engine.risk.risk_prediction import train_and_predict

app = Flask(__name__)

@app.route("/api/risk_alerts", methods=["GET"])
def get_risk_alerts():
    """
    API endpoint to provide risk alerts for a given wallet address.
    Query Parameters:
        wallet_address (str): Public key of the wallet.
    Returns:
        JSON: Risk alerts and advice for the user.
    """
    wallet_address = request.args.get("wallet_address")
    if not wallet_address:
        return jsonify({"error": "wallet_address is required"}), 400

    # Fetch transactions
    raw_data = fetch_transactions(wallet_address)
    transactions = clean_transactions(raw_data)

    if transactions.empty:
        return jsonify({"alerts": [], "advice": "No transaction data available."})

    # Extract risk-related data (e.g., transaction amounts)
    transaction_values = transactions["amount"].values if "amount" in transactions.columns else []

    # Generate risk predictions
    risk_predictions = train_and_predict(transaction_values) if len(transaction_values) > 0 else []

    # Generate risk alerts based on predictions
    alerts = []
    for i, risk in enumerate(risk_predictions):
        if risk > 0.7:  # Arbitrary threshold for high risk
            alerts.append({"message": f"High risk detected in transaction {i + 1}."})

    # Return risk alerts
    return jsonify({"alerts": alerts, "advice": "Consider diversifying your portfolio."})

if __name__ == "__main__":
    app.run(debug=True)
