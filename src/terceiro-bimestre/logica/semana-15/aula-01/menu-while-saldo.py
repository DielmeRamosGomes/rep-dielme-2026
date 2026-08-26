saldo_da_conta = 50
while True:
    print("1 - Consulta Saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("")
    opcao = int(input("Escolha uma das opções: "))
    if opcao == 1:
        print(f"Saldo da conta = {saldo_da_conta} \n")
    elif opcao == 2:
        deposito = int(input("Quanto deseja depositar?: "))
        saldo_da_conta += deposito
    elif opcao == 3:
        sacar = int(input("Quanto deseja sacar?: "))
        if sacar <= saldo_da_conta:
            saldo_da_conta -= sacar
            print("Saque aprovado")
        else:
            print("Saldo insuficiente")
    else:
        print("Opção inválida")