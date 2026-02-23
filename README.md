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
---




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

##
---






# JOUR 3  

# Projet Calculatrice Scientifique – Interface Graphique Tkinter  

---

## Description  

Ce projet consiste à créer une **calculatrice scientifique complète** en Python, en utilisant la bibliothèque **tkinter** pour l’interface graphique et le module **math** pour les calculs scientifiques.  

L’application permet d’effectuer des opérations mathématiques simples et avancées, de gérer les erreurs, d’afficher un historique scrollable des calculs et de basculer entre un **thème clair et un thème sombre**.

La calculatrice comprend :

- Les opérations de base `(+, −, ×, ÷)`  
- Les fonctions trigonométriques : `sin, cos, tan`  
- Les fonctions logarithmiques : `log`  
- La racine carrée `(sqrt)`  
- Les constantes mathématiques : `π` et `e` 
- La gestion des `parenthèses imbriquées`  
- Un historique des `calculs scrollable`  
- Un système de thème `clair/sombre`  
- La gestion des erreurs `(division par zéro, expressions invalides)`  

---

## Contenu des fichiers  

Le projet est structuré de manière modulaire pour une meilleure organisation du code :

- `main.py`  
  Script principal qui lance l’application Tkinter.

- `calculator/ui.py`  
  Gère l’interface graphique (boutons, affichage, historique, événements).

- `calculator/logic.py`  
  Contient la logique de calcul sécurisée avec restriction des fonctions autorisées.

- `calculator/theme.py`  
  Gère l’application des thèmes clair et sombre.

---

## Fonctionnalités  

- Création d’une interface graphique responsive avec tkinter  
- Organisation des boutons en grille dynamique  
- Gestion des expressions mathématiques complexes  
- Sécurisation de `eval()` pour limiter les fonctions autorisées  
- Gestion des erreurs :  
  - Division par zéro  
  - Expression invalide  
- Historique des calculs avec zone scrollable  
- Système de changement de thème (clair / sombre)  
- Code structuré en plusieurs fichiers (séparation des responsabilités)  

---

## Structure du projet  
 ```bash
 jour3_calculatrice/
│
├── main.py
├── calculator/
│ ├── init.py
│ ├── ui.py
│ ├── logic.py
│ └── theme.py
```
## Commandes pour exécuter le projet

- Vérifie que Python 3 est installé :

```bash 
python3 --version
```

- Si tu es sous Linux (Ubuntu / Kali), installe tkinter :

```bash
sudo apt update
sudo apt install python3-tk
```

- Place-toi dans le dossier du projet :

```bash
cd chemin/vers/nom_projet
```

- Lance l’application :

```bash
pyhon3 main.py
```
## Résultat de notre programme
- Une fenêtre graphique s’ouvre avec :

    - Un champ d’affichage pour les calculs

    - Des boutons scientifiques organisés en grille

    - Un historique scrollable des opérations

    - Un bouton de changement de thème

- Exemple d’utilisation :

```bash 
(5 + 3) * sin(0.5)

- Affichage 

(5 + 3) * sin(0.5) = 3.835404...

- En cas d\'erreur : 

`Erreur` : Division par zéro :

- Ou

`Erreur` : Expression invalide
```

## Points techniques importants

 - Utilisation de la programmation orientée objet (POO)

 - Séparation claire entre :

    - `Interface`

    - `Logique métier`

    - `Gestion du thème`

 - Sécurisation de l’évaluation des expressions

 - Interface responsive grâce au système grid de tkinter

---

## Conclusion

- Ce projet permet de mettre en pratique :

    - La création d’interfaces graphiques avec tkinter

    - La structuration modulaire d’un projet Python

    - La gestion des exceptions

    - L’intégration de fonctions mathématiques avancées

    - Les bonnes pratiques de développement

---


# Jour 5 – Simulateur de Poker Texas Hold’em

## Description

Ce projet implémente un **simulateur de poker Texas Hold’em** en **Python orienté objet (POO)**.
Le simulateur permet à un utilisateur de jouer contre des bots et inclut un **algorithme Monte Carlo** pour évaluer les probabilités de gain des mains.
Les cartes sont affichées en **ASCII dans le terminal** pour une expérience visuelle simple et ludique.

---

## Fonctionnalités

* Classes principales :

  * `Carte` : représente une carte du jeu (valeur et couleur)
  * `Deck` : représente le paquet de cartes avec mélange et tirage
  * `Main` : représente la main d’un joueur et évaluation de la force
  * `Joueur` : joueur humain ou bot avec cartes et bankroll

* **Simulation Monte Carlo** pour estimer la probabilité de gain d’une main.

* **Affichage ASCII** des cartes dans le terminal.

* **Moteur de jeu** permettant de jouer contre des bots.

* Gestion simple des tours : pré-flop, flop, turn, river.

---

## Arborescence du projet

```
jour5/
│
├── game.py           # Moteur principal du jeu
├── carte.py          # Classe Carte
├── deck.py           # Classe Deck
├── main.py           # Classe Main pour gérer les mains
├── joueur.py         # Classe Joueur
├── montecarlo.py     # Algorithme Monte Carlo
├── run.py            # Script principal pour lancer le jeu
└── README.md         # Documentation du projet
```

---

## Installation

1. **Cloner le projet** :

```bash
git clone <URL_DU_REPO>
cd jour5
```

2. **Installer Python 3** (>= 3.8 recommandé)

3. **Créer un environnement virtuel** :

```bash
python3 -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
```

4. **Installer les dépendances** :

```bash
pip install numpy
```

---

## Lancer le jeu

```bash
python run.py
```

* Suivez les instructions dans le terminal pour jouer contre les bots.
* Les cartes seront affichées en ASCII.
* Les probabilités de gain seront calculées automatiquement avec Monte Carlo.

---

## Algorithme Monte Carlo

* Simule un grand nombre de parties possibles pour estimer la probabilité de gagner avec la main actuelle.
* Permet au joueur de prendre des décisions plus stratégiques face aux bots.

---

## Exemple d’affichage

```
Vos cartes :
┌───┐ ┌───┐
| A♠ | | 10♥|
└───┘ └───┘

Cartes communes :
┌───┐ ┌───┐ ┌───┐
| K♣ | | 7♦ | | 2♠ |
└───┘ └───┘ └───┘

Probabilité de gain estimée : 45%
```

---

## Remarques

* Le projet est conçu pour être **modulaire et extensible** : possibilité d’ajouter plus de bots, différentes stratégies, ou une interface graphique future.
* Les probabilités sont calculées uniquement pour **des mains de 2 cartes** dans un jeu classique à 52 cartes.

---

