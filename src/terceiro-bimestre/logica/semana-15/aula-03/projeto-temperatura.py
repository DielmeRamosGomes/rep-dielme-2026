temperaturas = [22, 25, 21, 24, 26, 23, 22]

#Identifique quantos valores existem na lista.
print(f"A lista tem {len(temperaturas)} valores")

#Determine o índice do primeiro e do último valor.
print(temperaturas[0])
print(temperaturas[6])

#Desafio 2 
i = 0
while i < len(temperaturas):
    print(temperaturas[i])
    i += 1
    
#Desafio 3 Soma
soma = 0
i = 0
while i < len(temperaturas):
    soma = soma + temperaturas[i]
    i += 1
print(f"Soma = {soma}")

#Desafio 4
media = soma / len(temperaturas)
print(f"Média = {media}")

#Desafio 5 - Busca Linear
procurada = 24
encontrou = False
i = 0
while i < len(temperaturas):
    if temperaturas[i] == procurada:
        encontrou = True
        break
    i += 1
if encontrou == True:
    print(f"Encontrou a temperatura {procurada} na lista") 
else:
    print("Não encontrou a temperatura")
