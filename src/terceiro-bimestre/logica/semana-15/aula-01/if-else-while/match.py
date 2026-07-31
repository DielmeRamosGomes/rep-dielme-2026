'''
lista = ["Domingo"]
match lista:
    case ["Domingo"]:
        print("Hoje é Domingo")
    case ["Segunda"]:
        print("Hoje é Domingo")
    case ["Terça"]:
        print("Hoje é Domingo")
    case ["Quarta"]:
        print("Hoje é Domingo")
    case ["Quinta"]:
        print("Hoje é Domingo")
    case ["Sexta"]:
        print("Hoje é Domingo")
    case ["Sábado"]:
        print("Hoje é Domingo")
    case _:
        print("Não é dia da semana")
'''
comando = "Sábado"
match comando:
    case "Domingo":
        print("Hoje é Domingo")
    case "Segunda":
        print("Hoje é Segunda")
    case "Terça":
        print("Hoje é Terça")
    case "Quarta":
        print("Hoje é Quarta")
    case "Quinta":
        print("Hoje é Quinta")
    case "Sexta":
        print("Hoje é Sexta")
    case "Sábado":
        print("Hoje é Sábado")
    case _:
        print("Não é dia da semana")

