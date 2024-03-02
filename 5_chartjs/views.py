#import de la bibliothèque
from flask import Flask, render_template
import datetime

#création de l'application
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/bar')
def barre():
    return render_template("bar.html")

@app.route('/plot')
def courbe():
    
    data = [{'masse': 57146.0, 'date': '2018-05-02T06:00:00', 'temp_ext': 9.12, 'temp2': 21.88, 'temp3': 27.99, 'humi': 64.6}, 
        {'masse': 57130.27, 'date': '2018-05-02T07:00:00', 'temp_ext': 9.01, 'temp2': 21.92, 'temp3': 28.02, 'humi': 66.23}, 
        {'masse': 57117.47, 'date': '2018-05-02T08:01:00', 'temp_ext': 9.03, 'temp2': 21.9, 'temp3': 28.13, 'humi': 64.76}, 
        {'masse': 57113.73, 'date': '2018-05-02T09:01:00', 'temp_ext': 9.48, 'temp2': 22.14, 'temp3': 28.3, 'humi': 64.16}, 
        {'masse': 57105.24, 'date': '2018-05-02T10:00:00', 'temp_ext': 10.22, 'temp2': 22.26, 'temp3': 28.45, 'humi': 66.14}, 
        {'masse': 57091.07, 'date': '2018-05-02T11:00:00', 'temp_ext': 11.51, 'temp2': 22.41, 'temp3': 28.4, 'humi': 64.02}, 
        {'masse': 57085.33, 'date': '2018-05-02T12:01:00', 'temp_ext': 13.51, 'temp2': 22.9, 'temp3': 27.88, 'humi': 59.67}, 
        {'masse': 56964.13, 'date': '2018-05-02T13:01:00', 'temp_ext': 16.27, 'temp2': 23.52, 'temp3': 27.3, 'humi': 58.62}, 
        {'masse': 56798.48, 'date': '2018-05-02T14:00:00', 'temp_ext': 23.85, 'temp2': 24.74, 'temp3': 27.24, 'humi': 59.66}, 
        {'masse': 56315.33, 'date': '2018-05-02T15:00:00', 'temp_ext': 28.0, 'temp2': 26.82, 'temp3': 28.37, 'humi': 63.78}, 
        {'masse': 56445.38, 'date': '2018-05-02T16:00:00', 'temp_ext': 21.24, 'temp2': 28.27, 'temp3': 29.53, 'humi': 66.81}, 
        {'masse': 56654.13, 'date': '2018-05-02T17:01:00', 'temp_ext': 17.62, 'temp2': 27.46, 'temp3': 30.82, 'humi': 65.44}, 
        {'masse': 56665.87, 'date': '2018-05-02T18:01:00', 'temp_ext': 16.82, 'temp2': 26.6, 'temp3': 31.34, 'humi': 63.4}, 
        {'masse': 56673.79, 'date': '2018-05-02T19:00:00', 'temp_ext': 15.99, 'temp2': 26.2, 'temp3': 31.52, 'humi': 62.72}, 
        {'masse': 56659.87, 'date': '2018-05-02T20:00:00', 'temp_ext': 15.03, 'temp2': 25.82, 'temp3': 31.45, 'humi': 62.21}, 
        {'masse': 56638.4, 'date': '2018-05-02T21:01:00', 'temp_ext': 14.28, 'temp2': 25.54, 'temp3': 31.67, 'humi': 66.1}, 
        {'masse': 56575.87, 'date': '2018-05-02T22:01:00', 'temp_ext': 13.08, 'temp2': 24.91, 'temp3': 31.79, 'humi': 62.95}, 
        {'masse': 56556.93, 'date': '2018-05-02T23:01:00', 'temp_ext': 12.18, 'temp2': 24.44, 'temp3': 31.92, 'humi': 66.23}, 
        {'masse': 56538.62, 'date': '2018-05-03T00:00:00', 'temp_ext': 11.36, 'temp2': 24.19, 'temp3': 31.84, 'humi': 64.8}, 
        {'masse': 56534.4, 'date': '2018-05-03T01:00:00', 'temp_ext': 10.8, 'temp2': 23.71, 'temp3': 31.47, 'humi': 66.35}]

    return render_template("plot.html", data = data)

@app.route('/multi')
def multi_courbe():
    return render_template("multi.html")


#lancement de l'application en mode debugage version Thonny
app.run(threaded=False, use_reloader=False, debug=True)
#lancement de l'application en mode debugage version classique
#app.run(debug=True)