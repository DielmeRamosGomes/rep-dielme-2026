def menu():
    print("=== Menu ===")
    print("1 - Ver mensagem")
    print("2 - Sair")

def menu_escolha(escolha):  
    match escolha:
        case "1":
            print("Bem-vindo")
        case "2":
            print("Encerrando...")
        
escolha = input("Escolha: ")





