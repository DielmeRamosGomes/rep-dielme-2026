idade = int(input("Digite uma idade: "))

if idade <= 0:
    print("Idade não pode ser menor que ou igual a 0")
elif idade > 0 and idade <= 9:
    print("A pessoa é uma criança!")
elif idade > 9 and idade <= 17:
    print("A pessoa é adolescente")    
elif idade >= 18:
    print("A pessoa é adulta")


