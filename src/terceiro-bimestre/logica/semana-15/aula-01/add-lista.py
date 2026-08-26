lista = []
while True:
    palavra = input("Digite uma palavra: ")
    lista.append(palavra)
    print(f"Lista atualizada: {lista}")
    continua = input("Deseja continuar?[s, n]: ").lower()
    if (continua == "n") or (continua == "nao"):
        break
print(f"Lista Final: {lista}")
