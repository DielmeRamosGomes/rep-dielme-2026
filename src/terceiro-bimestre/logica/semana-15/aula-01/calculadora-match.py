num1 = float(input("Digite um numero: "))
num2 = float(input("Digite um numero: "))
operação = input("Digite uma operação (+, -, *, /): ")

match operação:
    case "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    case "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    case "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    case "/":
        if num2 > 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Não é possivel dividir por zero!")
    case _:
        print("Operador inválido!")