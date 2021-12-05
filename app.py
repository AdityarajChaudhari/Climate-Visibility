import numpy as np
from flask import Flask, render_template, request, jsonify
import pickle
import psycopg2
from flask_cors import CORS, cross_origin

app = Flask(__name__)
model = pickle.load(open('./ModelSaver/model.pkl', 'rb'))
print("Inside model")
scalar = pickle.load(open('./DataPreProcessing/Scalar.pkl', 'rb'))
print("inside scalar")


@cross_origin()
@app.route('/', methods=['GET'])
def home():
    print("Inside home page")
    return render_template('./home.html')


@cross_origin()
@app.route('/info', methods=['GET'])
def info():
    print("Inside info page")
    return render_template('./info.html')


@cross_origin()
@app.route('/developer', methods=['GET'])
def developer():
    print("Inside home page")
    return render_template('./developer.html')


@cross_origin()
@app.route('/contact', methods=['GET'])
def contact():
    print("Inside contact page")
    return render_template('./contact.html')


@cross_origin()
@app.route('/app', methods=['GET'])
def index_page():
    print("Inside app")
    return render_template('./index.html')


@cross_origin()
@app.route('/predict', methods=['POST','GET'])
def predict():
    print("Inside Predict")
    if request.method == 'POST':
        dry = np.log2(float(request.form['dry']))

        rel = float(request.form['rel'])

        spd = np.log2(float(request.form['spd']))

        dir = float(request.form['dir'])

        pre = np.log2(float(request.form['pre']))

        preci = float(request.form['preci'])

        month = request.form['mon']
        if month == 'August':
            month = 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        elif month == 'December':
            month = 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0
        elif month == 'February':
            month = 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0
        elif month == 'January':
            month = 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0
        elif month == 'July':
            month = 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0
        elif month == 'June':
            month = 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0
        elif month == 'March':
            month = 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0
        elif month == 'May':
            month = 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0
        elif month == 'November':
            month = 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0
        elif month == 'October':
            month = 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0
        elif month == 'September':
            month = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1
        else:
            month = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

        cols = ([[dry, rel, spd, dir, pre, preci, *month]])
        print(cols)
        scl = scalar.transform(cols)
        print(scl)
        pred = model.predict(scl)
        print(pred)

        if pred == np.array(1):
            return render_template('./result.html', Prediction_text = "There is No/Low Climate Visibility")
        elif pred == np.array(2):
            return render_template('./result.html', Prediction_text = "There is Medium/Moderate Climate Visibility")
        else:
            return render_template('./result.html', Prediction_text = "There is Good/High Climate Visibility")

    return render_template('./home.html')


if __name__ == "__main__":
    app.run(debug=True)