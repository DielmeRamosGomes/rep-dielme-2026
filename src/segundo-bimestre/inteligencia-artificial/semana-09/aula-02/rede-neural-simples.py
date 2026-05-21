import torch 
import torch.nn as nn

# Criando uma rede neural simples com o PyTorch
class MinhaPrimeiraIA(nn.Module):
    def __init__(self):
        super(MinhaPrimeiraIA, self).__init__()
        # Uma camada que recebe 10 dados e transforma em 5
        self.camada1 = nn.Linear(10, 5)
        # Uma camada que pega esses 5 e transforma na resposta final (1)
        self.camada2 = nn.Linear(5, 1)

    def forward(self, x):
        x = torch.relu(self.camada1(x)) # Ativação (filtro)
        x = self.camada2(x)
        return x

# Instanciando a IA
modelo = MinhaPrimeiraIA()
print(modelo)