from flask import Flask, request

app = Flask(_name_)

@app.route("/")
def home():
    return "Welcome to Heroku!"

@app.route("/someendpoints")
def firstendpoint():
    return "This is my first path on heorku"

if _name_ == "_main_":
    @app.run()