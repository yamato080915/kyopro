from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object("app.config")

@app.route("/")
def home():
	return render_template("app/index.html")

@app.route("/contests")
def contests():
	return render_template("app/contests/index.html")