use game_rpg;

CREATE TABLE IF NOT EXISTS characters (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nickname VARCHAR(50) NOT NULL,
    class VARCHAR(30) NOT NULL UNIQUE,
    life INT,
    strength INT,
    defense INT,
    speed INT,
    accuracy INT
);