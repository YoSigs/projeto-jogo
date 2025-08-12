from sorteio_da_classe import Classes
from random import choice, randint

choices = ["Mago", "Cavaleiro", "Barbaro",  "Druida", "Fada"]

classe = Classes.sortear_classe(choices)

print(f"Sua classe é {classe}")

status_myself = {}

if classe == "Mago":
    status_myself['Vida'] = randint(120, 200)
    status_myself['Força'] = randint(50, 80)
    status_myself['Defesa'] = randint(20, 40)
    status_myself['Velocidade'] = randint(40, 80)
    status_myself['Precisão'] = randint(50, 70)
elif classe == "Cavaleiro":
    status_myself['Vida'] = randint(200, 400)
    status_myself['Força'] = randint(70, 140)
    status_myself['Defesa'] = randint(35, 50)
    status_myself['Velocidade'] = randint(20, 60)
    status_myself['Precisão'] = randint(50, 80)
elif classe == "Druida":
    status_myself['Vida'] = randint(300, 500)
    status_myself['Força'] = randint(100, 150)
    status_myself['Defesa'] = randint(50, 80)
    status_myself['Velocidade'] = randint(40, 50)
    status_myself['Precisão'] = randint(20, 50)
elif classe == "Fada":
    status_myself['Vida'] = randint(75, 130)
    status_myself['Força'] = randint(50, 70)
    status_myself['Defesa'] = randint(10, 30)
    status_myself['Velocidade'] = randint(80, 100)
    status_myself['Precisão'] = randint(70, 100)
elif classe == 'Barbaro':
    status_myself['Vida'] = randint(250, 400)
    status_myself['Força'] = randint(150, 200)
    status_myself['Defesa'] = randint(50, 70)
    status_myself['Velocidade'] = randint(30, 50)
    status_myself['Precisão'] = randint(40, 70)

print()
print(f'''SEUS STATUS: 
      
Vida: {status_myself['Vida']}
Força: {status_myself['Força']}
Defesa: {status_myself['Defesa']}
Velocidade: {status_myself['Velocidade']}
Precisão: {status_myself["Precisão"]}''')
