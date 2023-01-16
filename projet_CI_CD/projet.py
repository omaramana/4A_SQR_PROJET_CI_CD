from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == "check_syntax":
            print("Build [ OK ]")
            exit(0)
        else:
            print("Passed argument not supported ! Supported argument : check_syntax")
            exit(1)
    app.run(debug=True)

class Personne:
    def __init__(self, id, nom, prenom, solde):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.solde = solde

    def toString(self):
        return str(self.id) + ': ' + self.nom + ' ' + self.prenom + ' ' + str(self.solde)

class Transaction:
    def __init__(self, p1, p2, date, somme):
        self.p1 = p1
        self.p2 = p2
        self.date = date
        self.somme = somme

    def toString(self):
        return self.p1.nom + ' ' +  self.p2.nom + ' ' +  self.date + ' ' + str(self.somme)

transactions = [
     ("Omar", "Simo", "Jeudi 12 Janvier 2023", 50),
     ("Simo", "Omar", "Vendredi 13 Janvier 2023", 25),
     ("Benjamin", "Romain", "Lundi 25 Juin 2023", 76)
     ]

personnes = []

@app.route('/', methods=['GET'])
def home():
    return "Hello World !"