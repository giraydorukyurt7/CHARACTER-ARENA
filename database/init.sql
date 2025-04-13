CREATE DATABASE fandom_game;

USE fandom_game;

CREATE TABLE characters (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    series VARCHAR(100),
    image_url TEXT
);
