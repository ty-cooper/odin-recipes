from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chicken-salad")
def chicken_salad():
    return render_template("chicken_salad.html")

@app.route("/pbj")
def pbj():
    return render_template("PBJ.html")

@app.route("/scrambled-eggs")
def scrambled_eggs():
    return render_template("scrambled_eggs.html")
