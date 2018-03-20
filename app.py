from flask import Flask, render_template, url_for, request

app = Flask(__name__)


array = ["Pera", "Mika", "Ana", "Janko"]

@app.route("/")
def index():
	return render_template("index.html")
@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/hello/<string:name>/<int:guess>")
def hello(name, guess):
	name =  name.capitalize()
	return render_template("hello.html", name=name, guess=guess) 

@app.route("/users")
def users():
	return render_template("users.html", users=array)

@app.route("/submit", methods=['GET'])
def submit():
	return render_template("submit.html")

@app.route("/submit", methods=['POST'])
def submit_post():
	name = request.form.get("name")
	link = request.form.get("link")
	return render_template("submited.html", name=name, link=link)


