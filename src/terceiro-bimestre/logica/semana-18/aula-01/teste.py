import random

dim_linha = int(input("Digite a dimensão: "))
dim_coluna = dim_linha

matriz1 = [[random.randint(1, 10) for coluna in range(dim_coluna)] for linha in range(dim_linha)]
matriz2 = [[random.randint(1, 10) for coluna in range(dim_coluna)] for linha in range(dim_linha)]
matriz3 = [[0 for coluna in range(dim_coluna)] for linha in range(dim_linha)]

def imprime_matriz(matriz):
    dim_linha = len(matriz)
    dim_coluna = len(matriz[0])
    for linha in range(dim_linha):
        for coluna in range(dim_coluna):
            print(matriz[linha][coluna], end=" ")
        print()

def soma_matriz(matriz1, matriz2, matriz3):
    dim_linha = len(matriz3)
    dim_coluna = len(matriz3[0])
    for linha in range(dim_linha):
        for coluna in range(dim_coluna):
            matriz3[linha][coluna] = matriz1[linha][coluna] + matriz2[linha][coluna]
    return matriz3

print("Matriz 1")
imprime_matriz(matriz1)
print()
print("Matriz 2")
imprime_matriz(matriz2)
print()
print("Matriz 3- Soma")
matriz3 = soma_matriz(matriz1, matriz2, matriz3)
imprime_matriz(matriz3)
