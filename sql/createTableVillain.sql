use game_rpg;

CREATE TABLE IF NOT EXISTS villains (
    id INT AUTO_INCREMENT PRIMARY KEY,
    vilName VARCHAR (50) NOT NULL,
    life VARCHAR (30) NOT NULL,
    strength INT,
    defense INT,
    speed INT,
    accuracy INT
)