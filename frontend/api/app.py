from flask import Flask, request, jsonify
from core.blockchain.transaction_fetcher import fetch_transactions, clean_transactions
from ai_engine.models.personality_analysis import generate_personality

app = Flask(__name__)

@app.route("/api/personality", methods=["GET"])
def get_personality():
    """
    API endpoint to fetch a user's personality profile based on transactions.
    Query Parameters:
        wallet_address (str): Public key of the wallet.
    Returns:
        JSON: User's personality profile.
    """
    wallet_address = request.args.get("wallet_address")
    if not wallet_address:
        return jsonify({"error": "wallet_address is required"}), 400

    # Fetch and clean transaction data
    raw_data = fetch_transactions(wallet_address)
    transactions = clean_transactions(raw_data)

    # Generate personality profile
    personality = generate_personality(transactions.to_dict(orient="records"))
    return jsonify(personality)

if __name__ == "__main__":
    app.run(debug=True)
