resto = 0
binario = []
quociente = int(input("Digite um número decimal: "))
while quociente > 0:
    resto = quociente % 2
    binario.append(resto)
    quociente = quociente // 2

binario.reverse()
print("O número em binário é: ", end="")
for bit in binario:
    print(bit, end="")
