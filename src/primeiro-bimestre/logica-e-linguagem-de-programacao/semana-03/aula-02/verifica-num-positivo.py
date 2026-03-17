def verifica_num():
    while True:
        numero = float(input("Digite um numero : "))
        if numero > 0:
            print("O número é positivo.")
        else: 
            if numero == 0:
                print("O número é zero portando não é positivo nem negativo e sim neutro.")
            else:
                print("O número não é positivo!")
        continua  = input("Deseja continuar executando?[sim, nao]: ").lower()
        if continua == "nao":
            break

verifica_num()

