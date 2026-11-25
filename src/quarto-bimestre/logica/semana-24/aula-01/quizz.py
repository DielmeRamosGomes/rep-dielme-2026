def pergunta_quizz():
    pontos = 0
    pergunta = input("Qual o maior oceano?: ").lower()
    if pergunta == "pacífico":
        pontos += 1
        print("Acertou!")
        print(f"Pontuação atual: {pontos}")
    else:
        print("Errou!")
        print(f"Pontuação atual: {pontos}")
    pergunta = input("Qual a capital dos USA?: ").lower()
    if pergunta == "washington dc":
        pontos += 1
        print("Acertou!")
        print(f"Pontuação atual: {pontos}")
    else:
        print("Errou!")
        print(f"Pontuação atual: {pontos}")

pergunta_quizz()



