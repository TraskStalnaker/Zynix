from flask import Flask, request, jsonify
from ai_engine.risk.asset_allocation import optimize_asset_allocation
from ai_engine.models.personality_analysis import generate_personality
from core.blockchain.transaction_fetcher import fetch_transactions, clean_transactions

app = Flask(__name__)

@app.route("/api/asset_allocation", methods=["GET"])
def get_asset_allocation():
    """
    API endpoint to provide asset allocation recommendations for a given wallet.
    Query Parameters:
        wallet_address (str): Public key of the wallet.
    Returns:
        JSON: Recommended asset allocation percentages.
    """
    wallet_address = request.args.get("wallet_address")
    if not wallet_address:
        return jsonify({"error": "wallet_address is required"}), 400

    # Fetch and clean transaction data
    raw_data = fetch_transactions(wallet_address)
    transactions = clean_transactions(raw_data)

    if transactions.empty:
        return jsonify({"error": "No transactions found for the wallet."}), 404

    # Generate personality profile
    profile = generate_personality(transactions.to_dict(orient="records"))

    # Generate risk predictions (simulate for now)
    risk_predictions = [0.2, 0.5, 0.8, 0.3]  # Example risk values

    # Optimize asset allocation
    allocation = optimize_asset_allocation(profile, risk_predictions)

    return jsonify(allocation)

if __name__ == "__main__":
    app.run(debug=True)
