import numpy as np
import matplotlib.pyplot as plt
timesteps = 1000
beta_start = 0.0001
beta_end = 0.002
beta_schedule_linear = np.linspace(beta_start, beta_end, timesteps)
plt.figure(figsize=(10, 5))
plt.plot(beta_schedule_linear, label='Linear Schedule')
plt.title('Previsão do Vento (Força do Ruído)')
plt.xlabel('Timestep (Rajada de Vento)')
plt.ylabel('Beta (Força do Vento / Ruído)')
plt.legend()
plt.show()