
# IMPORTATION DES LIBRAIRIES

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.animation import FuncAnimation


# CHARGEMENT DU DATASET

df = pd.read_csv("Iris.csv")

# Supprimer la colonne Id si elle existe
if "Id" in df.columns:
    df.drop("Id", axis=1, inplace=True)


# STATISTIQUES DESCRIPTIVES

print("===== STATISTIQUES DESCRIPTIVES =====\n")

print("Moyenne :\n", df.mean(numeric_only=True))
print("\nMédiane :\n", df.median(numeric_only=True))
print("\nÉcart-type :\n", df.std(numeric_only=True))
print("\nQuartiles :\n", df.quantile([0.25, 0.5, 0.75], numeric_only=True))


# CREATION DU DASHBOARD 2x2

sns.set(style="whitegrid")

fig, axs = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Dashboard Multi-Graphiques - Dataset Iris", fontsize=16, fontweight="bold")


#  Histogramme

sns.histplot(df["SepalLengthCm"], kde=True, color="skyblue", ax=axs[0, 0])
axs[0, 0].set_title("Histogramme - Longueur des Sépales")
axs[0, 0].set_xlabel("Longueur (cm)")
axs[0, 0].set_ylabel("Fréquence")

# Ajouter une annotation moyenne
mean_value = df["SepalLengthCm"].mean()
axs[0, 0].axvline(mean_value, color='red', linestyle='--', label="Moyenne")
axs[0, 0].legend()


#  Scatter + Régression

sns.regplot(
    data=df,
    x="SepalLengthCm",
    y="PetalLengthCm",
    scatter_kws={"alpha": 0.6},
    line_kws={"color": "red"},
    ax=axs[0, 1]
)
axs[0, 1].set_title("Relation Sépale vs Pétale")
axs[0, 1].set_xlabel("Longueur Sépale")
axs[0, 1].set_ylabel("Longueur Pétale")

#  Heatmap Corrélation

corr = df.corr(numeric_only=True)

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    ax=axs[1, 0]
)
axs[1, 0].set_title("Matrice de Corrélation")


# 4Graphe animé

ax_anim = axs[1, 1]
ax_anim.set_title("Animation - Evolution Sepal Length")
ax_anim.set_xlim(0, len(df))
ax_anim.set_ylim(df["SepalLengthCm"].min(), df["SepalLengthCm"].max())

line, = ax_anim.plot([], [], lw=2)

xdata, ydata = [], []

def update(frame):
    xdata.append(frame)
    ydata.append(df["SepalLengthCm"].iloc[frame])
    line.set_data(xdata, ydata)
    return line,

ani = FuncAnimation(fig, update, frames=len(df), interval=50)

# Ajustement automatique
plt.tight_layout()
plt.show()
#sauvegarde dans un fichier png
plt.tight_layout()
plt.savefig("dashboard_iris.png", dpi=300)
print("\nDashboard sauvegardé sous dashboard_iris.png")