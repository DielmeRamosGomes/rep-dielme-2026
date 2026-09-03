import random

dim_linha = int(input("Digite a dimensão da linha da matriz: "))
dim_coluna = int(input("Digite a dimensão da coluna da matriz: "))

def imprime_matriz(matriz):
    dim_linha = len(matriz)
    dim_coluna = len(matriz[0])
    for linha in range(dim_linha):
        for coluna in range(dim_coluna):
            print(matriz[linha][coluna], end=" ")
        print()
        
matriz = [[random.randint(1, 10) for coluna in range(dim_coluna)] for linha in range(dim_linha)]
imprime_matriz(matriz)
