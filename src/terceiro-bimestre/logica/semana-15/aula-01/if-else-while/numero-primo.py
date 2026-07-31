numero = int(input("Digite um número: "))

for i in range(2, numero):
    if numero % i == 0:
        print(f"{numero} não é primo (divisível por {i}).")
        break
else:
    print(f"{numero} é um número primo!")



