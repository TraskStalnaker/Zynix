from solana.rpc.api import Client
import pandas as pd

# Initialize Solana client
client = Client("https://api.mainnet-beta.solana.com")

def fetch_transactions(wallet_address, limit=100):
    """
    Fetch transaction history for a given Solana wallet.
    Args:
        wallet_address (str): Public key of the wallet.
        limit (int): Number of transactions to fetch. Default is 100.
    Returns:
        list: A list of transaction records.
    """
    try:
        response = client.get_confirmed_signature_for_address2(wallet_address, limit=limit)
        if "result" in response and response["result"]:
            return response["result"]
        else:
            print("No transactions found.")
            return []
    except Exception as e:
        print(f"Error fetching transactions: {e}")
        return []

def clean_transactions(raw_data):
    """
    Clean raw transaction data for further analysis.
    Args:
        raw_data (list): Raw transaction records from Solana API.
    Returns:
        pd.DataFrame: Cleaned transaction data as a pandas DataFrame.
    """
    if not raw_data:
        return pd.DataFrame()

    try:
        # Convert raw data to DataFrame
        df = pd.DataFrame(raw_data)
        # Select relevant columns
        df = df[["signature", "slot", "err"]]
        # Filter out transactions with errors
        df = df[df["err"].isna()]
        return df
    except Exception as e:
        print(f"Error cleaning transaction data: {e}")
        return pd.DataFrame()

# Example usage
if __name__ == "__main__":
    wallet_address = "YourWalletAddressHere"
    raw_transactions = fetch_transactions(wallet_address)
    print("Raw Transactions:")
    print(raw_transactions)

    cleaned_data = clean_transactions(raw_transactions)
    print("\nCleaned Transactions:")
    print(cleaned_data)
