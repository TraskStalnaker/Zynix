import React, { useEffect, useState } from "react";
import axios from "../services/apiService";

const AssetAllocation = ({ walletAddress }) => {
  const [allocation, setAllocation] = useState({});

  useEffect(() => {
    axios
      .get(`/api/asset_allocation?wallet_address=${walletAddress}`)
      .then((response) => setAllocation(response.data))
      .catch((error) => console.error("Error fetching asset allocation:", error));
  }, [walletAddress]);

  return (
    <div className="bg-blue-50 border-l-4 border-blue-400 p-4 mb-4 rounded-lg">
      <h2 className="text-lg font-bold text-blue-700 mb-2">Asset Allocation</h2>
      {Object.keys(allocation).length > 0 ? (
        <ul>
          {Object.entries(allocation).map(([asset, percentage], index) => (
            <li key={index} className="text-blue-600">
              {asset}: {percentage}%
            </li>
          ))}
        </ul>
      ) : (
        <p className="text-gray-600">No allocation data available.</p>
      )}
    </div>
  );
};

export default AssetAllocation;
