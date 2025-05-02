DROP DATABASE IF EXISTS character_arena;
CREATE DATABASE character_arena CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE character_arena;

CREATE TABLE characters (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100)    NOT NULL,
    series VARCHAR(100)  NOT NULL,
    age ENUM('kid','teen','adult','other') NOT NULL,
    gender ENUM('male','female','other') NOT NULL,
    picture VARCHAR(255) NOT NULL
);

-- example datacharacters
INSERT INTO characters (name, series, age, gender, picture) VALUES
('Optimus Prime',    'Transformers', 'adult',  'male',   'path/to/optimus.jpg'),
('Naruto',           'Naruto',       'teen',   'male',   'path/to/naruto.jpg'),
('Heisenberg',       'Breaking Bad', 'adult',  'male',   'path/to/heisenberg.jpg'),
('John Wick',        'John Wick',    'adult',  'male',   'path/to/johnwick.jpg'),
('Wall-E',           'Wall-E',       'other',  'other',  'path/to/walle.jpg'),
('Lightning McQueen','Cars',         'adult',  'male',   'path/to/mcqueen.jpg'),
('Hatsune Miku',     'Vocaloid',     'teen',   'female', 'path/to/miku.jpg'),
('Gon',              'Hunter x Hunter','kid',  'male',   'path/to/gon.jpg');

