livros = [{
    "codigo": 1,
    "titulo": "O Senhor dos Anéis",
    "autor": "J.R.R. Tolkien",
    "data-publicacao": 1954,
    "editora": "Allen & Unwin",
}]

print("Bem-vindo à Biblioteca!")
print("Cadastrar um livro.")
livros.append({
    "codigo": int(input("Digite o código do livro: ")),
    "titulo": input("Digite o título do livro: "),
    "autor": input("Digite o autor do livro: "),
    "data-publicacao": int(input("Digite o ano de publicação do livro: ")),
    "editora": input("Digite a editora do livro: ")
})

print("\nLista de livros cadastrados:")
for livro in livros:
    print(f"Código: {livro['codigo']}")
    print(f"Título: {livro['titulo']}")
    print(f"Autor: {livro['autor']}")
    print(f"Ano de Publicação: {livro['data-publicacao']}")
    print(f"Editora: {livro['editora']}")
    print("-------------------------------------------------")

