from solana.rpc.api import Client
from solana.transaction import Transaction
from solana.keypair import Keypair
import json

# Initialize Solana client
client = Client("https://api.mainnet-beta.solana.com")

def interact_with_contract(wallet, contract_address, method, args):
    """
    Interact with a deployed Solana smart contract.
    Args:
        wallet (Keypair): User's wallet keypair.
        contract_address (str): Address of the deployed contract.
        method (str): Method name to call.
        args (list): Arguments for the method call.
    Returns:
        dict: Response from the contract interaction.
    """
    try:
        # Build the transaction
        tx = Transaction()
        # Example: Adding an instruction (customize for the actual contract)
        tx.add(contract_address, method, args)

        # Send the transaction
        response = client.send_transaction(tx, wallet)
        return response
    except Exception as e:
        print(f"Error interacting with contract: {e}")
        return None

# Example usage
if __name__ == "__main__":
    wallet = Keypair.generate()
    contract_address = "YourContractAddressHere"
    response = interact_with_contract(wallet, contract_address, "updateRiskLevel", [wallet.public_key, 3])
    print(json.dumps(response, indent=2))
