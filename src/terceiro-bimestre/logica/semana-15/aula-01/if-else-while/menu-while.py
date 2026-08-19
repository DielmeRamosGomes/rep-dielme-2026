while True:
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Sair")
    print("")
    opcao = int(input("Digite a opção 1, 2 ou 3: "))
    if opcao == 1:
        num1 = int(input("Digite um numero1: "))
        num2 = int(input("Digite um numero2: "))
        print(f"{num1} + {num2} = {num1 + num2}")
    elif opcao == 2:
        num1 = int(input("Digite um numero1: "))
        num2 = int(input("Digite um numero2: "))
        print(f"{num1} - {num2} = {num1 - num2}")
    else:
        break
