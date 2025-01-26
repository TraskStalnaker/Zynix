from solana.rpc.api import Client
from solana.keypair import Keypair

# Initialize Solana client
client = Client("https://api.mainnet-beta.solana.com")

def generate_wallet():
    """
    Generate a new Solana wallet.
    Returns:
        dict: A dictionary containing public and private keys of the wallet.
    """
    keypair = Keypair.generate()
    wallet = {
        "public_key": str(keypair.public_key),
        "secret_key": list(keypair.secret_key)  # Secret key as a list for compatibility
    }
    return wallet

def get_balance(wallet_address):
    """
    Fetch the balance of a given Solana wallet.
    Args:
        wallet_address (str): Public key of the wallet.
    Returns:
        float: Balance of the wallet in SOL.
    """
    try:
        response = client.get_balance(wallet_address)
        balance = response['result']['value'] / 10**9  # Convert lamports to SOL
        return balance
    except Exception as e:
        print(f"Error fetching balance: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Generate a new wallet
    wallet = generate_wallet()
    print("Generated Wallet:")
    print(f"Public Key: {wallet['public_key']}")
    print(f"Secret Key: {wallet['secret_key']}")

    # Check balance
    balance = get_balance(wallet["public_key"])
    if balance is not None:
        print(f"Wallet Balance: {balance} SOL")
    else:
        print("Unable to fetch wallet balance.")
