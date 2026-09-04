# pip install pandas numpy scikit-learn

import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Configuração da semente aleatória para garantir a reprodutibilidade
np.random.seed(42)

# ==============================================================================
# ETAPA 1: GERAÇÃO E PREPARAÇÃO DOS DADOS
# ==============================================================================
# Criamos o DataFrame inicial com as variáveis explicativas de desempenho escolar
dados = pd.DataFrame({
    "horas_estudo": np.random.randint(1, 6, 50),
    "exercicios": np.random.randint(10, 100, 50),
    "frequencia": np.random.randint(60, 100, 50),
    "participacao": np.random.randint(1, 10, 50),
})

# EXPLICAÇÃO DA NOTA ANTERIOR:
# A 'nota_anterior' é gerada como uma função direta de 'horas_estudo' * 1.5 + ruído.
# Isso é feito intencionalmente no script para introduzir MULTICOLINEARIDADE
# (correlação forte entre duas variáveis explicativas).
dados["nota_anterior"] = dados["horas_estudo"] * 1.5 + np.random.normal(0, 1, 50)

# EXPLICAÇÃO DA NOTA FINAL (VARIÁVEL ALVO):
# A 'nota_final' foi simulada combinando TODAS as variáveis com pesos específicos.
# Por essa razão, quando usamos todas as 5 variáveis originais, o modelo de regressão
# obtém um R² altíssimo (~0.98), pois existe uma relação direta construída nos dados.
dados["nota_final"] = (dados["horas_estudo"] * 1.2 + 
                       dados["exercicios"] * 0.05 + 
                       dados["frequencia"] * 0.1 + 
                       dados["participacao"] * 0.5 + 
                       np.random.normal(0, 0.5, 50))

# ==============================================================================
# ETAPA 2: ANÁLISE DE CORRELAÇÃO E MULTICOLINEARIDADE
# ==============================================================================
print("=" * 60)
print("1. MATRIZ DE CORRELAÇÃO")
print("=" * 60)
matriz_corr = dados.corr()
print(matriz_corr.round(3))

# EXPLICAÇÃO DO RESULTADO DA CORRELAÇÃO:
# Na matriz gerada, 'horas_estudo' e 'nota_anterior' têm correlação muito alta (~0.90).
# Isso indica que ambas as variáveis fornecem praticamente a mesma informação ao modelo.
# Ter ambas no modelo pode inflar os coeficientes e causar instabilidade numérica.

# REDUÇÃO DE COLINEARIDADE:
# Decisão: Mantemos 'horas_estudo' e descartamos 'nota_anterior'.
dados_reduzidos = dados.drop(columns=["nota_anterior"])
print("\n[OK] Variável 'nota_anterior' removida devido à alta colinearidade com 'horas_estudo'.")

# ==============================================================================
# ETAPA 3: CRIAÇÃO DE NOVA FEATURE (ENGENHARIA DE ATRIBUTOS)
# ==============================================================================
# EXPLICAÇÃO DA NOVA FEATURE:
# Unimos 'frequencia' e 'participacao' em um único indicador sintético: 'engajamento_total'.
# Multiplicamos a participação por 10 para nivelar sua escala (1 a 10) com a frequência (60 a 100).
# Essa combinação resume o comportamento ativo do estudante em uma única métrica composta.
dados["engajamento_total"] = dados["frequencia"] + (dados["participacao"] * 10)

print("\n" + "=" * 60)
print("2. CRIAÇÃO DA FEATURE 'engajamento_total'")
print("=" * 60)
print(dados[["frequencia", "participacao", "engajamento_total"]].head())

# ==============================================================================
# ETAPA 4: APLICAÇÃO DE PCA (REDUÇÃO DE DIMENSIONALIDADE)
# ==============================================================================
features = ["horas_estudo", "exercicios", "frequencia", "participacao", "nota_anterior"]
X = dados[features]

# EXPLICAÇÃO DA PADRONIZAÇÃO (StandardScaler):
# O PCA calcula autovetores/autovalores e é extremamente sensível à escala dos dados.
# Como 'exercicios' varia de 10 a 100 e 'horas_estudo' de 1 a 5, devemos padronizar
# todas as variáveis para média 0 e desvio padrão 1 antes do PCA.
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# APLICANDO PCA PARA REDUZIR DE 5 VARIÁVEIS PARA 2 COMPONENTES
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print("\n" + "=" * 60)
print("3. RESULTADOS DO PCA")
print("=" * 60)
print("Variância explicada por cada componente:", pca.explained_variance_ratio_.round(4))
print(f"Variância explicada acumulada (2 componentes): {np.sum(pca.explained_variance_ratio_):.2%}")

# EXPLICAÇÃO DOS COMPONENTES DO PCA:
# Ao reduzir de 5 variáveis originais para 2 componentes, retemos aproximadamente ~62.5%
# da variação total dos dados originais. Os ~37.5% restantes foram descartados na compressão.

# ==============================================================================
# ETAPA 5: AVALIAÇÃO DE DESEMPENHO E COMPARAÇÃO DO MODELO
# ==============================================================================
y = dados["nota_final"]

# MODELO 1: Regressão Linear com todas as 5 variáveis originais
reg1 = LinearRegression().fit(X_scaled, y)
pred1 = reg1.predict(X_scaled)
r2_orig = r2_score(y, pred1)

# MODELO 2: Regressão Linear utilizando apenas os 2 componentes do PCA
reg2 = LinearRegression().fit(X_pca, y)
pred2 = reg2.predict(X_pca)
r2_pca = r2_score(y, pred2)

print("\n" + "=" * 60)
print("4. AVALIAÇÃO DO IMPACTO NO MODELO (R²)")
print("=" * 60)
print(f"R² com Dados Originais (5 variáveis) : {r2_orig:.4f}")
print(f"R² com PCA (2 Componentes Principais): {r2_pca:.4f}")

# EXPLICAÇÃO FINAL DOS RESULTADOS:
# 1. O R² original é muito elevado (~0.98) porque a nota final dependia de todas as 5 variáveis originais.
# 2. O R² com PCA cai para ~0.76 porque ao usarmos apenas 2 componentes, descartamos quase 37.5% da variância.
# 3. TRADE-OFF DO PCA: O PCA reduz a complexidade, remove redundâncias e reduz overfitting em grandes bases,
#    porém resulta em duas desvantagens:
#    a) Perda de informação explicativa relevante quando reduzimos muito os componentes.
#    b) Perda total de interpretabilidade (Componente 1 e 2 são combinações matemáticas abstratas,
#       não correspondendo diretamente a 'horas de estudo' ou 'frequência').