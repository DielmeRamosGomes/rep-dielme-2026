idade = int(input("Digite uma idade: "))
if (idade > 0) and (idade <= 4):
    print("A pessoa é um Bebe")
elif (idade >= 5) and (idade <= 9):
    print("A pessoa é criança")
elif (idade >= 10) and (idade <= 17):
    print("A pessoa é adolescente")
elif (idade >= 18):
    print("A pessoa é adulta")
else:
    print("A idade não pode ser negativa")

