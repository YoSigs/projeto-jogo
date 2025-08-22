from time import sleep
from classes import CLASSES
import random
from pymongo import MongoClient

def conectar():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["Jogo"]
    return db

print("="*30)
print(str("SEJA BEM VINDO").center(30))
print("="*30)

print("Para começar o jogo você tem duas opções")
MontOuSort = input('[1] Montar uma classe\n[2] Sortear uma classe\nEscolha uma: ')
print()
#Montar classe
if MontOuSort == '1':
    Classe = input('[1] Mago\n[2] Cavaleiro\n[3] Druida\n[4] Fada\n[5] Barbaro\nEscolha uma classe:')
    
    classes_opcoes = {
        '1': 'Mago',
        '2': 'Cavaleiro',
        '3': 'Druida',
        '4': 'Fada',
        '5': 'Barbaro'
    }

    classe_escolhida = classes_opcoes.get(Classe)

    if classe_escolhida:
        atributos = CLASSES[classe_escolhida]

        personagem = {
            'nome': input('Digite seu nome: '),
            'classe': classe_escolhida,
            'vida': random.randint(*atributos['vida']),
            'força': random.randint(*atributos['força']),
            'defesa': random.randint(*atributos['defesa']),
            'velocidade': random.randint(*atributos['velocidade']),
            'precisão': random.randint(*atributos['precisão'])
        }

        print('\n===FICHA DE PERSONAGEM===')
        for chave, valor in personagem.items():
            print(f'{chave}: {valor}')

elif MontOuSort == '2':
    
    classes_opcoes = ['Mago', 'Cavaleiro', 'Druida', 'Fada', 'Barbaro']

    classe_sorteada = random.choice(classes_opcoes)

    
    atributos = CLASSES[classe_sorteada]

    personagem = {
        'nome': input('Digite seu nome: '),
        'classe': classe_sorteada,
        'vida': random.randint(*atributos['vida']),
        'força': random.randint(*atributos['força']),
        'defesa': random.randint(*atributos['defesa']),
        'velocidade': random.randint(*atributos['velocidade']),
        'precisão': random.randint(*atributos['precisão'])
    }

    print('\n===FICHA DE PERSONAGEM===')
    for chave, valor in personagem.items():
        print(f'{chave}: {valor}')

db = conectar()
personagens = db["Personagens"]
personagens.insert_one(personagem)

print("Personagem adicionado ao BD")