produtos = []
def mostrar_menu():
    print("\n1 - Cadastrar Produto")
    print("2 - Consultar Produto por ID")
    print("3 - Listar todos os produtos")  
    print("s - Sair do Programa") 

def cadastrar_produto():
    id = int(input("\nDigite o ID do produto: "))
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: \n"))
    produto = {
        "id":id,
        "nome": nome,
        "preco": preco   
    }
    produtos.append(produto)
    print("\nProduto cadastrado com sucesso!")
    
def busca_id(id):
    encontrado = False
    for produto in produtos:
        if produto["id"] == id:
            encontrado = True
            print("\nProduto encontrado")
            print(produto)
    if encontrado == False:
        print("\nProduto não encontrado")

def listar_produtos():
    for produto in produtos:
        if len(produtos) > 0:
            print(f"ID: {produto["id"]}")
            print(f"Nome: {produto["nome"]}")
            print(f"Preço: {produto["preco"]}")
            print("----------------------------------------\n")
        else:
            print("Lista de produtos está vazia!")
            
def menu_escolha(escolha):
    match escolha:
        case "1":
            cadastrar_produto()
        case "2":
            id_produto = int(input("Digite o ID: "))
            busca_id(id_produto)
        case "3":
            listar_produtos()
                 
while True:
    mostrar_menu()
    escolha = input("\nDigite a escolha ou [s] para sair: ")
    menu_escolha(escolha)
    if escolha.lower() == "s":
        break







