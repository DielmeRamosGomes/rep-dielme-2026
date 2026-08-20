'''
index = 0
while index <= 10:
    print(index)
    index += 1
'''

'''
i  = 1
while i <= 10:
    if i == 5:
        break
    print(i)
    i = i + 1
'''



 
'''
i = 10
while i >= 0:
    print(i)
    i -= 1
else:
    print("Lançando foguete")
'''

'''
i = 0
while i <= 10: 
    if i % 2 != 0:
        i += 1
        continue
    print(i, end=" ")
    i += 1
'''  
   
while True:
    fruta = input("Digite o nome da fruta: ")
    print(f"Fruta: {fruta}")
    continua = input("Deseja continuar executando? [s, n]: ").lower()
    if (continua == "n") or (continua == "nao"):
        break


'''
lista = []

while True:
    fruta = input("Digite o nome fruta: ")
    lista.append(fruta)
    print(lista)
    continua = input("Deseja sair? [s, n]: ").lower()
    if (continua == "n") or (continua == "nao"):
        break
'''
