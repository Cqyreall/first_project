DROP TABLE IF EXISTS competitions;
DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS teams;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS games;


CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE teams(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    points INT
);

CREATE TABLE players(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    team_id INT REFERENCES teams(id),
    goals INT,
    assists INT,
    yellow_cards INT,
    red_cards INT
);

CREATE TABLE games(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    home_team_goals INT,
    away_team_goals INT
);

CREATE TABLE competitions(
    id SERIAL PRIMARY KEY,
    team_id INT REFERENCES teams(id),
    game_id INT REFERENCES games(id)
);