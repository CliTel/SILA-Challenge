import json
from datetime import datetime
from exceptions import SoldeInsuffisantError

class Compte:
    def __init__(self, numero, nom, solde=0):
        self.numero = numero
        self.nom = nom
        self.solde = solde
        self.historique = []

    def deposer(self, montant):
        self.solde += montant
        self.historique.append({
            "type": "Depot",
            "montant": montant,
            "date": str(datetime.now())
        })
        print(f"Tu as deposé {montant} fcfa. Nouveau solde: {self.solde}")
        self.sauvegarder()

    def retirer(self, montant):
        if montant > self.solde:
            raise SoldeInsuffisantError("Pas assez d'argent pour retirer !")
        self.solde -= montant
        self.historique.append({
            "type": "Retrait",
            "montant": montant,
            "date": str(datetime.now())
        })
        print(f"Tu as retiré {montant} fcfa. Nouveau solde: {self.solde}")
        self.sauvegarder()

    def virement(self, autre_compte, montant):
        if montant > self.solde:
            raise SoldeInsuffisantError("Pas assez d'argent pour le virement !")
        self.solde -= montant
        autre_compte.solde += montant
        self.historique.append({
            "type": f"Virement vers {autre_compte.numero}",
            "montant": montant,
            "date": str(datetime.now())
        })
        autre_compte.historique.append({
            "type": f"Virement reçu de {self.numero}",
            "montant": montant,
            "date": str(datetime.now())
        })
        print(f"Virement de {montant} fcfa vers le compte {autre_compte.numero}")
        self.sauvegarder()
        autre_compte.sauvegarder()

    def sauvegarder(self):
        try:
            with open("comptes.json", "r") as f:
                data = json.load(f)
        except:
            data = {}
        data[str(self.numero)] = {
            "nom": self.nom,
            "solde": self.solde,
            "historique": self.historique
        }
        with open("comptes.json", "w") as f:
            json.dump(data, f, indent=4)
