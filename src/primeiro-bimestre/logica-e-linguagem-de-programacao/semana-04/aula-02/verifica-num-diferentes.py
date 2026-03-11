def verifica_numero():
    while True:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        if num1 != num2:
            print("Os números são diferentes.")
        else:
            print("Os números são iguais.")
        continua = input("Deseja continuar executando? [sim, nao]: ").lower()
        if continua == "nao":
            break

verifica_numero()