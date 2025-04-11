from flask import Flask, render_template, redirect, url_for
import glob, os

abc = [os.path.basename(x) for x in glob.glob("./templates/app/contests/abc/*")]

app = Flask(__name__)
#app.config.from_object("app.config")

@app.route("/")
def home():
	return render_template("app/index.html")

@app.route("/contests")
def contests():
	return render_template("app/contests/index.html")

@app.route("/contests/<name>")
def contest(name):
	if name in abc:
		return render_template(f"app/contests/abc/{name}/index.html")
	else:
		return redirect(url_for("contests"))