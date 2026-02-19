# SILA-ChallengE

# JOUR 1 

# Projet Banque Python

## Description
Ce projet est un **système bancaire simple en Python** utilisant la programmation orientée objet (POO).  
Il permet de créer différents types de comptes, effectuer des dépôts, retraits et virements, et suivre l’historique des transactions.

---

## Contenu des fichiers

- `main.py` :  
  Contient le **script principal** pour exécuter le programme.  
  Permet de créer des comptes, faire des opérations (dépôt, retrait, virement) et afficher l’historique.

- `compte.py` :  
  Définit la **classe de base `Compte`**.  
  Gère le solde, les opérations de base (dépot, retrait) et l’historique des transactions.

- `compte_epargne.py` :  
  Définit la **classe `CompteEpargne`**, qui hérite de `Compte`.  
  Ajoute un **plafond de dépôt** spécifique aux comptes épargne.

- `compte_pro.py` :  
  Définit la **classe `ComptePro`**, qui hérite de `Compte`.  
  Permet des opérations adaptées aux comptes professionnels (par exemple virement plus libre).

- `exceptions.py` :  
  Contient les **exceptions personnalisées** utilisées dans le projet :  
  - `SoldeInsuffisantError` → déclenchée si le solde est insuffisant.  
  - `PlafondDepasserError` → déclenchée si le dépôt dépasse le plafond.

- `comptes.json` :  
  Fichier de **sauvegarde des comptes** et de l’historique des transactions en JSON.  
  Permet de **persister les données** même après la fermeture du programme.

---

## Resultat du programme apres Test


- `Tu as deposé 10000 fcfa. Nouveau solde: 60000':` :
- `Pas assez d'argent pour retirer !`
- `Virement de 30000 fcfa vers le compte 9665085667`
- `Historique tedy: [{'type': 'Depot', 'montant': 10000, 'date': '2026-02-18 21:34:19.804407'}, {'type': 'Virement vers 9665085667', 'montant': 30000, 'date': '2026-02-18 21:34:19.817764'}]`
- `Historique CliTel: [{'type': 'Virement reçu de 3640650897', 'montant': 30000, 'date': '2026-02-18 21:34:19.817782'}]`

##
##


# SILA-ChallengE

# JOUR 2

# Projet Visualisation de Données – Dashboard Multi-Graphiques

## Description
Ce projet consiste à créer un **tableau de bord multi-graphiques** avec Python, en utilisant les bibliothèques **pandas, numpy, matplotlib et seaborn**.  
Le projet utilise le **dataset Iris** et permet de visualiser les caractéristiques des fleurs avec différents types de graphiques et d’obtenir des statistiques descriptives.

Le tableau de bord comprend :

- Un **histogramme** de la longueur des sépales  
- Un **scatter plot** avec régression pour la relation sépales/pétales  
- Une **heatmap** de corrélation des variables numériques  
- Une **courbe animée** représentant l’évolution de la longueur des sépales  

Le projet calcule également **la moyenne, la médiane, l’écart-type et les quartiles** pour chaque colonne numérique.

---

## Contenu des fichiers

- `dashboard.py` :  
  Script principal qui charge le dataset, calcule les statistiques descriptives, crée le tableau de bord 2x2 et génère les graphiques.

- `Iris.csv` :  
  Dataset officiel **Iris** (disponible sur [Kaggle](https://www.kaggle.com/datasets)) contenant les colonnes :  
  - `Id` : identifiant de la fleur  
  - `SepalLengthCm` : longueur du sépale (cm)  
  - `SepalWidthCm` : largeur du sépale (cm)  
  - `PetalLengthCm` : longueur du pétale (cm)  
  - `PetalWidthCm` : largeur du pétale (cm)  
  - `Species` : espèce de la fleur (`Iris-setosa`, `Iris-versicolor`, `Iris-virginica`)  

---

## Fonctionnalités

- Lecture et traitement des données avec **pandas**  
- Calcul des **statistiques descriptives** : moyenne, médiane, écart-type, quartiles  
- Création d’un **dashboard 2x2** avec **matplotlib** et **seaborn** :  
  - Histogramme  
  - Scatter plot avec ligne de régression  
  - Heatmap de corrélation  
  - Graphe animé  
- **Annotations et mise en forme** : titres, axes, légendes  
- Sauvegarde du tableau de bord dans un fichier `dashboard_iris.png`

---

## Commandes pour exécuter le projet

1. Crée un **environnement virtuel** Python :
 
```bash
- python3 -m venv venv
- source venv/bin/activate
```

2. Installe **les bibliothèques nécessaires** :

```bash
- pip install pandas numpy matplotlib seaborn
```

3. Place **le fichier Iris.csv** dans le même **dossier que dashboard.py** : 

4. **Lance le script** : 

```bash
- python3 dashboard.py
```

5. Résultat de notre programme :  

- Les statistiques descriptives s’affichent dans le terminal
```bash
Moyenne :
 SepalLengthCm    5.843333
 SepalWidthCm     3.054000
 PetalLengthCm    3.758667
 PetalWidthCm     1.198667

Médiane :
 SepalLengthCm    5.80
 SepalWidthCm     3.00
 PetalLengthCm    4.35
 PetalWidthCm     1.30

Écart-type :
 SepalLengthCm    0.828066
 SepalWidthCm     0.433594
 PetalLengthCm    1.764420
 PetalWidthCm     0.763161

Quartiles :
       SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm
0.25            5.1           2.8           1.60           0.3
0.50            5.8           3.0           4.35           1.3
0.75            6.4           3.3           5.10           1.8

```
- Le dashboard multi-graphiques est sauvegardé dans :

`dashboard_iris.png`

## Tu peux ouvrir cette image pour visualiser :

- `L’histogramme des longueurs de sépales`

- `Le scatter plot avec régression`

- `La heatmap de corrélation`

- `La courbe animée de la longueur des sépales`