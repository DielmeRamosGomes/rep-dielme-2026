import random

while True:
    dim_linha = int(input("Digite a linha: "))
    dim_coluna = int(input("Digite a coluna: "))
    matriz = [[random.randint(1, 10) for coluna in range(dim_coluna)] for linha in range(dim_linha)]
    for linha in range(dim_linha):
        for coluna in range(dim_coluna):
            print(matriz[linha][coluna], end=" ")
        print()
    continua = input("Deseja continuar?[s, n]")
    if continua == "n":
        break





