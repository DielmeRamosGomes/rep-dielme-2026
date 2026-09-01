import random
while True:
    lista = [random.randint(1, 10) for i in range(3)]
    if lista[0] == lista[1] == lista[2]:
        print(lista)
        print(f"Parabéns! Você ganhou R$50.000,00 reais")
        break
    else:
        print(lista)
        print(f"Você perdeu tente novamente!")
    continua = input("Deseja continuar? [s, n]: ").lower()
    if continua == 'n':
        print("Obrigado por jogar!")
        break