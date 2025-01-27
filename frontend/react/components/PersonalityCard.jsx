import React from "react";

const PersonalityCard = ({ personality }) => {
  // Ensure personality data exists
  if (!personality) {
    return (
      <div className="bg-white shadow-md rounded-lg p-6 text-center">
        <h2 className="text-xl font-bold mb-4">Personality Profile</h2>
        <p>No personality data available.</p>
      </div>
    );
  }

  return (
    <div className="bg-gradient-to-r from-purple-500 to-indigo-500 text-white shadow-md rounded-lg p-6">
      <h2 className="text-2xl font-bold mb-4">Personality Profile</h2>
      <p className="mb-2">
        <strong>Risk Tolerance:</strong> {personality.risk_tolerance}
      </p>
      <p className="mb-2">
        <strong>Active Days:</strong> {personality.active_days}
      </p>
      <p>
        <strong>Average Transaction Value:</strong>{" "}
        {personality.average_transaction_value}
      </p>
    </div>
  );
};

export default PersonalityCard;
