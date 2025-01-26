# Zynix

## AI + Web3 Intelligent Digital Persona and Asset Protection

Zynix is a Web3 application driven by artificial intelligence as the core, which redefines the identity and asset management of users in a decentralized world. Through deep learning and behavior modeling technology, it transforms the user's on-chain data into a visual "digital personality" and dynamically updates the user's on-chain behavior portrait, giving each user a unique intelligent identity. On this basis, Zynix uses AI models to predict asset risks in real time, identify investment opportunities, optimize asset allocation, and provide users with intelligent asset protection solutions. 

The core innovation of Zynix is that AI technology is not only a tool, but also an "thinking extension" of users in Web3: it can self-learn user behavior patterns, dynamically adjust the protection strategy of user assets, and even actively warn risks before users are aware of them. This application is like an AI-driven "digital split", which transforms the complexity of Web3 into an experience that each user can understand and control with accurate predictions and personalized services.

## Project Directory Structure

```
Zynix/
├── core/                               # Core blockchain and smart contract logic
│   ├── blockchain/                     # Blockchain-related utilities
│   │   ├── wallet_management.py        # Generate and manage user wallets
│   │   ├── transaction_fetcher.py      # Fetch and clean on-chain transaction data
│   │   ├── nft_tracker.py              # Track NFT-related activities
│   │   ├── defi_monitor.py             # Monitor DeFi investments and returns
├── ai_engine/                          # AI models and utilities
│   ├── models/                         # Machine learning models for risk and behavior
│   │   ├── personality_analysis.py     # Generate digital persona based on behavior
│   │   ├── clustering.py               # Cluster user behavior patterns
│   │   ├── risk_prediction.py          # Predict risks using time-series models
│   ├── risk/                           # Asset risk prediction and optimization
│   │   ├── asset_allocation.py         # Optimize asset allocation based on risk
│   │   ├── time_series_model.py        # LSTM model for time-series risk prediction
│   ├── nlp/                            # NLP analysis for metadata and notes
│   │   ├── proposal_analysis.py        # Analyze governance proposals
│   │   ├── interaction_system.py       # Natural language interaction system
│   ├── utils/                          # Utility functions for AI models
│   │   ├── data_preprocessor.py        # Preprocessing utilities for data cleaning
│   │   ├── evaluation_metrics.py       # Metrics for evaluating AI models
├── frontend/                           # Frontend for user interaction
│   ├── api/                            # Flask API backend
│   │   ├── app.py                      # Main Flask application
│   │   ├── risk_alerts.py              # API endpoint for risk alerts
│   │   ├── asset_allocation.py         # API endpoint for asset allocation
│   ├── react/                          # React-based user interface
│   │   ├── components/                 # React components for UI
│   │   │   ├── Dashboard.jsx           # Main user dashboard
│   │   │   ├── PersonalityCard.jsx     # Display digital persona
│   │   │   ├── RiskAlerts.jsx          # Display risk alerts
│   │   │   ├── AssetAllocation.jsx     # Display asset allocation
│   │   ├── services/                   # Services for API interactions
│   │   │   ├── apiService.js           # Axios-based API service
│   │   ├── styles/                     # CSS and global styles
│   │   │   ├── global.css              # Global styles for the application
│   │   ├── index.js                    # Main entry point for the React app
├── infra/                              # Infrastructure and storage utilities
│   ├── database/                       # Database schema and connection utilities
│   │   ├── schema.sql                  # PostgreSQL database schema
│   │   ├── data_connector.py           # Connect to and query the database
│   ├── storage/                        # Storage-related utilities
│   │   ├── ipfs_client.py              # IPFS client for distributed storage
├── tests/                              # Unit and integration tests
│   ├── test_blockchain.py              # Tests for blockchain functions
│   ├── test_ai_engine.py               # Tests for AI models
│   ├── test_integration.py             # Integration tests for full pipeline
│   ├── test_risk_alerts.py             # Tests for risk alerts API
├── README.md                           # Project documentation
├── requirements.txt                    # Python dependencies
├── package.json                        # JavaScript dependencies for React
```

## Highlights

### `core/`
- Contains all blockchain logic and smart contracts.
- Includes utilities to interact with Solana network, track NFTs, and monitor DeFi activities.
- Provides smart contract definitions for risk management and digital persona NFTs.

### `ai_engine/`
- Implements AI models for generating user behavior profiles, risk predictions, and asset allocation strategies.
- Includes NLP tools for analyzing transaction metadata and governance proposals.

### `frontend/`
- Provides a React-based UI for interacting with the platform.
- Integrates with Flask API endpoints for fetching and displaying real-time data.

### `infra/`
- Handles database and distributed storage solutions (PostgreSQL, IPFS).
- Includes schema definitions and data connectors.

### `tests/`
- Comprehensive test suite for blockchain interactions, AI models, and API endpoints.
- Includes integration tests to validate the full pipeline.

---

## Getting Started

### Prerequisites
- Python 3.8+
- Node.js 14+
- PostgreSQL 12+
- Solana CLI and Keypair setup
- IPFS daemon running locally or via Infura

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/TraskStalnaker/zynix.git
   cd zynix

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Install React dependencies:
   ```bash
   cd frontend/react
   npm install
   ```
4. Set up the PostgreSQL database:
   ```bash
   psql -U your_user -d your_database -f infra/database/schema.sql
   ```
5. Configure `.env` files for API keys and environment variables.

### Running the Application
1. Start the Flask backend:
   ```bash
   python frontend/api/app.py
   ```
2. Start the React frontend:
   ```bash
   cd frontend/react
   npm start
   ```

### Testing
Run the full test suite:
```bash
pytest tests/
```

