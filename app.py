from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/characters")
def characters():
    return render_template("characters.html")

@app.route("/characters/jittik")
def jittik():
    return render_template("characters/jittik.html")

@app.route("/characters/kaelin")
def kaelin():
    return render_template("characters/milo2.html")

@app.route("/characters/milo")
def milo():
    return render_template("characters/milo.html")

@app.route("/characters/lucien")
def lucien():
    return render_template("characters/lucien.html")

@app.route("/characters/al")
def al():
    return render_template("characters/al.html")

@app.route("/campaigns")
def campaigns():
    return render_template("campaigns.html")

@app.route("/items")
def items():
    return render_template("items.html")


