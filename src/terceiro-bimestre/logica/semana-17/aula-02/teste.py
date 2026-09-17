import random

matriz = [[random.randint(1, 9) for coluna in range(5)] for linha in range(5)]

def imprime_matriz(matriz):
    dim_linha = len(matriz)
    dim_coluna = len(matriz[0])
    for linha in range(dim_linha):
        for coluna in range(dim_coluna):
            print(matriz[linha][coluna], end=" ")
        print()


def soma_linha(matriz, num_linha):
    dim_coluna = len(matriz[0])
    soma = 0
    for coluna in range(dim_coluna):
        soma += matriz[num_linha][coluna]
    return soma

imprime_matriz(matriz)
print()
soma = soma_linha(matriz, 0)
print(f"Soma da linha: {soma}")
