soma_total = 0
while True:
    produto = float(input("Valor produto: "))
    soma_total = soma_total + produto
    print(f"Valor parcial: R${soma_total}")
    continua = input("Finalizou a compra?[f]: ")
    if continua == "f":
        break
print(f"Total da compra: {soma_total}")
    