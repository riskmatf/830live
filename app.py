from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "Hello world!"

@app.route("/about")
def about():
	return "Flask demo app"

@app.route("/hello/<string:name>")
def hello(name):
	name =  name.capitalize()
	return "Hello " + name + "!"
