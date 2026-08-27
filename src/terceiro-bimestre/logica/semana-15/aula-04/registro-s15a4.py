qtd_notas = int(input("Digite a quantidade de notas: "))
notas = []
soma = 0
for posicao in range(qtd_notas):
    nota = float(input(f"Digite a nota {posicao + 1}: "))
    while (nota < 0) or (nota > 10):
        print("Nota inválida! Digite uma nota entre 0 e 10.")
        nota = float(input(f"Digite a nota {posicao + 1}: "))
    notas.append(nota)
    soma += nota
media = soma / qtd_notas
print(f"A média das notas é: {media:.2f}")
if media >= 7:
    print("Desempenho: Satisfatório")
else:
    print("Desempenho: Insatisfatório")