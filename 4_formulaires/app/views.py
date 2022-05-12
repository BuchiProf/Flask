from urllib import request
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
 return render_template('index.html')

@app.route('/resultat', methods=['GET', 'POST'])
def demo():
    if request.method == 'GET':
        donnee = request.args
        m = 'GET'
    elif request.method == 'POST':
        donnee = request.form
        m = 'POST'
    p = donnee['prenom']
    n = donnee['nom']
    return render_template("resultat.html", firstname=p, method=m,  lastname=n)


app.run(debug=True)
