# joueur.py

class Joueur:
    def __init__(self, nom, bot=False):
        self.nom = nom
        self.cartes = []
        self.bot = bot

    def recevoir(self, carte):
        self.cartes.append(carte)

    def reset(self):
        self.cartes = []

    def afficher_cartes(self):
        lignes = [""] * 7
        for carte in self.cartes:
            ascii_c = carte.ascii()
            for i in range(7):
                lignes[i] += ascii_c[i] + "  "
        for ligne in lignes:
            print(ligne)