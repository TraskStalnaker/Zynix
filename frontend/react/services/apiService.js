import axios from "axios";

// Create an Axios instance for API calls
const apiClient = axios.create({
  baseURL: "http://localhost:5000/api", // Base URL for the Flask API
  timeout: 10000, // Timeout for requests
  headers: {
    "Content-Type": "application/json",
  },
});

// Example API call: Fetch personality data
export const fetchPersonality = async (walletAddress) => {
  try {
    const response = await apiClient.get(`/personality?wallet_address=${walletAddress}`);
    return response.data;
  } catch (error) {
    console.error("Error fetching personality data:", error);
    throw error;
  }
};

// Example API call: Fetch risk alerts
export const fetchRiskAlerts = async (walletAddress) => {
  try {
    const response = await apiClient.get(`/risk_alerts?wallet_address=${walletAddress}`);
    return response.data;
  } catch (error) {
    console.error("Error fetching risk alerts:", error);
    throw error;
  }
};

export default apiClient;
