matriz  = [[0 for coluna in range(3)] for linha in range(2)]

for linha in range(2):
    for coluna in range(3):
        print(matriz[linha][coluna], end=" ")
    print()

matriz[0][1] = 10
print()
for linha in range(2):
    for coluna in range(3):
        print(matriz[linha][coluna], end=" ")
    print()
