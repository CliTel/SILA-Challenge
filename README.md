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
