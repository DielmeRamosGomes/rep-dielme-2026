vendas = []
resultados = []

item1 = {
    "Nome": "Caderno",
    "quantidade": 10,
    "Data": "2026-01-15" 
} 

item2 = {
    "Nome": "Caderno",
    "quantidade": 12,
    "Data": "2026-02-10" 
} 

item3 = {
    "Nome": "Lápis",
    "quantidade": 8,
    "Data": "2026-03-05" 
} 

item4 = {
    "Nome": "Lápis",
    "quantidade": 5,
    "Data": "2026-03-05"
}

vendas.append([item1, item2]) #venda1
vendas.append([item3, item4]) #venda2

def media_venda(venda):
    soma = 0
    for item in venda:
        soma += item['quantidade']

    return soma / len(venda)

def classificacao_venda():
    for venda in vendas:  
        media = media_venda(venda)  
        if media >= 30:
            print(f"\nProduto: {venda[0]['Nome']}")
            print(f"Média: {media}")
            desempenho = "Alto"
            print(f"Desempenho de venda {desempenho}")
            resultados.append([venda[0]['Nome'], media, desempenho])
        elif media >= 10:
            print(f"\nProduto: {venda[0]['Nome']}")
            print(f"Média: {media}")
            desempenho = "Médio"
            print(f"Desempenho de venda {desempenho}")
            resultados.append([venda[0]['Nome'], media, desempenho])
        else:
            print(f"\nProduto: {venda[0]['Nome']}")
            print(f"Média: {media}")
            desempenho = "Baixo"
            print(f"Desenpenho de venda {desempenho}")
            resultados.append([venda[0]['Nome'], media, desempenho])

classificacao_venda()


