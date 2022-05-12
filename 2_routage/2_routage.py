from flask import Flask, request

app = Flask(__name__)

#pour transettre un paramètre dans l'URL
@app.route('/parametre/<param>')
def montrer_parametre(param):
    return f"Le paramètre en plus est {param}"

#pour prendre la query string dans l'URL /formulaire?nom=Marchal&prenom=Louis
@app.route('/formulaire')
def formulaire():
    valeur_nom = request.args.get('nom')
    valeur_prenom = request.args.get('prenom')
    return f"Les paramètre reçus : Nom = {valeur_nom} et prénom = {valeur_prenom}"


app.run(debug=True)