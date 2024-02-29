#import de la bibliothèque
from flask import Flask, render_template

#création de l'application
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


#lancement de l'application en mode debugage version Thonny
app.run(threaded=False, use_reloader=False, debug=True)
#lancement de l'application en mode debugage version classique
#app.run(debug=True)