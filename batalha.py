from inimigo import inimigo
from status import status_myself
from time import sleep


start = 0

start = int(input('Digite "1" para começar a batalha: '))
if start == 1:
    while inimigo['Vida'] or status_myself['Vida'] > 0:
        if inimigo['Velocidade'] > status_myself['Velocidade']:
            primeiro = inimigo
            segundo = status_myself
        else:
            primeiro = status_myself
            segundo = inimigo

    