from compte import Compte
from exceptions import PlafondDepasserError

class CompteEpargne(Compte):
    def __init__(self, numero, nom, solde=0):
        super().__init__(numero, nom, solde)
        self.plafond = 1000000  

    def deposer(self, montant):
        if self.solde + montant > self.plafond:
            raise PlafondDepasserError(f"Depot trop grand! Plafond = {self.plafond}")
        super().deposer(montant)
