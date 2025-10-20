import random

VILLAINS = {
    "Goblin": {
        "life": (50, 200),
        "strength": (20, 50),
        "defense": (10, 30),
        "speed": (20, 25),
        "accuracy": (40, 50)
    },
    "Executor": {
        "life": (150, 300),
        "strength": (40, 70),
        "defense": (30, 50),
        "speed": (10, 30),
        "accuracy": (30, 60)
    }
}

def random_villain():
    chosen = random.choice(list(VILLAINS.keys()))
    attributes = VILLAINS[chosen]

    return {
        "vilName": chosen,
        "life": random.randint(*attributes["life"]),
        "strength": random.randint(*attributes["strength"]),
        "defense": random.randint(*attributes["defense"]),
        "speed": random.randint(*attributes["speed"]),
        "accuracy": random.randint(*attributes["accuracy"])
    }