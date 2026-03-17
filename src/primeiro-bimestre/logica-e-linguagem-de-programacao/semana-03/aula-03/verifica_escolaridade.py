def verifica_idade():
    while True:
        try:
            idade = int(input("\nDigite uma idade para o aluno maior que 10 anos: "))
            if idade > 10:
                return idade
            else:
                print("\nErro: A idade deve ser maior que 10 anos.")
        except ValueError:
            print("\nErro: Parâmetro inapropriado")

def verifica_media():
    while True:
        try:
            media = float(input("\nDigite uma média para o aluno entre [0, 10]: "))
            if 0 <= media <= 10:
                return media
            else:
                print("\nErro: A média deve estar entre [0, 10].")
        except ValueError:
            print("\nErro: Parâmetro inapropriado")

def classifica_serie_desempenho(idade, media):
    if idade > 10:
        if idade <= 13: 
            

def menu():
    while True:
        idade = verifica_idade()
        media = verifica_media()

        continua = input("\nDeseja continuar executando? [s/n]: ").lower()
        if continua == "n":
            break

if __name__ == "__main__":
    menu()