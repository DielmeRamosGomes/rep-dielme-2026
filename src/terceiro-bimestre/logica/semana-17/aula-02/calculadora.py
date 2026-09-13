num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

def calculadora(num1, num2, operacao):
    match operacao:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            if num2 != 0:
                return num1 / num2
            else:
                return "Erro: Divisão por zero não é permitida."
        case _:
            return "Erro: Operação inválida."
        
resultado = calculadora(num1, num2, operacao)
print(f"{num1} {operacao} {num2} = {resultado}")

