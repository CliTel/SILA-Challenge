# deck.py

import random
from carte import Carte

class Deck:
    def __init__(self):
        self.cartes = [Carte(v, c)
                       for v in Carte.valeurs
                       for c in Carte.couleurs]
        self.melanger()

    def melanger(self):
        random.shuffle(self.cartes)

    def distribuer(self):
        return self.cartes.pop()