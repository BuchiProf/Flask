from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
@app.route('/<nom>')
def demo(nom=None):
  date = datetime.datetime.now()
  h = date.hour
  m = date.minute
  s = date.second
  return render_template("index.html", heure = h, minute = m, seconde = s, name=nom)

app.run(debug=True)