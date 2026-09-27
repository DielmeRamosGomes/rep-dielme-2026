from pathlib import Path

'''
with open(Path(__file__).with_name("carros.txt"), "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read() # Uma única string com todo o arquivo
    print(conteudo)

with open(Path(__file__).with_name("carros.txt"), "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines() # Lista de strings, uma por linha
    for linha in linhas:
        print(linha.strip())
'''

with open(Path(__file__).with_name("carros.txt"), "r", encoding="utf-8") as arquivo:
    for linha in arquivo: 
        print(linha.strip()) # Uma linha por vez, sem carregar tudo



