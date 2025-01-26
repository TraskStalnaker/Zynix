// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract PersonalityNFT is ERC721URIStorage, Ownable {
    uint256 private _tokenIds;

    constructor() ERC721("PersonalityNFT", "PNFT") {}

    /**
     * Mint a new Personality NFT.
     * @param recipient Address of the NFT recipient.
     * @param tokenURI Metadata URI for the NFT.
     * @return uint256 ID of the newly minted NFT.
     */
    function mintNFT(address recipient, string memory tokenURI) public onlyOwner returns (uint256) {
        _tokenIds += 1;
        uint256 newItemId = _tokenIds;

        _mint(recipient, newItemId);
        _setTokenURI(newItemId, tokenURI);

        return newItemId;
    }
}
