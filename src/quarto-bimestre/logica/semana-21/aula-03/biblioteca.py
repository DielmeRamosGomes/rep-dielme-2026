biblioteca = []
def menu():
    print("\n1 - Cadastrar livro: ")
    print("2 - Buscar livro por ID: ")
    print("3 - Listar todos os livros")
    print("4 - Sair do programa")

def cadastrar_livro():
    id = int(input("\nDigite o ID: "))
    nome = input("Digite o nome: ")
    autor = input("Digite o autor: ")
    editora = input("Digite o nome da editora: ")
    livro = {
        "id": id,
        "nome": nome,
        "autor": autor,
        "editora": editora
    }
    biblioteca.append(livro)
    print("Livro foi cadastro com sucesso!")

def busca_livro(id):
    for livro in biblioteca:
        if livro['id'] == id:
            return livro
    return None

def imprime_livro(livro):
    print(f"ID: {livro['id']}")
    print(f"Nome: {livro['nome']}")
    print(f"Autor: {livro['autor']}")
    print(f"Editora: {livro['editora']}")

def listar_livros():
    for livro in biblioteca:
        imprime_livro(livro)
        print("----------------------------") 

def menu_escolha(escolha):
    match escolha:
        case "1":
            cadastrar_livro()
        case "2":
            id_usuario = int(input("\nDigite o ID: "))
            livro = busca_livro(id_usuario)
            if livro != None:
                imprime_livro(livro)
            else:
                print("\nO livro não está na lista")
        case "3":
            listar_livros()

def principal():
    while True:
        menu()
        escolha = input("Digite a escolha: ")
        menu_escolha(escolha)
        if escolha == "4":
            break

principal()