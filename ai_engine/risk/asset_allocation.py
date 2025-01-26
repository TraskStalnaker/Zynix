import numpy as np

def optimize_asset_allocation(profile, risk_predictions):
    """
    Optimize asset allocation based on personality profile and risk predictions.
    Args:
        profile (dict): User personality profile (e.g., risk tolerance).
        risk_predictions (list): Predicted risk scores for assets.
    Returns:
        dict: Recommended allocation percentages for different asset types.
    """
    try:
        risk_tolerance = profile.get("risk_tolerance", 0.5)
        # Normalize risk predictions
        normalized_risks = np.array(risk_predictions) / np.max(risk_predictions)

        # Calculate allocation weights (lower risk -> higher allocation)
        weights = 1 - normalized_risks
        weights = weights / np.sum(weights)  # Normalize to 100%

        # Adjust based on risk tolerance
        allocation = {
            f"Asset_{i+1}": round(weight * risk_tolerance * 100, 2)
            for i, weight in enumerate(weights)
        }
        return allocation
    except Exception as e:
        print(f"Error optimizing asset allocation: {e}")
        return {}

# Example usage
if __name__ == "__main__":
    personality_profile = {"risk_tolerance": 0.7}
    risk_scores = [0.2, 0.5, 0.9, 0.1]
    allocation = optimize_asset_allocation(personality_profile, risk_scores)
    print("Recommended Allocation:")
    print(allocation)
