import os
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, models, transforms
from torch.utils.data import DataLoader

# pip install -r requisitos.txt

# --- Adicione esta linha para descobrir a pasta atual do script ---
DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))

# Configurações e Hiperparâmetros
EPOCAS = 5
BATCH_SIZE = 32

# Configurações e Hiperparâmetros
EPOCAS = 5
BATCH_SIZE = 32
PASTA_TREINO = os.path.join(DIRETORIO_ATUAL, 'dados', 'treino')
PASTA_MODELO = os.path.join(DIRETORIO_ATUAL, 'modelos', 'modelo_ppt.pth')

# 1. Transformações de Imagem
transformacoes = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

# 2. Carregar os dados
if not os.path.exists(PASTA_TREINO):
    raise FileNotFoundError(f"Crie a pasta '{PASTA_TREINO}' e adicione as subpastas com as fotos.")

dataset_treino = datasets.ImageFolder(root=PASTA_TREINO, transform=transformacoes)
loader_treino = DataLoader(dataset_treino, batch_size=BATCH_SIZE, shuffle=True)

# 3. Modelo Base (Transfer Learning)
modelo = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)

for param in modelo.parameters():
    param.requires_grad = False

# Alterando a saída para 3 classes (Papel, Pedra, Tesoura)
num_caracteristicas = modelo.fc.in_features
modelo.fc = nn.Linear(num_caracteristicas, 3)

# 4. Treinamento
funcao_perda = nn.CrossEntropyLoss()
otimizador = optim.Adam(modelo.fc.parameters(), lr=0.001)
dispositivo = torch.device("cuda" if torch.cuda.is_available() else "cpu")
modelo = modelo.to(dispositivo)

modelo.train()
print("Iniciando o Fine-Tuning...")

for epoca in range(EPOCAS):
    perda_da_epoca = 0.0
    for imagens, labels in loader_treino:
        imagens, labels = imagens.to(dispositivo), labels.to(dispositivo)
        
        otimizador.zero_grad()
        saidas = modelo(imagens)
        perda = funcao_perda(saidas, labels)
        perda.backward()
        otimizador.step()
        
        perda_da_epoca += perda.item()
        
    print(f"Época {epoca+1}/{EPOCAS} - Perda: {perda_da_epoca/len(loader_treino):.4f}")

# 5. Salvar o modelo treinado
os.makedirs('modelos', exist_ok=True)
torch.save(modelo.state_dict(), PASTA_MODELO)
print(f"Modelo salvo com sucesso em: {PASTA_MODELO}")
