#import de la bibliothèque
from flask import Flask

#création de l'application
app = Flask(__name__)

#définition de la fonction à exécuter à la racine de l'application
@app.route('/')
def hello_world():
    return "Ceci est simplement un texte 'Hello World'!"


#lancement de l'application en mode debugage
app.run(debug=True)