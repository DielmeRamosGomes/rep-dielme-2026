produtos = []
def mostrar_menu():
    print("\n1 - Cadastrar Produto")
    print("2 - Consultar Produto por ID")
    print("3 - Listar todos os produtos")  
    print("s - Sair do Programa") 

def cadastrar_produto():
    id = int(input("\nDigite o ID do produto: "))
    produto = busca_id(id)
    while produto != None:
        print(f"\nProduto com ID {id} já cadastrado.")
        id = int(input("Digite o ID do produto: "))
        produto = busca_id(id)
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    produto = {
        "id":id,
        "nome": nome,
        "preco": preco   
    }
    produtos.append(produto)
    print("\nProduto cadastrado com sucesso!")

def busca_id(id):
    for produto in produtos:
        if produto["id"] == id:
            return produto
    return None

def imprime_produto(produto):
    print(f"ID: {produto['id']}")
    print(f"Nome: {produto['nome']}")
    print(f"Preço: {produto['preco']}")
    print("-----------------------------------------")

def listar_produtos():
    if len(produtos) == 0:
        print("\nNenhum produto cadastrado.")
    else:
        print("\nLista de produtos:")
        for produto in produtos:
            imprime_produto(produto)

def menu_escolha(escolha):
    match escolha:
        case "1":
            cadastrar_produto()
        case "2":
            id_produto = int(input("Digite o ID: "))
            produto = busca_id(id_produto)
            if produto != None:
                imprime_produto(produto)
            else:
                print(f"\nProduto com ID {id_produto} não encontrado.")
        case "3":
            listar_produtos()
                
while True:
    mostrar_menu()
    escolha = input("\nDigite a escolha ou [s] para sair: ")
    menu_escolha(escolha)
    if escolha.lower() == "s":
        break







