def analyze_nft_activity(transactions):
    """
    Analyze NFT-related activity from a user's transaction history.
    Args:
        transactions (list): List of transactions from Solana API.
    Returns:
        dict: Summary of NFT activity including total NFTs and unique collections.
    """
    try:
        nft_transactions = [tx for tx in transactions if "NFT" in tx.get("memo", "")]
        unique_collections = set(tx.get("memo", "").split(":")[1] for tx in nft_transactions if ":" in tx.get("memo", ""))
        return {
            "total_nfts": len(nft_transactions),
            "unique_collections": len(unique_collections)
        }
    except Exception as e:
        print(f"Error analyzing NFT activity: {e}")
        return {"total_nfts": 0, "unique_collections": 0}

# Example usage
if __name__ == "__main__":
    transactions = [
        {"memo": "NFT:CryptoPunks"},
        {"memo": "Transfer"},
        {"memo": "NFT:BoredApeYachtClub"},
    ]
    nft_summary = analyze_nft_activity(transactions)
    print("NFT Activity Summary:")
    print(nft_summary)
