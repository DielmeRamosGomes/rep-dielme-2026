def soma(lista):
    soma = 0
    for i in range(len(lista)):
        soma = soma + lista[i]
    return soma

def subtracao(lista):
    subtracao = lista[0]
    for i in range(1, len(lista)):
        subtracao = subtracao - lista[i]
    return subtracao

def multiplicacao(lista):
    multiplicacao = lista[0]
    for i in range(1, len(lista)):
        multiplicacao = multiplicacao * lista[i]
    return multiplicacao

def cria_lista():
    lista = []
    while True:
        numero = int(input("Digite um numero: "))
        lista.append(numero)
        continua = input("Deseja mais numeros? [s, n]: ").lower()    
        if (continua == "n") or (continua == "não") or (continua == "nao"):
            break
    return lista
        
#print(f"Soma = {soma(cria_lista())}")
#print(f"Subtração = {subtracao(cria_lista())}")
#print(f"Multiplicação = {multiplicacao(cria_lista())}")
