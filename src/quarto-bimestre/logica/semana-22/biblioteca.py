biblioteca = []
usuarios = []
usuario_logado = {
    "email": "",
    "senha": ""
}

def busca_usuario(email, senha):
    for usuario in usuarios:
        if usuario['email'] == email and usuario['senha'] == senha:
            return usuario
    return None

def menu_usuario():
    print("\n1 - Login: ")
    print("2 - Cadastrar de usuário: ")
    print("3 - Sair do programa")

def login():
    email = input("\nDigite o e-mail: ")
    senha = input("Digite a senha: ")
    for usuario in usuarios:
        if usuario['email'] == email and usuario['senha'] == senha:
            usuario_logado = busca_usuario(email, senha)
            return True
    return False

def cadastro_usuario():
    email = input("\nDigite o e-mail: ")
    senha = input("Digite a senha: ")
    usuario = {
        "email": email,
        "senha": senha
    }
    usuarios.append(usuario)
    print("\nCadastro realizado com sucesso!")

def loop_cadastro():
    while True:
        menu()
        escolha = input("Digite a escolha: ")
        menu_usuario(escolha)
        if escolha == "4":
            print("\nSaindo do programa!")
            break

def menu_usuario_escolha(escolha):
    match escolha:
        case "1":
            confirma = login()
            if confirma:
                print("\nBem-vindo usuário!")
                loop_cadastro()
            else:
                print("Usuário não encontrado!")
        case "2":
            cadastro_usuario()

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
        menu_usuario()
        escolha = input("Digite a escolha: ")
        menu_usuario_escolha(escolha)
        if escolha == "3":
            print("\nSaindo do programa!")
            break

principal()