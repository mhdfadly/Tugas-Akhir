from web_ta import app
from flask import render_template, request, redirect

@app.route('/')
def home():
        return render_template('home.html')

@app.route('/knn/')
def knn():
        return render_template('knn.html')

@app.route('/nv_bayes/')
def nv_bayes():
        return render_template('nv_bayes.html')

@app.route('/rdm_forest/')
def rdm_forest():
        return render_template('rdm_forest.html')