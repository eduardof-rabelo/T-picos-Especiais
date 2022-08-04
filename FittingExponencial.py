import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def decay(t, p0):
    return p0 * np.exp(-t*p0)

decaimento = pd.read_excel("dados-decaimento.xlsx")
#Leitura de dados pelo Pandas

fig, ax1 = plt.subplots(sharex=True, dpi=150, figsize=(6,4))
ax1.hist(decaimento["Decaimento"], bins=50, rwidth=0.8, color='tab:blue')
ax1.set_ylabel("Ocorrencias", color='tab:blue')
ax1.set_xlabel("t")
ax1.tick_params(axis ='y', labelcolor='tab:blue')
#Plot Histograma dos tempos de decaimento regrsitrados

tal_chapeu = 0
n, k, val = 50, 0, 0

for i in decaimento["Decaimento"]:
    val += i
tal_chapeu = val/n
print("Tau (ou tempo de decaimento) e: "+ str(tal_chapeu))
#Cálculo de tal_chapeu
var_tal_chapeu = (tal_chapeu**2)/n
print("A variancia de tau_chapeu e: " + str(var_tal_chapeu))
#Cálculo da variancia

t = np.linspace(0, 80, 80)
y = decay(t, 1/tal_chapeu)
ax2 = ax1.twinx()
ax2.plot(t,y, color="tab:orange")
ax2.set_title("Fitting tempo de decaimento")
ax2.set_xlabel("Tempo de decaimento")
ax2.set_ylabel("Probabilidade", color='tab:orange')
ax2.tick_params(axis ='y', labelcolor='tab:orange')
#Plot do fiiting do gráfico com 80 pontos em função de tal_chapeu
plt.savefig('Likelihood2.png')
