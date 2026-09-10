def soma_numeros(numero1, numero2):
    return numero1 + numero2

def multiplicacao(numero1, numero2):
    return numero1 * numero2
 
def divisao(numero1, numero2):
    if numero2 == 0:
        return "não é possível dividir por 0"
    return numero1 / numero2 

def soma_lista(lista):
    soma = 0 
    for posicao in range(len(lista)):
        soma = soma + lista[posicao]
    return soma 


num1 = 10
num2 = 0
resultado = soma_numeros(num1, num2)
res = multiplicacao(num1, num2)
div = divisao(num1, num2)
print(f"{num1} + {num2} = {resultado}")
print(f"{num1} * {num2} = {res}")
print(f"{num1} / {num2} = {div}")

print(f"Soma da lista = {soma_lista([1, 2, 3, 4, 5, 15])}")





