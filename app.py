from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Bidirectional, LSTM, Dense
from survey import pic,pic1
from tensorflow.keras.models import load_model
app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        age = int(request.form['age'])
        sex = request.form.get('sex')
        cp = request.form.get('cp')
        trestbps = int(request.form['trestbps'])
        chol = int(request.form['chol'])
        fbs = request.form.get('fbs')
        restecg = int(request.form['restecg'])
        thalach = int(request.form['thalach'])
        exang = request.form.get('exang')
        oldpeak = float(request.form['oldpeak'])
        slope = request.form.get('slope')
        ca = int(request.form['ca'])
        thal = request.form.get('thal')
        data = pd.read_csv('heart1.csv')
        features = data.drop('target', axis=1).values
        scaler = MinMaxScaler()
        scaler.fit(features)
        new_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        print(new_data)
        new_data = scaler.transform(new_data)
        new_data = new_data.reshape((new_data.shape[0], new_data.shape[1], 1))
        loaded_model = load_model("CardioVascular.h5")
        predictions = loaded_model.predict(new_data)
        print(predictions)
        if predictions<0.5:
            predictions=" You are lucky you don't have a chance of heart disease."
            print("Detect")
        elif predictions>0.5:
            predictions="Oh no, you have a chance of heart disease"
            print("NotDetect")
        return render_template('result.html', prediction=predictions)
@app.route('/survey', methods=['GET','POST'])
def survey():
    image=pic()
    image=pic1()
    return render_template('survey.html')

if __name__ == '__main__':
    app.run(debug=False, port=300)
