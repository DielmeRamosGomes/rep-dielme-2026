temperaturas = [22, 25, 21, 24, 26, 23, 20]

#Identifique quantos valores existem na lista.
print(f"O tamanho da lista é = {len(temperaturas)}")

#Determine o índice do primeiro e do último valor.
print(f"{temperaturas[0]} tem o indice = {temperaturas.index(22)}")
print(f"{temperaturas[6]} tem o indice = {temperaturas.index(20)}")

#Desafio 2 - Percorrendo a lista
i = 0
while i < len(temperaturas):
    print(temperaturas[i])
    i += 1

#Desafio 3- soma
soma = 0
i = 0
while i < len(temperaturas):
    soma = soma + temperaturas[i]
    i += 1
print(f"Soma = {soma}")