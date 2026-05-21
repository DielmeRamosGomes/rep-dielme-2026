# Equipando nossa academia de IA

import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim.lr_scheduler import CosineAnnealingLR
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import os

print("🏋️‍♂️ Personal Trainer de IA inicializado!")
print("🏃‍♀️ Academia equipada com:")
print("   💪 Otimizador AdamW")
print("   📈 Scheduler Cosine LR")
print("   💾 Sistema de Checkpoints")
print("   📊 Monitoramento de progresso")


# Criando nosso "aluno" - uma rede neural simples
class AlunoIA(nn.Module):
    def __init__(self):
        super(AlunoIA, self).__init__()
        print("🎓 Criando novo aluno na academia...")

        self.features = nn.Sequential(
            nn.Conv2d(3, 32, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 64, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.AdaptiveAvgPool2d((4, 4)),
        )

        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(64 * 4 * 4, 128),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(128, 10),  # CIFAR-10 tem 10 classes
        )

    def forward(self, x):
        x = self.features(x)
        x = self.classifier(x)
        return x


# Instanciando nosso aluno

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
aluno = AlunoIA().to(device)
print(f"🎯 Aluno criado e enviado para: {device}")
print(
    f"📊 Parâmetros treináveis: {sum(p.numel() for p in aluno.parameters() if p.requires_grad):,}"
)

# Preparando os exercícios (dados de treino)

print("📚 Preparando exercícios para o aluno...")

transform = transforms.Compose(
    [
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),  # [-1,1]
    ]
)

# Carregando CIFAR-10

trainset = torchvision.datasets.CIFAR10(
    root="./data", train=True, download=True, transform=transform
)

trainloader = torch.utils.data.DataLoader(
    trainset, batch_size=128, shuffle=True, num_workers=2
)

testset = torchvision.datasets.CIFAR10(
    root="./data", train=False, download=True, transform=transform
)

testloader = torch.utils.data.DataLoader(
    testset, batch_size=128, shuffle=False, num_workers=2
)

print(f"💪 Exercícios de treino: {len(trainset)} exemplos")
print(f"🎯 Exercícios de teste: {len(testset)} exemplos")
print(f"📦 Tamanho do lote: 128 exemplos por vez")
print("💪 CONFIGURANDO O PERSONAL TRAINER (AdamW)")
print("=" * 45)
print("🤔 Por que AdamW é especial?")
print("   • Adam: Adapta a taxa de aprendizado para cada parâmetro")
print("   • W (Weight Decay): Evita que o aluno 'decore' demais (overfitting)")
print("   • É como um trainer que ajusta exercícios individualmente")
print("   • E ainda evita que o aluno fique 'viciado' em um tipo de exercício")
print()

# Configurando o otimizador AdamW

learning_rate = 0.001

weight_decay = 0.01  # Regularização para evitar overfitting

optimizer = optim.AdamW(
    aluno.parameters(),
    lr=learning_rate,
    weight_decay=weight_decay,
    betas=(0.9, 0.999),  # Parâmetros de momentum
    eps=1e-8,
)

print("⚙️ Personal Trainer AdamW configurado:")
print(f"   📈 Taxa de aprendizado inicial: {learning_rate}")
print(f"   ⚖️ Weight decay (regularização): {weight_decay}")
print(f"   🏃‍♂️ Momentum beta1: 0.9 (memória de curto prazo)")
print(f"   🏃‍♀️ Momentum beta2: 0.999 (memória de longo prazo)")

# Simulando como AdamW ajusta diferentes parâmetros

def demonstrar_adamw():
    print("🔍 DEMONSTRAÇÃO: Como AdamW ajusta parâmetros")
    print("=" * 50)

    # Simulando gradientes diferentes para diferentes camadas

    gradientes_simulados = {
        "conv1.weight": 0.1,
        "conv2.weight": 0.05,
        "fc1.weight": 0.2,
        "fc2.weight": 0.01,
    }

    print("📊 Gradientes simulados por camada:")

    for camada, grad in gradientes_simulados.items():
        # AdamW ajustaria a taxa de aprendizado baseado no histórico
        lr_ajustada = learning_rate * (1.0 / (1.0 + abs(grad)))
        print(f"   {camada:15s}: grad={grad:5.2f} → lr_efetiva≈{lr_ajustada:.6f}")

    print("\n💡 AdamW faz isso automaticamente para TODOS os parâmetros!")


demonstrar_adamw()
