from flask import Flask

app = Flask(__name__)

class Personne:
    def __init__(self, id, prenom, nom, solde):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.solde = solde

    def toString(self):
        return "Le client " + "<b>" + self.prenom + "</b>" + ' ' + "<b>" +self.nom +"</b>"+ " dont l'id est " + "<b>" +str(self.id) +"</b>"+ ' ' + "possède un solde de " + "<b>" + str(self.solde) + "</b>" + " euros."

class Transaction:
    def __init__(self, p1, p2, date, somme):
        self.p1 = p1
        self.p2 = p2
        self.date = date
        self.somme = somme

    def toString(self):
        return "Le client " + "<b>"+self.p1.nom+"</b>" +" a envoyé "+ "<b>"+str(self.somme)+"</b>" + " à "+ "<b>"+self.p2.nom+"</b>" + ' le ' + "<b>"+self.date+"</b>" + '.'


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

@app.route("/listeClients", methods=['GET'])
def listeClients():
    sortieEcran = "<h1>Liste des clients :</h1>\n"
    for personne in personnes:
        sortieEcran += "<p>" + personne.toString() + "</p>\n"
    return sortieEcran
