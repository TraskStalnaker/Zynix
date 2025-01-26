import React from "react";
import PersonalityCard from "./PersonalityCard";
import RiskAlerts from "./RiskAlerts";
import AssetAllocation from "./AssetAllocation";

const Dashboard = ({ walletAddress }) => {
  return (
    <div className="container">
      <h1 className="text-3xl font-bold mb-6">User Dashboard</h1>
      <PersonalityCard walletAddress={walletAddress} />
      <RiskAlerts walletAddress={walletAddress} />
      <AssetAllocation walletAddress={walletAddress} />
    </div>
  );
};

export default Dashboard;
