soma_total = 0
while True:
    valor_produto = float(input("Digite o valor do produto: "))
    soma_total += valor_produto
    print(f"Valor Parcial R${soma_total}")
    continua = input("Finalizou a compra?[f] para sair: ")
    if continua == "f":
        break
print(f"Total da compra = {soma_total}")



