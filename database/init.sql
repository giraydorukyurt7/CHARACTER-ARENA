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

INSERT INTO characters (name, series, age, gender, picture) VALUES
-- Transformers Series (8)
('Optimus Prime', 'Transformers', 'adult', 'male', 'images/transformers/optimus_prime.jpg'),
('Bumblebee', 'Transformers', 'adult', 'male', 'images/transformers/bumblebee.jpg'),
('Megatron', 'Transformers', 'adult', 'male', 'images/transformers/megatron.jpg'),
('Starscream', 'Transformers', 'adult', 'male', 'images/transformers/starscream.jpg'),
('Ratchet', 'Transformers', 'adult', 'male', 'images/transformers/ratchet.jpg'),
('Ironhide', 'Transformers', 'adult', 'male', 'images/transformers/ironhide.jpg'),
('Soundwave', 'Transformers', 'adult', 'male', 'images/transformers/soundwave.jpg'),
('Arcee', 'Transformers', 'adult', 'female', 'images/transformers/arcee.jpg'),

-- Naruto Series (8)
('Naruto Uzumaki', 'Naruto', 'teen', 'male', 'images/naruto/naruto_uzumaki.jpg'),
('Sasuke Uchiha', 'Naruto', 'teen', 'male', 'images/naruto/sasuke_uchiha.jpg'),
('Sakura Haruno', 'Naruto', 'teen', 'female', 'images/naruto/sakura_haruno.jpg'),
('Kakashi Hatake', 'Naruto', 'adult', 'male', 'images/naruto/kakashi_hatake.jpg'),
('Hinata Hyuga', 'Naruto', 'teen', 'female', 'images/naruto/hinata_hyuga.jpg'),
('Shikamaru Nara', 'Naruto', 'teen', 'male', 'images/naruto/shikamaru_nara.jpg'),
('Gaara', 'Naruto', 'teen', 'male', 'images/naruto/gaara.jpg'),
('Jiraiya', 'Naruto', 'adult', 'male', 'images/naruto/jiraiya.jpg'),

-- Breaking Bad Series (8)
('Walter White "Heisenberg"', 'Breaking Bad', 'adult', 'male', 'images/breaking_bad/walter_white.jpg'),
('Jesse Pinkman', 'Breaking Bad', 'adult', 'male', 'images/breaking_bad/jesse_pinkman.jpg'),
('Saul Goodman', 'Breaking Bad', 'adult', 'male', 'images/breaking_bad/saul_goodman.jpg'),
('Gustavo Fring', 'Breaking Bad', 'adult', 'male', 'images/breaking_bad/gustavo_fring.jpg'),
('Skyler White', 'Breaking Bad', 'adult', 'female', 'images/breaking_bad/skyler_white.jpg'),
('Hank Schrader', 'Breaking Bad', 'adult', 'male', 'images/breaking_bad/hank_schrader.jpg'),
('Mike Ehrmantraut', 'Breaking Bad', 'adult', 'male', 'images/breaking_bad/mike_ehrmantraut.jpg'),
('Lydia Rodarte-Quayle', 'Breaking Bad', 'adult', 'female', 'images/breaking_bad/lydia_rodarte_quayle.jpg'),

-- John Wick Series (8)
('John Wick', 'John Wick', 'adult', 'male', 'images/john_wick/john_wick.jpg'),
('Viggo Tarasov', 'John Wick', 'adult', 'male', 'images/john_wick/viggo_tarasov.jpg'),
('Santino DAntonio', 'John Wick', 'adult', 'male', 'images/john_wick/santino_dantonio.jpg'),
('Winston', 'John Wick', 'adult', 'male', 'images/john_wick/winston.jpg'),
('Charon', 'John Wick', 'adult', 'male', 'images/john_wick/charon.jpg'),
('The Bowery King', 'John Wick', 'adult', 'male', 'images/john_wick/bowery_king.jpg'),
('Ares', 'John Wick', 'adult', 'female', 'images/john_wick/ares.jpg'),
('Cassian', 'John Wick', 'adult', 'male', 'images/john_wick/cassian.jpg'),

-- Wall-E Series (8)
('Wall-E', 'Wall-E', 'other', 'other', 'images/wall_e/wall_e.jpg'),
('EVE', 'Wall-E', 'other', 'female', 'images/wall_e/eve.jpg'),
('M-O', 'Wall-E', 'other', 'other', 'images/wall_e/mo.jpg'),
('Auto', 'Wall-E', 'adult', 'male', 'images/wall_e/auto.jpg'),
('Captain B. McCrea', 'Wall-E', 'adult', 'male', 'images/wall_e/captain_mccrea.jpg'),
('Shelby Forthright', 'Wall-E', 'adult', 'male', 'images/wall_e/shelby_forthright.jpg'),
('GO-4', 'Wall-E', 'other', 'male', 'images/wall_e/go4.jpg'),
('John', 'Wall-E', 'adult', 'male', 'images/wall_e/john.jpg'),

-- Cars Series (8)
('Lightning McQueen', 'Cars', 'adult', 'male', 'images/cars/lightning_mcqueen.jpg'),
('Mater', 'Cars', 'adult', 'male', 'images/cars/mater.jpg'),
('Sally Carrera', 'Cars', 'adult', 'female', 'images/cars/sally_carrera.jpg'),
('Doc Hudson', 'Cars', 'adult', 'male', 'images/cars/doc_hudson.jpg'),
('Luigi', 'Cars', 'adult', 'male', 'images/cars/luigi.jpg'),
('Guido', 'Cars', 'adult', 'male', 'images/cars/guido.jpg'),
('Ramone', 'Cars', 'adult', 'male', 'images/cars/ramone.jpg'),
('Sheriff', 'Cars', 'adult', 'male', 'images/cars/sheriff.jpg'),

-- Vocaloid Series (8)
('Hatsune Miku', 'Vocaloid', 'teen', 'female', 'images/vocaloid/hatsune_miku.jpg'),
('Kagamine Rin', 'Vocaloid', 'teen', 'female', 'images/vocaloid/kagamine_rin.jpg'),
('Kagamine Len', 'Vocaloid', 'teen', 'male', 'images/vocaloid/kagamine_len.jpg'),
('Megurine Luka', 'Vocaloid', 'adult', 'female', 'images/vocaloid/megurine_luka.jpg'),
('KAITO', 'Vocaloid', 'adult', 'male', 'images/vocaloid/kaito.jpg'),
('MEIKO', 'Vocaloid', 'adult', 'female', 'images/vocaloid/meiko.jpg'),
('GUMI', 'Vocaloid', 'teen', 'female', 'images/vocaloid/gumi.jpg'),
('IA', 'Vocaloid', 'teen', 'female', 'images/vocaloid/ia.jpg'),

-- Hunter X Hunter Series (8)
('Gon Freecss', 'Hunter X Hunter', 'kid', 'male', 'images/hunterxhunter/gon_freecss.jpg'),
('Killua Zoldyck', 'Hunter X Hunter', 'kid', 'male', 'images/hunterxhunter/killua_zoldyck.jpg'),
('Kurapika', 'Hunter X Hunter', 'teen', 'male', 'images/hunterxhunter/kurapika.jpg'),
('Leorio Paradinight', 'Hunter X Hunter', 'adult', 'male', 'images/hunterxhunter/leorio_paradinight.jpg'),
('Hisoka Morow', 'Hunter X Hunter', 'adult', 'male', 'images/hunterxhunter/hisoka_morow.jpg'),
('Chrollo Lucilfer', 'Hunter X Hunter', 'adult', 'male', 'images/hunterxhunter/chrollo_lucilfer.jpg'),
('Neferpitou', 'Hunter X Hunter', 'other', 'other', 'images/hunterxhunter/neferpitou.jpg'),
('Biscuit Krueger', 'Hunter X Hunter', 'adult', 'female', 'images/hunterxhunter/biscuit_krueger.jpg'),

-- House Series (8)
('Dr. Gregory House', 'House', 'adult', 'male', 'images/house/gregory_house.jpg'),
('Dr. James Wilson', 'House', 'adult', 'male', 'images/house/james_wilson.jpg'),
('Dr. Lisa Cuddy', 'House', 'adult', 'female', 'images/house/lisa_cuddy.jpg'),
('Dr. Eric Foreman', 'House', 'adult', 'male', 'images/house/eric_foreman.jpg'),
('Dr. Robert Chase', 'House', 'adult', 'male', 'images/house/robert_chase.jpg'),
('Dr. Allison Cameron', 'House', 'adult', 'female', 'images/house/allison_cameron.jpg'),
('Dr. Remy "Thirteen" Hadley', 'House', 'adult', 'female', 'images/house/remy_hadley.jpg'),
('Dr. Chris Taub', 'House', 'adult', 'male', 'images/house/chris_taub.jpg'),

-- Rick and Morty Series (8)
('Rick Sanchez', 'Rick and Morty', 'adult', 'male', 'images/rick_and_morty/rick_sanchez.jpg'),
('Morty Smith', 'Rick and Morty', 'teen', 'male', 'images/rick_and_morty/morty_smith.jpg'),
('Summer Smith', 'Rick and Morty', 'teen', 'female', 'images/rick_and_morty/summer_smith.jpg'),
('Beth Smith', 'Rick and Morty', 'adult', 'female', 'images/rick_and_morty/beth_smith.jpg'),
('Jerry Smith', 'Rick and Morty', 'adult', 'male', 'images/rick_and_morty/jerry_smith.jpg'),
('Mr. Meeseeks', 'Rick and Morty', 'other', 'male', 'images/rick_and_morty/mr_meeseeks.jpg'),
('Birdperson', 'Rick and Morty', 'adult', 'male', 'images/rick_and_morty/birdperson.jpg'),
('Squanchy', 'Rick and Morty', 'adult', 'male', 'images/rick_and_morty/squanchy.jpg');

