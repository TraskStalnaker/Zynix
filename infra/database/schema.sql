-- Table for storing user transactions
CREATE TABLE user_transactions (
    id SERIAL PRIMARY KEY,
    wallet_address VARCHAR(64) NOT NULL,
    transaction_signature VARCHAR(128) UNIQUE NOT NULL,
    transaction_type VARCHAR(32),
    amount NUMERIC(20, 8),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing personality profiles
CREATE TABLE personality_profiles (
    id SERIAL PRIMARY KEY,
    wallet_address VARCHAR(64) NOT NULL UNIQUE,
    risk_tolerance NUMERIC(5, 2),
    active_days INT,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for risk alerts
CREATE TABLE risk_alerts (
    id SERIAL PRIMARY KEY,
    wallet_address VARCHAR(64) NOT NULL,
    risk_level VARCHAR(16),
    alert_message TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
