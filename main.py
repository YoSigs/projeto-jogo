from battle import Battle
from classes import choose_class, random_class
from utils import show_character, show_villain, run_sql_file, connect, save_villain, get_existing_character
from villains import random_villain



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

def main():
    conn = connect()
    cursor = conn.cursor()

    run_sql_file("sql/criaTabela.sql")
    run_sql_file("sql/createTableVillain.sql")

    print("=".center(40, "="))
    print(" SEJA BEM-VINDO AO RPG ".center(40, "="))
    print("=".center(40, "="))

    nickname = input("\nDigite seu nickname: ")

    existing = get_existing_character(cursor, nickname)

    if existing:
        print(f'Olá {nickname}, seu personagem foi encontrado!\n')
        character = {
            "id": existing[0],
            "nickname": existing[1],
            "life": existing[3],
            "speed": existing[6],
            "strength": existing[4],
            "defense": existing[5],
            "accuracy": existing[7],
            "class": existing[2]
        }
        show_character(character)
    else:

        print("\nPara começar o jogo você tem duas opções:")
        escolha = input("[1] Montar sua classe | [2] Sortear uma classe \nEscolha: ")

        if escolha == '1':
            character = choose_class()
        else:
            character = random_class()

        character["nickname"] = nickname


        show_character(character)

        save_character(character)

    villain = random_villain()
    save_villain(villain)

    b = Battle()

    character = b.get_character()
    villain = b.get_villain()

    b.start_battle()

if __name__ == "__main__":
    run_sql_file("sql/criaBanco.sql")
    main()