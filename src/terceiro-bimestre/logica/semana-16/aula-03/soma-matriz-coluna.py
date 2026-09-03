import random

def imprime_matriz(matriz):
    dim_linha = len(matriz)
    dim_coluna = len(matriz[0])
    for linha in range(dim_linha):
        for coluna in range(dim_coluna):
            print(matriz[linha][coluna], end=" ")
        print()

while True:
    dim_linha = int(input("Digite a linha: "))
    dim_coluna = int(input("Digite a coluna: "))
    matriz = [[random.randint(1, 10) for coluna in range(dim_coluna)] for linha in range(dim_linha)]
    imprime_matriz(matriz)
    opcao = int(input("\nDigite o número da coluna para soma: "))
    soma = 0
    if 0 <= opcao < dim_coluna:
        for linha in range(dim_linha):
            soma += matriz[linha][opcao]
        print(f"A soma da coluna {opcao} é: {soma}") 
    else:
        print("Opção inválida. Tente novamente.")
        
    continua = input("Deseja continuar? (s/n): ").lower()
    if continua == 'n':
        break








