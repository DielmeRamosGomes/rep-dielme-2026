import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
timesteps = 1000
beta_start = 0.0001
beta_end = 0.02

# Tempo normalizado de 0 a 1
t_norm = np.linspace(0, 1, timesteps)

# Função: 1 - cos(theta) de 0 a pi/2
# Isso garante o início suave (derivada 0) e o final com crescimento máximo
crescimento_suave = 1 - np.cos(t_norm * (np.pi / 2))

# Ajuste para os limites de beta
beta_schedule = beta_start + (beta_end - beta_start) * crescimento_suave

# Plotagem
plt.figure(figsize=(10, 6))
plt.plot(beta_schedule, label='Início Suave -> Final Alto', color='crimson', linewidth=2.5)

# Linha para mostrar que o final não é suavizado (não "achata")
plt.axline((timesteps-100, beta_schedule[-100]), (timesteps, beta_schedule[-1]), 
           color='grey', linestyle=':', alpha=0.5, label='Tendência de Crescimento')

plt.title('Força do Vento: Início Quase Zero com Crescimento Contínuo')
plt.xlabel('Timestep')
plt.ylabel('Beta (Intensidade)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.show()