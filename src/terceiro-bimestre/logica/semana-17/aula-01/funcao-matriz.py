import random

def cria_matriz(dim_linha, dim_coluna):
    matriz = [[random.randint(1, 10) for coluna in range(dim_coluna)] for linha in range(dim_linha)]
    return matriz

def imprime_matriz(matriz):
    dim_linha = len(matriz)
    dim_coluna = len(matriz[0])
    for linha in range(dim_linha):
        for coluna in range(dim_coluna):
            print(matriz[linha][coluna], end=" ")
        print()

matriz = cria_matriz(3, 3)
imprime_matriz(matriz)

