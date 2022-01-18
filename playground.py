from flask import Flask
# set FLASK_APP = playground.py
# $env:FLASK_APP = "playground.py"
app = Flask(__name__)


@app.route("/")
def home():
    return "hello"


@app.route("/username/<name>/<int:number>")
def best(name, number):
    return f"hello there {name}. you are {number} years old!"


if __name__ == "__main__":
    app.run(debug=True)
