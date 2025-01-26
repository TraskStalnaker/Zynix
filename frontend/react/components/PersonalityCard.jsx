import React from "react";

const PersonalityCard = ({ personality }) => {
  return (
    <div className="bg-white shadow-md rounded-lg p-6">
      <h2 className="text-xl font-bold mb-4">Personality Profile</h2>
      <p><strong>Risk Tolerance:</strong> {personality.risk_tolerance}</p>
      <p><strong>Active Days:</strong> {personality.active_days}</p>
    </div>
  );
};

export default PersonalityCard;
