import random

matriz1 = [[random.randint(1, 10) for coluna in range(3)] for linha in range(3)]
matriz2 = [[random.randint(1, 10) for coluna in range(3)] for linha in range(3)]
matriz3 = [[0 for coluna in range(3)] for linha in range(3)]

for linha in range(3):
    for coluna in range(3):
        matriz3[linha][coluna] = matriz1[linha][coluna] + matriz2[linha][coluna]

def imprimi_matriz(matriz):
    for linha in range(3):
        for coluna in range(3):
            print(matriz[linha][coluna], end=" ")
        print()
  
print("Matriz 1")      
imprimi_matriz(matriz1)
print("------------------------------------------")

print("Matriz 2")
imprimi_matriz(matriz2)
print("------------------------------------------")

print("Matriz 3 - Resultado da soma")
imprimi_matriz(matriz3)