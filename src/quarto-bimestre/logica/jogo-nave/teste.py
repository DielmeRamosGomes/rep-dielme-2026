'''
Leia um numero inteiro pelo teclado, coloque esse numero na 
primeira posição de uma lista de 10 elementos, o próximo 
termo da sequencia é sempre o dobro do elemento que está na 
posição anterior, depois imprima a lista com os elementos.
Condição: O numero lido tem que ser menor ou igual a 100.
Condição: Utilizar estruturas de repetição
'''

'''
numero = int(input("Digite um número inteiro menor ou igual a 100: "))
while numero < 0 or numero > 100:
    numero = int(input("Número inválido. Digite um número inteiro menor ou igual a 100: "))
lista = []
lista.append(numero)
for i in range(1, 10):
    lista.append(lista[i-1] * 2)
        
print(f"Lista: {lista}")
'''

'''
Faça um programa que gera uma matriz de ordem 5x5 que tenha 
seus elementos números inteiros e que sejam gerados de forma 
aleatória, depois imprima essa matriz na tela.
'''
import random

matriz = [[random.randint(0, 10) for _ in range(5)] for _ in range(5)]

def imprime_matriz(matriz):
    dim_linha = len(matriz)
    dim_coluna = len(matriz[0])
    for linha in range(dim_linha):
        for coluna in range(dim_coluna):
            print(matriz[linha][coluna], end=" ")
        print()
    
print("Matriz 5x5:\n") 
imprime_matriz(matriz)

