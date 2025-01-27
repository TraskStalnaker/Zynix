from solana.rpc.api import Client
from solana.transaction import Transaction
from solana.keypair import Keypair
from solana.rpc.types import TxOpts
from solana.system_program import transfer, TransferParams
import json

# Initialize Solana client with mainnet endpoint
client = Client("https://api.mainnet-beta.solana.com")

def interact_with_contract(wallet: Keypair, contract_address: str, method: str, args: list) -> dict:
    """
    Interact with a deployed Solana smart contract.
    
    Args:
        wallet (Keypair): User's wallet keypair containing private and public keys.
        contract_address (str): Address of the deployed Solana contract.
        method (str): The contract method or function to be invoked.
        args (list): Arguments required for the method call.
    
    Returns:
        dict: Response from the Solana network, including transaction signature and result.
    """
    try:
        # Build the transaction
        tx = Transaction()
        
        # Example: Add an instruction for a simple contract interaction
        # In this example, we use a generic transfer instruction as a placeholder.
        # Replace with actual contract logic (e.g., `invoke_signed`).
        tx.add(
            transfer(
                TransferParams(
                    from_pubkey=wallet.public_key,
                    to_pubkey=contract_address,
                    lamports=1000  # Replace with appropriate logic for the method and args
                )
            )
        )

        # Send the transaction to the network with options
        response = client.send_transaction(
            tx, 
            wallet, 
            opts=TxOpts(skip_preflight=False, preflight_commitment="confirmed")
        )
        return response

    except Exception as e:
        print(f"Error interacting with contract: {e}")
        return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    try:
        # Generate a test wallet (replace with an actual keypair for production)
        wallet = Keypair.generate()

        # Define the smart contract address (replace with actual deployed contract address)
        contract_address = "YourContractAddressHere"

        # Interact with the contract
        response = interact_with_contract(
            wallet, 
            contract_address, 
            "updateRiskLevel", 
            [wallet.public_key, 3]  # Example arguments
        )

        # Print response from the Solana network
        print("Contract Interaction Response:")
        print(json.dumps(response, indent=2))
    except Exception as main_exception:
        print(f"Unexpected error in main: {main_exception}")
