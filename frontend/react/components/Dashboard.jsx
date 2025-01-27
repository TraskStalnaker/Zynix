import React, { useEffect, useState } from "react";
import PersonalityCard from "./PersonalityCard";
import RiskAlerts from "./RiskAlerts";
import AssetAllocation from "./AssetAllocation";

const Dashboard = ({ walletAddress }) => {
  // State for loading and error handling
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [personality, setPersonality] = useState(null);

  // Fetch personality data when the component mounts
  useEffect(() => {
    const fetchPersonality = async () => {
      try {
        setLoading(true);
        // Replace this URL with your API endpoint
        const response = await fetch(`/api/personality/${walletAddress}`);
        if (!response.ok) {
          throw new Error("Failed to fetch personality data");
        }
        const data = await response.json();
        setPersonality(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchPersonality();
  }, [walletAddress]);

  // Render the loading and error states
  if (loading) {
    return <div className="text-center mt-10">Loading...</div>;
  }

  if (error) {
    return <div className="text-center mt-10 text-red-500">{error}</div>;
  }

  return (
    <div className="container mx-auto p-6">
      <h1 className="text-3xl font-bold mb-6 text-center">User Dashboard</h1>
      {personality && <PersonalityCard personality={personality} />}
      <RiskAlerts walletAddress={walletAddress} />
      <AssetAllocation walletAddress={walletAddress} />
    </div>
  );
};

export default Dashboard;
