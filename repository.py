import json

class CompteRepository:
    def __init__(self, fichier="comptes.json"):
        self.fichier = fichier

    def sauvegarder(self, compte_data):
        try:
            with open(self.fichier, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {}

        data[str(compte_data["numero"])] = compte_data

        with open(self.fichier, "w") as f:
            json.dump(data, f, indent=4)
