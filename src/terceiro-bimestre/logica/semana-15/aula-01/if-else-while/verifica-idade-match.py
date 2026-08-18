idade = int(input("Digite uma idade: "))
match idade:
    case idade if idade > 0 and idade <= 4:
        print("Bebê")
    case idade if idade >= 5 and idade <= 9:
        print("Criança")
    case idade if idade >= 10 and idade <= 17:
        print("Adolescente")
    case idade if idade >= 18:
        print("Adulto")
    case _:
        print("Idade não pode ser negativo")   

