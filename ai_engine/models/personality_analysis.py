import pandas as pd
from sklearn.cluster import KMeans

def generate_personality(transactions):
    """
    Generate a personality profile based on user's transaction data.
    Args:
        transactions (list): List of user's transaction records.
    Returns:
        dict: A personality profile including risk tolerance and active days.
    """
    try:
        # Convert transactions to DataFrame
        df = pd.DataFrame(transactions)
        # Extract features for clustering
        features = df[["transaction_value", "transaction_frequency"]].fillna(0)
        kmeans = KMeans(n_clusters=3, random_state=42)
        clusters = kmeans.fit_predict(features)
        return {
            "risk_tolerance": clusters.mean(),
            "active_days": df["date"].nunique()
        }
    except Exception as e:
        print(f"Error generating personality: {e}")
        return {"risk_tolerance": 0, "active_days": 0}

# Example usage
if __name__ == "__main__":
    transactions = [
        {"transaction_value": 100, "transaction_frequency": 5, "date": "2023-01-01"},
        {"transaction_value": 200, "transaction_frequency": 10, "date": "2023-01-02"},
    ]
    personality_profile = generate_personality(transactions)
    print("Personality Profile:")
    print(personality_profile)
