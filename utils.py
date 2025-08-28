from time import sleep


def exibir_ficha(personagem):
    print("\n" + "="*30)
    print(f" FICHA DO PERSONAGEM ".center(30, "="))
    print("="*30)
    sleep(1)

    print(f"Nome      : {personagem['nome']}")
    print(f"Classe    : {personagem['classe']}")
    print("-"*30)
    sleep(1)
    print(f"Vida      : {personagem['vida']}")
    sleep(0.5)
    print(f"Força     : {personagem['força']}")
    sleep(0.5)
    print(f"Defesa    : {personagem['defesa']}")
    sleep(0.5)
    print(f"Velocidade: {personagem['velocidade']}")
    sleep(0.5)
    print(f"Precisão  : {personagem['precisão']}")
    print("="*30 + "\n")


def mostra_vilao(vilao):
    print('='*30)
    print("STATUS DO VILAO".center(30, '='))
    print('='*30)
    sleep(1)
    print(f"Nome      : {vilao['nome']}")
    sleep(1)
    print(f"Vida      : {vilao['vida']}")
    sleep(0.5)
    print(f"Força     : {vilao['força']}")
    sleep(0.5)
    print(f"Defesa    : {vilao['defesa']}")
    sleep(0.5)
    print(f"Velocidade: {vilao['velocidade']}")
    sleep(0.5)
    print(f"Precisão  : {vilao['precisão']}")
    

