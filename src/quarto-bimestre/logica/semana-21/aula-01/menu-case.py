def menu():
    print("=== Menu ===")
    print("1 - Ver mensagem")
    print("2 - Sair")

def mostrar_mensagem():
    print("\nBem-vindo \n")

def mostrar_sair():
    print("\nEncerrando... \n")

def menu_escolha(escolha):
    match escolha:
        case "1":
            mostrar_mensagem()
        case "2":
            mostrar_sair()
  
while True:
    menu()      
    escolha = input("\nEscolha: ")
    menu_escolha(escolha)
    if escolha == "2":
        break      