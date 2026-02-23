# game.py

from deck import Deck
from joueur import Joueur
from main import Main
from montecarlo import simulation_montecarlo

class PokerGame:
    def __init__(self):
        self.deck = Deck()
        self.joueur = Joueur("Vous")
        self.bot = Joueur("Bot", bot=True)
        self.cartes_communes = []

    def distribuer_cartes(self):
        for _ in range(2):
            self.joueur.recevoir(self.deck.distribuer())
            self.bot.recevoir(self.deck.distribuer())

    def distribuer_communes(self):
        for _ in range(5):
            self.cartes_communes.append(self.deck.distribuer())

    def afficher_communes(self):
        lignes = [""] * 7
        for carte in self.cartes_communes:
            ascii_c = carte.ascii()
            for i in range(7):
                lignes[i] += ascii_c[i] + "  "
        for ligne in lignes:
            print(ligne)

    def jouer(self):
        self.distribuer_cartes()

        print("\nVos cartes :")
        self.joueur.afficher_cartes()

        self.distribuer_communes()

        print("\nCartes communes :")
        self.afficher_communes()

        proba = simulation_montecarlo(
            self.joueur.cartes,
            self.cartes_communes[:3]
        )

        print(f"\nProbabilité estimée de gain : {proba}%")

        main_joueur = Main(self.joueur.cartes + self.cartes_communes)
        main_bot = Main(self.bot.cartes + self.cartes_communes)

        if main_joueur.evaluate() > main_bot.evaluate():
            print("\n Vous gagnez !")
        elif main_joueur.evaluate() < main_bot.evaluate():
            print("\n Le bot gagne !")
        else:
            print("\n Égalité !")