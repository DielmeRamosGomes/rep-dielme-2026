def calculadora(num1, num2, operador):
    if operador == "+":
        return num1 + num2
    elif operador == "-":
        return num1 - num2
    elif operador == "*":
        return num1 * num2
    elif operador == "/":
        if num2 == 0:
            return "Não é possível dividir por zero!"
        else:
            return num1 / num2
    else:
        return "Erro opção inválida"
 
numero1 = 10
numero2 = 20
operador = "+"   
print(f"{numero1} {operador} {numero2} = {calculadora(numero1, numero2, operador)}")