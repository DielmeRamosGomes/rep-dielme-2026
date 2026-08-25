# pip install scikit-learn

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# ==========================================
# ETAPA 1 — PREPARAÇÃO DOS DADOS
# ==========================================
# X representa a matriz de características (Features): [horas de estudo, faltas]
X = [
    [2, 1], [4, 0], [1, 3], [3, 1], [5, 0], [2, 2]
]

# y representa o vetor de rótulos (Labels/Target): 0 = Reprovado, 1 = Aprovado
y = [0, 1, 0, 1, 1, 0]

# ==========================================
# ETAPA 2 — SEPARAÇÃO EM TREINO E TESTE
# ==========================================
# Separar em treino e teste evita a memorização dos dados (overfitting),
# garantindo que o modelo seja testado em informações inéditas.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42
)

# ==========================================
# ETAPA 3 — CRIAÇÃO DO MODELO
# ==========================================
# Instanciando a Regressão Logística, ideal para problemas de classificação binária.
# "Treinar um modelo" significa fazer o algoritmo ajustar seus parâmetros internos
# para encontrar padrões que relacionem as características (X) ao resultado (y).
modelo = LogisticRegression()

# ==========================================
# ETAPA 4 — TREINAMENTO
# ==========================================
# Os dados de treino servem como base de aprendizado para que o modelo
# identifique as regras de decisão entre horas de estudo, faltas e aprovação.
modelo.fit(X_train, y_train)

# ==========================================
# ETAPA 5 — AVALIAÇÃO
# ==========================================
# Gerando previsões com os dados de teste inéditos
y_pred = modelo.predict(X_test)

# A acurácia mede a porcentagem de acertos totais do modelo sobre o conjunto de teste.
acuracia = accuracy_score(y_test, y_pred)
print(f"Acurácia do modelo: {acuracia * 100:.2f}%")



