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
-- Transformers Series
('Optimus Prime',     'Transformers', 'adult', 'male',   'path/to/optimus.jpg'),
('Bumblebee',         'Transformers', 'adult', 'male',   'path/to/bumblebee.jpg'),
('Megatron',          'Transformers', 'adult', 'male',   'path/to/megatron.jpg'),
('Starscream',        'Transformers', 'adult', 'male',   'path/to/starscream.jpg'),

-- Naruto Series
('Naruto Uzumaki',    'Naruto',       'teen',  'male',   'path/to/naruto.jpg'),
('Sasuke Uchiha',     'Naruto',       'teen',  'male',   'path/to/sasuke.jpg'),
('Sakura Haruno',     'Naruto',       'teen',  'female', 'path/to/sakura.jpg'),
('Kakashi Hatake',    'Naruto',       'adult', 'male',   'path/to/kakashi.jpg'),

-- Breaking Bad Series
('Walter White "Heisenberg"', 'Breaking Bad', 'adult', 'male', 'path/to/heisenberg.jpg'),
('Jesse Pinkman',      'Breaking Bad', 'adult', 'male',   'path/to/jesse.jpg'),
('Saul Goodman',       'Breaking Bad', 'adult', 'male',   'path/to/saul.jpg'),
('Gustavo Fring',      'Breaking Bad', 'adult', 'male',   'path/to/gustavo.jpg'),

-- John Wick Series
('John Wick',         'John Wick',    'adult', 'male',   'path/to/johnwick.jpg'),
('Viggo Tarasov',     'John Wick',    'adult', 'male',   'path/to/viggo.jpg'),
('Santino DAntonio', 'John Wick',   'adult', 'male',   'path/to/santino.jpg'),
('Winston',           'John Wick',    'adult', 'male',   'path/to/winston.jpg'),

-- Wall-E Series
('Wall-E',            'Wall-E',       'other', 'other',  'path/to/walle.jpg'),
('EVE',               'Wall-E',       'other', 'female', 'path/to/eve.jpg'),
('M-O',               'Wall-E',       'other', 'other',  'path/to/mo.jpg'),
('Auto',              'Wall-E',       'adult', 'male',   'path/to/auto.jpg'),

-- Cars Series
('Lightning McQueen', 'Cars',         'adult', 'male',   'path/to/mcqueen.jpg'),
('Mater',             'Cars',         'adult', 'male',   'path/to/mater.jpg'),
('Sally Carrera',     'Cars',         'adult', 'female', 'path/to/sally.jpg'),
('Doc Hudson',        'Cars',         'adult', 'male',   'path/to/dochudson.jpg'),

-- Vocaloid Series
('Hatsune Miku',      'Vocaloid',     'teen',  'female', 'path/to/miku.jpg'),
('Kagamine Rin',      'Vocaloid',     'teen',  'female', 'path/to/rin.jpg'),
('Kagamine Len',      'Vocaloid',     'teen',  'male',   'path/to/len.jpg'),
('Megurine Luka',     'Vocaloid',     'adult', 'female', 'path/to/luka.jpg'),

-- Hunter x Hunter Series
('Gon Freecss',       'Hunter x Hunter', 'kid',  'male',   'path/to/gon.jpg'),
('Killua Zoldyck',    'Hunter x Hunter', 'kid',  'male',   'path/to/killua.jpg'),
('Kurapika',          'Hunter x Hunter', 'teen', 'male',   'path/to/kurapika.jpg'),
('Leorio Paradinight','Hunter x Hunter', 'adult','male',   'path/to/leorio.jpg');

