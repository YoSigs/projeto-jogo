from utils import connect, save_villain
from villains import random_villain 
from time import sleep

class Battle:
    def __init__(self):
        self.conn = connect()
        self.cursor = self.conn.cursor()

    def get_villain(self, villain_id = 1):
        self.cursor.execute("SELECT * FROM villains where id = %s", (villain_id,))
        villainResults = self.cursor.fetchone()
        
        return{
            "id": villainResults[0],
            "name": villainResults[1],
            "life": int(villainResults[2]),
            "speed": int(villainResults[5]),
            "strength": int(villainResults[3]),
            "defense": int(villainResults[4]),
            "accuracy": int(villainResults[6])
        }

    def get_character(self, character_id = 1):
        self.cursor.execute("SELECT * FROM characters where id = %s", (character_id,))
        characterResults = self.cursor.fetchone()
        
        return{
            "id": characterResults[0],
            "name": characterResults[1],
            "life": int(characterResults [3]),
            "speed": int(characterResults[6]),
            "strength": int(characterResults[4]),
            "defense": int(characterResults[5]),
            "accuracy": int(characterResults[7])
        }

    def delete_villain(self, villain_id):
        self.cursor.execute("DELETE FROM villains WHERE id = %s", (villain_id,))
        self.conn.commit()

    def update_character_life(self, new_life, character_id):
        self.cursor.execute("UPDATE characters SET life = %s WHERE id = %s", (new_life, character_id))
        self.conn.commit()

    def handle_defeat(self, character):
        conn = connect()
        cursor = conn.cursor()

        character["life"] = 50
        #tira 5% da força
        character["strength"] -= character["strength"] *5/100

        cursor.execute("""
            UPDATE characters
            SET life = %s, strength = %s
            WHERE id = %s
        """, (character["life"], character["strength"], character["id"]))

        conn.commit()
        cursor.close()
        conn.close()

        print(f"Seu personagem foi derrotado! Sua vida foi restaurada parcialmente, mas perdeu um pouco de força.")
            


    def start_battle(self, character_id=1, villain_id=1):
        character = self.get_character(character_id)
        villain = self.get_villain(villain_id)

        print(f"{character['name']} VS {villain['name']}".center(30, "="))
        sleep(1)
        print(f"{character['name']} (Vida: {character['life']}) | {villain['name']} (Vida: {villain['life']})")
        sleep(1)

        #compara a velocidade
        if character["speed"] > villain["speed"]:
            first, second = character, villain
        else:
            first, second = villain, character

        print(f"\n{first['name']} ataca primeiro!\n")
        sleep(1)

        #combate
        round_num = 1
        while character["life"] > 0 and villain["life"] > 0:
            print(f"  ROUND: {round_num}  ".center(30,"="))
            damage = max(first["strength"] - second["defense"], 1)
            second["life"] -= damage
            sleep(1)
            print(f"{first['name']} ataca com {first['strength']} e causa {damage} de dano!")
            if second["life"] <= 0:
                second["life"] = 0
            sleep(1)
            print(f"{second['name']} agora tem {second['life']} de vida\n")
            sleep(1)

            if second["life"] <= 0:
                print(f"\n💀 {second['name']} foi derrotado!")
                break

            # troca o turno
            first, second = second, first
            round_num += 1
            sleep(1)
        print("\n🏆 FIM DA BATALHA 🏆")
        if character["life"] > 0:
            print(f"✅ {character['name']} venceu!")
            self.update_character_life(character["life"], character["id"])
            self.delete_villain(villain["id"])
            
        else:
            print(f"❌ {villain['name']} venceu!")
            self.handle_defeat(character)
            