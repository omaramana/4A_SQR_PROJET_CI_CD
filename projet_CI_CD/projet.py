from flask import Flask
from operator import attrgetter
import sys 

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
        return "Le client " + "<b>"+self.p1.nom+"</b>" +" a envoyé "+ "<b>"+str(self.somme)+"</b>" +" euros "+ " à "+ "<b>"+self.p2.nom+"</b>" + ' le ' + "<b>"+self.date+"</b>" + '.'


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

@app.route("/ajouterTransaction/<int:id1>/<int:id2>/<date>/<int:somme>")
def ajouterTransaction(id1, id2, date, somme):
    sortieEcran = "<h1>La transaction effectuée est la suivante : </h1>\n"
    transactions.append(Transaction(personnes[int(id1)], personnes[int(id2)], date, int(somme)))
    transactions.sort(key=attrgetter('date'))
    sortieEcran += transactions[-1].toString() + listeClients()
    return sortieEcran

@app.route("/listeTransactions", methods=['GET'])
def afficherTransactions():
    sortieEcran = "<h3>Liste des transactions :</h3>\n"
    for transaction in transactions:
        transactions.sort(key=attrgetter('date'))
        sortieEcran += "<p>" + transaction.toString() + "</p>\n"
    return sortieEcran

@app.route("/listeTransactionPourUnClient/<int:id>", methods=['GET'])
def listeTransactionPourUnClient(id):
    sortieEcran = "<h3>Liste des transactions du client "+str(personnes[int(id)].nom)+" "+str(personnes[int(id)].prenom)+" est :</h3>\n"
    for transaction in transactions:
        if transaction.p1 == personnes[int(id)]:
            sortieEcran += "<p>" + transaction.toString() + "</p>\n"
    return sortieEcran

@app.route("/soldeUnClient/<int:id>", methods=['GET'])
def soldeUnClient(id):
    sortieEcran = "<h3>Le solde restant pour le client "+str(personnes[int(id)].nom)+" "+str(personnes[int(id)].nom)+" est : </h3>\n"
    sortieEcran += str(personnes[int(id)].solde)
    return sortieEcran

@app.route("/importerDepuisCSV/personnes", methods=['POST'])
def listerClientsCSV():
    if request.files:
        file = request.files['personnes']
        filepath = os.path.join(file.filename)
        file.save(filepath)

        with open(clients.csv) as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                personnes.append(Personne(len(personnes), row[0], row[1], int(row[2])))
    else:
        print("Une erreur s'est produite.")    
    return listeClients()

@app.route("/importerDepuisCSV/transactions", methods=['POST'])
def listerTransactionsCSV():
    if request.files:
        file = request.files['transactions']
        filepath = os.path.join(file.filename)
        file.save(filepath)

        with open(transactions.csv) as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                ajouterTransaction(int(row[0]), int(row[1]), row[2], int(row[3]))
    else:
        print("Une erreur s'est produite.")      
    return afficherTransactions()

