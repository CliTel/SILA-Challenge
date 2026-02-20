# SILA-ChallengE  

# JOUR 3  

# Projet Calculatrice Scientifique – Interface Graphique Tkinter  

---

## Description  

Ce projet consiste à créer une **calculatrice scientifique complète** en Python, en utilisant la bibliothèque **tkinter** pour l’interface graphique et le module **math** pour les calculs scientifiques.  

L’application permet d’effectuer des opérations mathématiques simples et avancées, de gérer les erreurs, d’afficher un historique scrollable des calculs et de basculer entre un **thème clair et un thème sombre**.

La calculatrice comprend :

- Les opérations de base (+, −, ×, ÷)  
- Les fonctions trigonométriques : sin, cos, tan  
- Les fonctions logarithmiques : log  
- La racine carrée (sqrt)  
- Les constantes mathématiques : π et e  
- La gestion des parenthèses imbriquées  
- Un historique des calculs scrollable  
- Un système de thème clair/sombre  
- La gestion des erreurs (division par zéro, expressions invalides)  

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

    **Un champ d’affichage pour les calculs**

    **Des boutons scientifiques organisés en grille**

    **Un historique scrollable des opérations**

    **Un bouton de changement de thème**

- Exemple d’utilisation :

```bash 
(5 + 3) * sin(0.5)

- Affichage 

(5 + 3) * sin(0.5) = 3.835404...

- En cas d'erreur : 

Erreur : Division par zéro :

- Ou

Erreur : Expression invalide
```

## Points techniques importants

 - Utilisation de la programmation orientée objet (POO)

 - Séparation claire entre :

    - Interface

    - Logique métier

    - Gestion du thème

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
