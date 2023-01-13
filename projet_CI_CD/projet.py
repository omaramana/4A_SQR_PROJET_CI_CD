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
    
transactions = [
     ("Omar", "Simo", "Jeudi 12 Janvier 2023", 50),
     ("Simo", "Omar", "Vendredi 13 Janvier 2023", 25),
     ("Benjamin", "Romain", "Lundi 25 Juin 2023", 76)
     ]


@app.route('/', methods=['GET'])
def home():
    return "Hello World !"

