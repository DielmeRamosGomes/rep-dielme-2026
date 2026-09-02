import random

def imprime_matriz(matriz):
    dim_linha = len(matriz)
    dim_coluna = len(matriz[0])
    for linha in range(dim_linha):
        for coluna in range(dim_coluna):
            print(matriz[linha][coluna], end=" ")
    print()
    
while True:
    matriz = [[random.randint(1, 10) for coluna in range(3)] for linha in range(1)]
    if matriz[0][0] == matriz[0][1] == matriz[0][2]:
        imprime_matriz(matriz)
        print("Parabéns você ganhou!")
    else:
        imprime_matriz(matriz)
        print("Você perdeu tente outra vez!")
    continua = input("\nDeseja continuar?[s, n]: ").lower()
    if continua == "n":
        break




