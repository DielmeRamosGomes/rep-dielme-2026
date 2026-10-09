import random

lista = [random.randint(1, 100) for _ in range(10)]
maior = lista[0]
menor = maior
for posicao in range(10):
    if lista[posicao] > maior:
        maior = lista[posicao]
    if lista[posicao] < menor:
        menor = lista[posicao]
         
print(f"Lista = {lista}")
print(f"Maior = {maior}")
print(f"Menor = {menor}")
