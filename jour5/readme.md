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

