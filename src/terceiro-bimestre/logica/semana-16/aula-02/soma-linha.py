import random

def imprime_matriz(matriz):
    dim_linha = len(matriz)
    dim_coluna = len(matriz[0])
    for linha in range(dim_linha):
        for coluna in range(dim_coluna):
            print(matriz[linha][coluna], end=" ")
        print()

matriz = [[random.randint(1, 10) for j in range(3)] for i in range(3)]
imprime_matriz(matriz)

opcao = int(input("\nDigite 0, 1 ou 2 para somar uma linha específica: "))
soma = 0
match opcao:
    case 0:
        linha = matriz[0]
        for elemento in linha:
            soma += elemento
        print(f"A soma da linha 0 é: {soma}")
    case 1:
        linha = matriz[1]
        for elemento in linha:
            soma += elemento
        print(f"A soma da linha 1 é: {soma}")
    case 2:
        linha = matriz[2]
        for elemento in linha:
            soma += elemento
        print(f"A soma da linha 2 é: {soma}")
    case _:
        print("Opção inválida. Digite 0, 1 ou 2.")

