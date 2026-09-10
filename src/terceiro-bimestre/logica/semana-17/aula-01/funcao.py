def soma(numero1, numero2):
    return numero1 + numero2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 == 0:
        return "Não é possível dividir por zero"
    return num1 / num2

def soma_lista(lista):
    soma = 0
    for pos in range(len(lista)):
        soma += lista[pos]
    return soma

num1 = 10
num2 = 0
n1 = 30
n2 = 50
#resultado = soma(num1, num2)
print(f"{num1} + {num2} = {soma(num1, num2)}")
print(f"{num1} * {num2} = {multiplicacao(num1, num2)}")
print(f"{num1} / {num2} = {divisao(num1, num2)}")

print(f"Soma = {soma_lista([1, 2, 3, 4, 5])}")

