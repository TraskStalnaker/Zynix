import requests

IPFS_API_URL = "http://localhost:5001/api/v0"

def upload_to_ipfs(file_path):
    """
    Upload a file to IPFS.
    Args:
        file_path (str): Path to the file to upload.
    Returns:
        str: The CID (Content Identifier) of the uploaded file.
    """
    try:
        with open(file_path, "rb") as file:
            response = requests.post(f"{IPFS_API_URL}/add", files={"file": file})
            response_data = response.json()
            return response_data["Hash"]  # Return the IPFS CID
    except Exception as e:
        print(f"Error uploading to IPFS: {e}")
        return None

def fetch_from_ipfs(cid):
    """
    Fetch a file from IPFS using its CID.
    Args:
        cid (str): Content Identifier of the file.
    Returns:
        bytes: The file content.
    """
    try:
        response = requests.get(f"{IPFS_API_URL}/cat?arg={cid}")
        return response.content
    except Exception as e:
        print(f"Error fetching from IPFS: {e}")
        return None

# Example usage
if __name__ == "__main__":
    cid = upload_to_ipfs("example_file.txt")
    print(f"Uploaded to IPFS with CID: {cid}")

    content = fetch_from_ipfs(cid)
    print(f"Fetched content: {content.decode()}")
