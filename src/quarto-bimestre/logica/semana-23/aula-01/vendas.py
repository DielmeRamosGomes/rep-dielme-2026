vendas = []

venda1 = {
    "Nome": "Caderno",
    "quantidade": 10,
    "Data": "2026-01-15" 
} 

venda2 = {
    "Nome": "Caderno",
    "quantidade": 12,
    "Data": "2026-02-10" 
} 

venda3 = {
    "Nome": "Caderno",
    "quantidade": 8,
    "Data": "2026-03-05" 
} 

vendas.append(venda1)
vendas.append(venda2)
vendas.append(venda3)

def media_venda():
    soma = 0
    media = 0
    for venda in vendas:
        soma += venda['quantidade']
    media = soma / len(vendas)
    return media

def classificacao_venda():
    media = media_venda()
    if media >= 30:
        print(f"\nProduto: {venda1['Nome']}")
        print(f"Média: {media}")
        print("Desempenho de venda Alto")
    elif media >= 10:
        print(f"\nProduto: {venda1['Nome']}")
        print(f"Média: {media}")
        print("Desempenho de venda Médio")
    else:
        print(f"\nProduto: {venda1['Nome']}")
        print(f"Média: {media}")
        print("Desenpenho de venda baixo")

classificacao_venda()