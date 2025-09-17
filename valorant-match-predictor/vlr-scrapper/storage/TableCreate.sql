CREATE TABLE IF NOT EXISTS teams (
    team_id SERIAL PRIMARY KEY,
    team_name VARCHAR(255) UNIQUE NOT NULL,
    region VARCHAR(100),
    country VARCHAR(100),
    team_url TEXT
);

CREATE TABLE IF NOT EXISTS players (
    player_id SERIAL PRIMARY KEY,
    team_id INT REFERENCES teams(team_id) ON DELETE CASCADE, 
    ign VARCHAR(100) UNIQUE NOT NULL,
    full_name VARCHAR(255),
    role_ VARCHAR(100),
    profile_url TEXT
);
ALTER TABLE players
ADD CONSTRAINT unique_ign UNIQUE (ign);

CREATE TABLE IF NOT EXISTS staff (
    staff_id SERIAL PRIMARY KEY,
    team_id INT REFERENCES teams(team_id) ON DELETE CASCADE,
    ign VARCHAR(100) NOT NULL,
    full_name VARCHAR(255),
    role_ VARCHAR(100),
    profile_url TEXT
);
