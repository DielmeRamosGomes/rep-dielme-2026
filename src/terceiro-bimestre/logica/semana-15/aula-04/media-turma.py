notas = []
soma = 0
qtd_notas = int(input("Digite o tamanho da lista: "))
for posicao in range(qtd_notas):
    nota = float(input(f"Digite a nota {posicao+1}: "))
    while (nota < 0) or (nota > 10):
        print("A nota deve ser entre 0 e 10")
        nota = float(input(f"Digite a nota {posicao+1}: "))
    notas.append(nota)
    soma += notas[posicao]
media = soma / qtd_notas
print(f"Media da turma = {media}")
if media >= 7:
    print("Desempenho: Satisfatório")
else:
    print("Desenpenho: Insatisfatório")
