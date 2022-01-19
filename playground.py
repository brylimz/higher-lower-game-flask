from flask import Flask
from functools import wraps
# set FLASK_APP = playground.py
# $env:FLASK_APP = "playground.py"
app = Flask(__name__)



@app.route("/")
def hello_world():
    return '<h1 style="text-align:center"> Hello World </h1>' \
           '<p> This is a paragraph </p>' \
           '<img src="https://c.tenor.com/ZhfMGWrmCTcAAAAM/cute-kitty-best-kitty.gif" </img>' \
           ''

# creating vairable paths and converting the path to a specified data type


def makebold(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        return "<h1>" + fn(*args, **kwargs) + "</h1>"
    return wrapper

#different routes using the app.route decorator


@makebold
@app.route("/bye")
def bye():
    return "bye"



@app.route("/username/<name>/<int:number>")
def best(name, number):
    return f"hello there {name}. you are {number} years old!"


if __name__ == "__main__":
    app.run(debug=True)
