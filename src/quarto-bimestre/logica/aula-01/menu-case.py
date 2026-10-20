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
  
while True:
    menu()      
    escolha = input("Escolha: ")
    menu_escolha(escolha)
    if escolha == "2":
        break      