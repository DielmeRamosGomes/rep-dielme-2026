import random

def imprime_matriz(matriz):
    dim_linha = len(matriz)
    dim_coluna = len(matriz[0])
    for linha in range(dim_linha):
        for coluna in range(dim_coluna):
            print(matriz[linha][coluna], end=" ")
        print()

matriz = [[random.randint(1, 10) for coluna in range(3)] for linha in range(3)]
imprime_matriz(matriz)
soma = 0
opcao = int(input("Digita a linha [0, 1, 2]: "))
match opcao:
    case 0:
        linha = matriz[0]
        for elemento in linha:
            soma += elemento
        print(f"Soma da linha 0 = {soma}")
    case 1:
        linha = matriz[1]
        for elemento in linha:
            soma += elemento
        print(f"Soma da linha 1 = {soma}")
    case 2:
        linha = matriz[2]
        for elemento in linha:
            soma += elemento
        print(f"Soma da linha 2 = {soma}")
    case _:
        print("Opção inválida")  