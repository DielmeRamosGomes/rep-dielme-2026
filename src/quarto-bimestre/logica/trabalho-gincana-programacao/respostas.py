'''
1 - Crie um programa que receba 10 números aleatórios
inteiros no intervalo entre 1 e 100 e armazene-os em uma 
lista. Ao final, exiba:
A lista com os numeros
O maior número
O menor número
Exemplo:
Saída:
lista = 5 8 1 9 4 7 2 6 3 10
Maior = 10
Menor = 1
'''

'''
import random
numeros = [random.randint(1,100) for _ in range(10)]
maior = numeros[0]
menor = maior
for posicao in range(1, len(numeros)):   
    if numeros[posicao] > maior:
        maior = numeros[posicao]
    if numeros[posicao] < menor:
        menor = numeros[posicao]
print(f"Lista = {numeros}")
print(f"Maior: {maior}")
print(f"Menor: {menor}")
'''

'''
2 - Crie um programa que receba 15 números aleatórios no 
intervalo entre 1 e 100 e armazene-os em uma lista.
Mostre:
A quantidade de pares
Mostre os pares em uma lista chamada lista_pares
Exemplo:
Saída:
Lista = [38, 24, 85, 44, 89, 98, 94, 16, 88, 35, 71, 63, 16, 29, 85]
Quantidade de pares = 8
Lista de pares = [38, 24, 44, 98, 94, 16, 88, 16]
'''
import random
numeros = [random.randint(1,100) for _ in range(15)]
cont_pares = 0
lista_pares = []
for posicao in range(len(numeros)):
    if numeros[posicao] % 2 == 0:
        cont_pares += 1
        lista_pares.append(numeros[posicao])
print(f"Lista = {numeros}")
print(f"Quantidade de pares = {cont_pares}")
print(f"Lista de pares = {lista_pares}")



