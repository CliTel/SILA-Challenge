import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path


def nettoyer_valeurs_manquantes(df):
    for col in df.select_dtypes(include=np.number).columns:
        df[col].fillna(df[col].median(), inplace=True)
    for col in df.select_dtypes(include='object').columns:
        df[col].fillna(df[col].mode()[0], inplace=True)
    return df

def detecter_outliers_iqr(df, col):
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    outliers = df[(df[col] < Q1 - 1.5*IQR) | (df[col] > Q3 + 1.5*IQR)]
    return outliers

def creer_features(df):
    for col in df.select_dtypes(include=np.number).columns:
        df[f'{col}_mean'] = df[col].mean()
        df[f'{col}_median'] = df[col].median()
        df[f'{col}_std'] = df[col].std()
    return df

def exporter_csv_excel(df, nom_fichier):
    Path("output").mkdir(exist_ok=True)
    df.to_csv(f"output/{nom_fichier}.csv", index=False)

    with pd.ExcelWriter(f"output/{nom_fichier}.xlsx", engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='Data', index=False)
        workbook  = writer.book
        worksheet = writer.sheets['Data']
        # Format pour colonnes numériques
        fmt = workbook.add_format({'num_format':'#,##0.00'})
        for i, col in enumerate(df.select_dtypes(include=np.number).columns):
            worksheet.set_column(i, i, 15, fmt)

def visualisations(df, nom_dataset):
    numeric_cols = df.select_dtypes(include=np.number).columns
    # Histogrammes
    for col in numeric_cols:
        plt.figure(figsize=(6,4))
        sns.histplot(df[col], kde=True)
        plt.title(f"{col} - {nom_dataset}")
        plt.show()
    # Boxplots pour outliers
    for col in numeric_cols:
        plt.figure(figsize=(6,4))
        sns.boxplot(x=df[col])
        plt.title(f"{col} Boxplot - {nom_dataset}")
        plt.show()
    # Heatmap corrélations
    if len(numeric_cols) > 1:
        plt.figure(figsize=(8,6))
        sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm")
        plt.title(f"Corrélation - {nom_dataset}")
        plt.show()
datasets = {
    "Titanic": "data/titanic.csv",
    "Iris": "data/iris.csv",
    "Amazon": "data/amazon.csv",
    "Weather": "data/weather.csv"
}

for nom, chemin in datasets.items():
    print(f"\n--- Traitement {nom} ---")
    df = pd.read_csv(chemin)

    # Nettoyage valeurs manquantes
    df = nettoyer_valeurs_manquantes(df)

    # Détection outliers
    for col in df.select_dtypes(include=np.number).columns:
        outliers = detecter_outliers_iqr(df, col)
        print(f"{nom} - {col} outliers: {len(outliers)}")

    # Création features dérivées
    df = creer_features(df)

    # Export
    exporter_csv_excel(df, f"{nom}_clean")

    # Visualisations
    visualisations(df, nom)