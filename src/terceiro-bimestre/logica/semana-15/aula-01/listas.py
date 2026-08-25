'''
lista = [7.5, 8.0, 6.5, 9.0, 7.0]
print(lista)
'''
'''
numeros = []
numeros.append(1)
numeros.append(2)
numeros.append(3)
numeros.append(4)
numeros.append(5)
print(numeros)
'''
print("Digite 5 números:")
numeros = []
for i in range(5):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)
print(numeros)
