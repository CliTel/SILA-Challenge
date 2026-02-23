# montecarlo.py

from deck import Deck
from main import Main

def simulation_montecarlo(joueur_cartes, cartes_communes, iterations=1000):
    victoires = 0

    for _ in range(iterations):
        deck = Deck()
        deck.cartes = [
            c for c in deck.cartes
            if c not in joueur_cartes + cartes_communes
        ]

        adversaire = [deck.distribuer(), deck.distribuer()]

        communes = cartes_communes.copy()
        while len(communes) < 5:
            communes.append(deck.distribuer())

        main_joueur = Main(joueur_cartes + communes)
        main_adv = Main(adversaire + communes)

        # ✅ Utilise evaluate()
        if main_joueur.evaluate() > main_adv.evaluate():
            victoires += 1

    return round((victoires / iterations) * 100, 2)