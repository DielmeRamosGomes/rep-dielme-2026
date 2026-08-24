#lista  = [1, 2, 3, 4, 5]

'''
for i in range(0, len(lista)):
    print(lista[i])
'''

'''
for i in range(len(lista)):
    print(lista[i])
'''

'''
for i in range(len(lista)-1, -1, -1):
    print(lista[i])
'''
'''
frutas = ["Maçã", "Banana", "Limão"]
for fruta in frutas:
    print(fruta)
'''

'''
frutas = ["maçã", "banana", "uva"]
for posicao, fruta in enumerate(frutas):
    print(posicao, fruta)
''' 

'''
nomes = ["Ana", "Bia", "Carla"]
idades = [20, 25, 18]
for nome, idade in zip(nomes, idades):
    print(nome, idade)
'''

'''
pessoa = {"nome": "João", "idade": 30}
for chave, valor in pessoa.items():
    print(chave, valor)
'''

'''
for i in range(6):
    for j in range(6):
        print("*", end="")
    print()
'''

'''
raiz_quadrada = [x**2 for x in range(6)]  
print(raiz_quadrada)      
'''    

'''
numeros = [i for i in range(1, 11)]
print(numeros)
numeros_pares = [x for x in numeros if x % 2 == 0]
print(numeros_pares)
'''
 
