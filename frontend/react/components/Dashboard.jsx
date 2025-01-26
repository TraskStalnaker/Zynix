import React, { useEffect, useState } from "react";
import axios from "../services/apiService";
import PersonalityCard from "./PersonalityCard";

const Dashboard = () => {
  const [personality, setPersonality] = useState(null);

  useEffect(() => {
    axios
      .get("/api/personality?wallet_address=YourWalletAddressHere")
      .then((response) => setPersonality(response.data))
      .catch((error) => console.error("Error fetching personality:", error));
  }, []);

  return (
    <div className="dashboard">
      <h1 className="text-3xl font-bold mb-6">User Dashboard</h1>
      {personality ? (
        <PersonalityCard personality={personality} />
      ) : (
        <p>Loading personality data...</p>
      )}
    </div>
  );
};

export default Dashboard;
