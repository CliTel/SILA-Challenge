# main.py

from collections import Counter

class Main:

    RANK_ORDER = {v: i for i, v in enumerate(
        ['2', '3', '4', '5', '6', '7', '8',
         '9', '10', 'J', 'Q', 'K', 'A'], start=2)
    }

    def __init__(self, cartes):
        self.cartes = cartes

    def evaluate(self):
        values = sorted(
            [self.RANK_ORDER[c.valeur] for c in self.cartes],
            reverse=True
        )
        suits = [c.couleur for c in self.cartes]

        value_count = Counter(values)
        suit_count = Counter(suits)

        is_flush = max(suit_count.values()) >= 5
        is_straight, straight_high = self.check_straight(values)

        counts = sorted(
            value_count.items(),
            key=lambda x: (-x[1], -x[0])
        )

        # Quinte Flush
        if is_flush and is_straight:
            return (8, straight_high)

        # Carré
        if counts[0][1] == 4:
            return (7, counts[0][0])

        # Full House
        if counts[0][1] == 3 and counts[1][1] >= 2:
            return (6, counts[0][0], counts[1][0])

        # Couleur
        if is_flush:
            return (5, values[:5])

        # Quinte
        if is_straight:
            return (4, straight_high)

        # Brelan
        if counts[0][1] == 3:
            return (3, counts[0][0])

        # Double Paire
        if counts[0][1] == 2 and counts[1][1] == 2:
            return (2, counts[0][0], counts[1][0])

        # Paire
        if counts[0][1] == 2:
            return (1, counts[0][0])

        # Carte haute
        return (0, values[:5])

    def check_straight(self, values):
        unique = sorted(set(values), reverse=True)

        # Cas spécial A-2-3-4-5
        if {14, 2, 3, 4, 5}.issubset(set(values)):
            return True, 5

        for i in range(len(unique) - 4):
            if unique[i] - unique[i+4] == 4:
                return True, unique[i]

        return False, None