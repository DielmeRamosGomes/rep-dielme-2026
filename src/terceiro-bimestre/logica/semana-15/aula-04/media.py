qtd_notas = int(input("Digite a quantidade de notas: "))
notas = []
soma = 0
i = 1
while True:
    try:
        nota = float(input(f"Digite a nota {i}:  "))
        if nota < 0 or nota > 10:
            print("Nota inválida! Digite uma nota entre 0 e 10.")
            continue
        notas.append(nota)
        i += 1
        soma += nota
        if len(notas) == qtd_notas:
            break
    except ValueError:
        print("Entrada inválida! Digite um número.")

media = soma / qtd_notas
print(f"A média das notas é: {media:.2f}")
if media >= 7:
    print("Desempenho: Satisfatório")
else:
    print("Desempenho: Insatisfatório")