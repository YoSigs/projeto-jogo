import random
from utils import connect

CLASSES = {
    "Mago": {
        "life": (120, 200),
        "strength": (25, 50),
        "defense": (20, 40),
        "speed": (40, 80),
        "accuracy": (60, 90),
    },
    "Cavaleiro": {
        "life": (200, 400),
        "strength": (40, 60),
        "defense": (50, 70),
        "speed": (20, 40),
        "accuracy": (30, 60),
    },
    "Druida": {
        "life": (150, 300),
        "strength": (30, 50),
        "defense": (25, 50),
        "speed": (30, 70),
        "accuracy": (40, 80),
    },
    "Fada": {
        "life": (75, 150),
        "strength": (15, 30),
        "defense": (20, 40),
        "speed": (50, 100),
        "accuracy": (70, 100),
    },
    "Barbaro": {
        "life": (200, 400),
        "strength": (50, 80),
        "defense": (20, 40),
        "speed": (30, 50),
        "accuracy": (20, 50),
    }
}

def choose_class():
    option = input("[1] Mago | [2] Cavaleiro | [3] Druida | [4] Fada | [5] Barbaro\nEscolha uma classe: ")
    mapping = {
        "1": "Mago",
        "2": "Cavaleiro",
        "3": "Druida",
        "4": "Fada",
        "5": "Barbaro"
    }

    chosen = mapping.get(option, "mago")
    attributes = CLASSES[chosen]

    return {
        "class": chosen,
        "life": random.randint(*attributes["life"]),
        "strength": random.randint(*attributes["strength"]),
        "defense": random.randint(*attributes["defense"]),
        "speed": random.randint(*attributes["speed"]),
        "accuracy": random.randint(*attributes["accuracy"])
    }

def random_class():
    chosen = random.choice(list(CLASSES.keys()))
    attributes = CLASSES[chosen]

    return {
        "class": chosen,
        "life": random.randint(*attributes["life"]),
        "strength": random.randint(*attributes["strength"]),
        "defense": random.randint(*attributes["defense"]),
        "speed": random.randint(*attributes["speed"]),
        "accuracy": random.randint(*attributes["accuracy"])
    }

def save_character(character):
    conn = connect()
    cursor = conn.cursor()

    sql = """
        INSERT INTO characters (nickname, class, life, strength, defense, speed, accuracy)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
    values = (
        character["nickname"],
        character["class"],
        character["life"],
        character["strength"],
        character["defense"],
        character["speed"],
        character["accuracy"]
    )

    cursor.execute(sql, values)
    conn.commit()

    character_id = cursor.lastrowid
    cursor.close()
    conn.close()

    return character_id