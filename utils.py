def exibir_ficha(personagem):
    print("\n" + "="*30)
    print(f" FICHA DO PERSONAGEM ".center(30, "="))
    print("="*30)

    print(f"Nome      : {personagem['nome']}")
    print(f"Classe    : {personagem['classe']}")
    print("-"*30)
    print(f"Vida      : {personagem['vida']}")
    print(f"Força     : {personagem['força']}")
    print(f"Defesa    : {personagem['defesa']}")
    print(f"Velocidade: {personagem['velocidade']}")
    print(f"Precisão  : {personagem['precisão']}")
    print("="*30 + "\n")
