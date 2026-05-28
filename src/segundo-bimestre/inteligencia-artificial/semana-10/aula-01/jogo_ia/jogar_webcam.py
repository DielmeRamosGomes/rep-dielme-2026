import cv2
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
import os

# Configurações
DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
CLASSES = ['Papel', 'Pedra', 'Tesoura'] # Atenção: o PyTorch organiza por ordem alfabética das pastas!
PASTA_MODELO = os.path.join(DIRETORIO_ATUAL, 'modelos', 'modelo_ppt.pth')

dispositivo = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 1. Recriar a estrutura do modelo exatamente como no treino
modelo = models.resnet18()
num_caracteristicas = modelo.fc.in_features
modelo.fc = nn.Linear(num_caracteristicas, 3)

# 2. Carregar o aprendizado salvo
try:
    modelo.load_state_dict(torch.load(PASTA_MODELO, map_location=dispositivo))
    modelo = modelo.to(dispositivo)
    modelo.eval()
    print("Modelo carregado com sucesso! Abrindo webcam...")
except FileNotFoundError:
    print(f"Erro: O arquivo '{PASTA_MODELO}' não foi encontrado. Rode o 'treinar.py' primeiro.")
    exit()

# 3. Transformações para os frames da câmera
transformacoes = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

# 4. Loop da Webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
        
    # Inverte o frame para agir como um espelho (opcional, mas melhora a experiência)
    frame = cv2.flip(frame, 1)
    
    # Prepara a imagem para o PyTorch
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    imagem_pil = Image.fromarray(frame_rgb)
    input_tensor = transformacoes(imagem_pil).unsqueeze(0).to(dispositivo)
    
    # Previsão da IA
    with torch.no_grad():
        saidas = modelo(input_tensor)
        _, indice = torch.max(saidas, 1)
        resultado = CLASSES[indice.item()]
    
    # Mostra o resultado na tela
    cv2.putText(frame, f"IA detectou: {resultado}", (30, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    
    cv2.imshow('Pedra, Papel e Tesoura - Janela de Jogo', frame)
    
    # Fecha se apertar 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
