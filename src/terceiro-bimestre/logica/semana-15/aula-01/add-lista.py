lista = []
while True:
    numero = int(input("Digite um numero: "))
    lista.append(numero)
    print(f"Lista atualizada: {lista}")
    continua = input("Deseja continuar?[s, n]: ").lower()
    if (continua == "n") or (continua == "nao"):
        break
print(f"Lista Final: {lista}")
