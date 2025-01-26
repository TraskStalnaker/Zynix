import pandas as pd

def analyze_defi_investments(transactions):
    """
    Analyze DeFi investment activity from a user's transaction history.
    Args:
        transactions (list): List of user's transaction records.
    Returns:
        dict: Summary of DeFi investments including total investments and ROI.
    """
    try:
        # Filter DeFi-related transactions
        defi_transactions = [tx for tx in transactions if "DeFi" in tx.get("memo", "")]
        if not defi_transactions:
            return {"total_investments": 0, "roi": 0.0}

        # Convert to DataFrame for analysis
        df = pd.DataFrame(defi_transactions)
        df["amount"] = df.get("amount", 0).astype(float)

        # Calculate total investments
        total_investments = df["amount"].sum()

        # Example: Calculate ROI (randomized for simplicity)
        roi = total_investments * 0.15  # Assume 15% return as an example

        return {
            "total_investments": total_investments,
            "roi": roi
        }
    except Exception as e:
        print(f"Error analyzing DeFi investments: {e}")
        return {"total_investments": 0, "roi": 0.0}

# Example usage
if __name__ == "__main__":
    transactions = [
        {"memo": "DeFi:LiquidityPool", "amount": 500},
        {"memo": "DeFi:Staking", "amount": 300},
        {"memo": "Transfer", "amount": 200},
    ]
    defi_summary = analyze_defi_investments(transactions)
    print("DeFi Investment Summary:")
    print(defi_summary)
