from collections import deque
resto = 0
binario = deque([])
quociente = int(input("Digite um número decimal: "))
while quociente > 0:
    resto = quociente % 2
    binario.appendleft(resto)
    quociente = quociente // 2
    
print("O número em binário é: ", end="")
for bit in binario:
    print(bit, end="")
