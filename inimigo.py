from utils import connect

conn = connect()
cursor = conn.cursor()
cursor.execute("SELECT DATABASE();")
print("Banco conectado:", cursor.fetchone())
cursor.execute("SELECT * FROM villains;")
print(cursor.fetchall())
cursor.close()
conn.close()

