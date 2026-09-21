import random

def im_matriz1(matriz1):
    dim_linha = len(matriz1)
    dim_coluna = len(matriz1[0])
    for lin in range(dim_linha):
        for col in range(dim_coluna):
            print(matriz1[lin][col], end=" ")
        print()
matriz1 = [[random.randint(1,10) for col in range(3)] for lin in range(3)]
print("matriz1:",matriz1)

def im_matriz2(matriz2):
    dim_linha = len(matriz2)
    dim_coluna = len(matriz2[0])
    for lin in range(dim_linha):
        for col in range(dim_coluna):
            print(matriz2[lin][col], end=" ")
        print()
matriz2 = [[random.randint(1,10) for col in range(3)] for lin in range(3)]
print("matriz2:",matriz2)

soma = matriz1
total = matriz2
total += soma
print(f"soma é:",total)