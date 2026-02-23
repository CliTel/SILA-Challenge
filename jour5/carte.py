# carte.py

class Carte:
    valeurs = ['2', '3', '4', '5', '6', '7', '8', '9',
               '10', 'J', 'Q', 'K', 'A']
    couleurs = ['♠', '♥', '♦', '♣']

    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __repr__(self):
        return f"{self.valeur}{self.couleur}"

    def __eq__(self, other):
        return self.valeur == other.valeur and self.couleur == other.couleur

    def __hash__(self):
        return hash((self.valeur, self.couleur))

    def ascii(self):
        return [
            "┌─────────┐",
            f"│{self.valeur:<2}       │",
            "│         │",
            f"│    {self.couleur}    │",
            "│         │",
            f"│       {self.valeur:>2}│",
            "└─────────┘"
        ]