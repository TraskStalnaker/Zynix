import pandas as pd
from sklearn.cluster import KMeans
import numpy as np

def generate_personality(transactions):
    """
    Generate a personality profile based on user's transaction data.
    Args:
        transactions (list): List of user's transaction records.
    Returns:
        dict: A personality profile including risk tolerance and active days.
    """
    try:
        # Validate input data
        if not transactions or not isinstance(transactions, list):
            raise ValueError("Transactions must be a non-empty list.")

        # Convert transactions to DataFrame
        df = pd.DataFrame(transactions)

        # Check for required columns
        required_columns = ["transaction_value", "transaction_frequency", "date"]
        for column in required_columns:
            if column not in df.columns:
                raise ValueError(f"Missing required column: {column}")

        # Extract features for clustering
        features = df[["transaction_value", "transaction_frequency"]].fillna(0)
        
        # Apply KMeans clustering
        kmeans = KMeans(n_clusters=3, random_state=42, n_init=10, max_iter=300)
        clusters = kmeans.fit_predict(features)
        
        # Calculate risk tolerance as the average cluster index
        risk_tolerance = np.mean(clusters)

        # Calculate the number of unique active days
        active_days = df["date"].nunique()

        return {
            "risk_tolerance": round(risk_tolerance, 2),
            "active_days": active_days
        }
    except Exception as e:
        print(f"Error generating personality: {e}")
        return {"risk_tolerance": 0, "active_days": 0}

# Example usage
if __name__ == "__main__":
    transactions = [
        {"transaction_value": 100, "transaction_frequency": 5, "date": "2023-01-01"},
        {"transaction_value": 200, "transaction_frequency": 10, "date": "2023-01-02"},
        {"transaction_value": 150, "transaction_frequency": 7, "date": "2023-01-01"},
        {"transaction_value": 300, "transaction_frequency": 12, "date": "2023-01-03"},
    ]
    personality_profile = generate_personality(transactions)
    print("Personality Profile:")
    print(personality_profile)
