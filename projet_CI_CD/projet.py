from flask import Flask

app = Flask(__name__)

class Personne:
    def __init__(self, id, nom, prenom, solde):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.solde = solde

class Transaction:
    def __init__(self, p1, p2, date, somme):
        self.p1 = p1
        self.p2 = p2
        self.date = date
        self.somme = somme

personne0 = Personne(0, "Mohamed", "El Amri", 500)
personne1 = Personne(1, "Omar", "Amana", 120)
personne2 = Personne(2, "Karim", "Benzema", 120000)
personne3 = Personne(3, "Valerie", "Pecresse", -5000000)

personnes = [personne0, personne1, personne2, personne3]
transactions = []

@app.route('/', methods=['GET'])
def home():
    sortieEcran = "<h1> Bienvenue sur l'API de gestion des transactions !<h1>"
    return sortieEcran

