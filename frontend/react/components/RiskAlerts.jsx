import React, { useEffect, useState } from "react";
import axios from "../services/apiService";

const RiskAlerts = ({ walletAddress }) => {
  const [alerts, setAlerts] = useState([]);

  useEffect(() => {
    axios
      .get(`/api/risk_alerts?wallet_address=${walletAddress}`)
      .then((response) => setAlerts(response.data.alerts || []))
      .catch((error) => console.error("Error fetching risk alerts:", error));
  }, [walletAddress]);

  return (
    <div className="bg-red-50 border-l-4 border-red-400 p-4 mb-4 rounded-lg">
      <h2 className="text-lg font-bold text-red-700 mb-2">Risk Alerts</h2>
      {alerts.length > 0 ? (
        <ul>
          {alerts.map((alert, index) => (
            <li key={index} className="text-red-600">
              {alert.message}
            </li>
          ))}
        </ul>
      ) : (
        <p className="text-gray-600">No risk alerts at the moment.</p>
      )}
    </div>
  );
};

export default RiskAlerts;
