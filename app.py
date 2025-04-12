from flask import Flask, render_template, redirect, url_for, jsonify
import glob, os, requests

abc = [os.path.basename(x) for x in glob.glob("./templates/app/contests/abc/*")]

app = Flask(__name__)
#app.config.from_object("app.config")
debug = "/kyopro/" if os.getenv("FLASK_DEBUG") else "/"

@app.route(f"{debug}")
def home():
	return render_template("app/index.html")

@app.route(f"{debug}atcoder_rating")
def graph():
    data = requests.get("https://atcoder.jp/users/yamato0915/history/json")
    data = data.json()
    data = [x for x in data if x["IsRated"]]
    return jsonify(data)

@app.route(f"{debug}contests")
def contests():
	return render_template("app/contests/index.html")

@app.route(f"{debug}contests/<name>")
def contest(name):
	print(abc)
	if name in abc:
		return render_template(f"app/contests/abc/{name}/index.html")
	else:
		return redirect(url_for("contests"))