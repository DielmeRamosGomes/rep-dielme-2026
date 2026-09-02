import random

while True:
    matriz = [[random.randint(1, 10) for coluna in range(3)] for linha in range(3)]
    dim_linha = len(matriz)
    dim_coluna = len(matriz[0])
    
    print("Matriz gerada aleatoriamente: \n")
    for linha in range(dim_linha):
        for coluna in range(dim_coluna):
            print(matriz[linha][coluna], end=" ")
        print()
    continua = input("\nDeseja gerar outra matriz? [s, n]: ").lower()
    if continua == "n" or continua == "nao":
        break
    