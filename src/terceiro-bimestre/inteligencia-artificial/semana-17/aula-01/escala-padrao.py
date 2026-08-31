# pip install scikit-learn
# pip install pandas

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pandas as pd

dados = pd.DataFrame({
    'matematica':[9,8,4,3],
    'fisica':[8,7,5,4],
    'quimica':[9,8,4,3]
})

scaler = StandardScaler()
dados_pad = scaler.fit_transform(dados)

pca = PCA(n_components=1)
resultado = pca.fit_transform(dados_pad)

print(resultado)

'''
[
    [ 2.08893962] Aluno 1 (Notas: 9, 8, 9) -> Desempenho muito acima da média
    [ 1.27112069] Aluno 2 (Notas: 8, 7, 8) -> Desempenho acima da média
    [-1.27112069] Aluno 3 (Notas: 4, 5, 4) -> Desempenho abaixo da média
    [-2.08893962] Aluno 4 (Notas: 3, 4, 3) -> Desempenho muito abaixo da média
 ]
'''

# 1. Quanto da informação total (variância) foi preservada em 1 única coluna?
print("Variância explicada:", pca.explained_variance_ratio_[0])

'''
Mostra um valor próximo de 0.98 (98%), o que significa 
que condensar 3 colunas em apenas 1 fez perder apenas 
2% da informação original.
'''

# 2. Qual o peso/impacto de cada matéria nessa nova coluna?
pesos = pd.DataFrame(pca.components_, columns=dados.columns, index=['PC1'])
print("\nPesos das matérias:\n", pesos)   
   
'''
Pesos (components_): Mostrará pesos equilibrados (aprox. 0.58
para cada matéria), indicando que o PC1 funciona como um 
"índice de desempenho geral em exatas".
'''

