from flask import Flask, render_template, redirect, url_for
import glob, os

abc = [os.path.basename(x) for x in glob.glob("./templates/app/contests/abc/*")]

app = Flask(__name__)
#app.config.from_object("app.config")
debug = "/kyopro" if os.getenv("FLASK_DEBUG") else ""
if os.getenv("FLASK_DEBUG"):
	@app.route("/")
	def debugger():
		return redirect(url_for("home"))

@app.route(f"{debug}/")
def home():
	return render_template("app/index.html")

@app.route(f"{debug}/contests")
def contests():
	return render_template("app/contests/index.html")

@app.route(f"{debug}/contests/<name>")
def contest(name):
	print(abc)
	if name in abc:
		return render_template(f"app/contests/abc/{name}/index.html")
	else:
		return redirect(url_for("contests"))