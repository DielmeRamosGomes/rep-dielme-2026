# pip install pandas
import pandas as pd

# Passo 1: Criando o conjunto de dados simples
dados = pd.DataFrame({
    "horas_estudo": [1, 2, 3, 4, 5],
    "nota_anterior": [2, 4, 6, 8, 10]
})

print("--- Tabela de Dados ---")
print(dados)

# Passo 2: Verificando a matriz de correlação
print("\n--- Matriz de Correlação ---")
print(dados.corr())

'''
o método corr() calcula a matriz de correlação entre as colunas numéricas. 
Nesse caso, a correlação entre horas_estudo e nota_anterior será 1.0, 
indicando uma correlação positiva perfeita. Isso significa que, neste 
pequeno conjunto de dados, o aumento das horas de estudo está associado 
linearmente ao aumento da nota.
'''



