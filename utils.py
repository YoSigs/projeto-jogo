from time import sleep
import mysql.connector

def show_character(character):
    print("\n" + "="*30)
    print(f" FICHA DO PERSONAGEM ".center(30, "="))
    print("="*30)
    sleep(1)

    print(f"Nome      : {character['nickname']}")
    print(f"Classe    : {character['class']}")
    print("-"*30)
    sleep(1)
    print(f"Vida      : {character['life']}")
    sleep(0.5)
    print(f"Força     : {character['strength']}")
    sleep(0.5)
    print(f"Defesa    : {character['defense']}")
    sleep(0.5)
    print(f"Velocidade: {character['speed']}")
    sleep(0.5)
    print(f"Precisão  : {character['accuracy']}")
    print("="*30 + "\n")

def show_villain(villain):
    print('='*30)
    print("STATUS DO VILÃO".center(30, '='))
    print('='*30)
    sleep(1)
    print(f"Nome      : {villain['vilName']}")
    sleep(1)
    print(f"Vida      : {villain['life']}")
    sleep(0.5)
    print(f"Força     : {villain['strength']}")
    sleep(0.5)
    print(f"Defesa    : {villain['defense']}")
    sleep(0.5)
    print(f"Velocidade: {villain['speed']}")
    sleep(0.5)
    print(f"Precisão  : {villain['accuracy']}")
    print('='*30 +  "\n")

def save_villain(villain):
    conn = connect()
    cursor = conn.cursor()

   

    sql = """
    INSERT INTO villains (vilName, life, strength, defense, speed, accuracy)
    VALUES (%s, %s, %s, %s, %s, %s)"""

    values = (
        villain["vilName"],
        villain["life"],
        villain["strength"],
        villain["defense"],
        villain["speed"],
        villain["accuracy"]
    )

    

    cursor.execute(sql, values)
    conn.commit()
    
    cursor.close()
    conn.close()
    
def run_sql_file(filenickname):
    conn = connect()
    cursor = conn.cursor()

    with open (filenickname, "r") as f:
        sql = f.read()

    statements = sql.split(";")
    
    for statement in statements:
        if statement.strip():
            cursor.execute(statement)

    conn.commit()
    cursor.close()
    conn.close()

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="game_rpg"
    )

def get_existing_character(cursor, nickname):
    cursor.execute("SELECT * FROM characters WHERE nickname = %s", (nickname,))
    return cursor.fetchone()