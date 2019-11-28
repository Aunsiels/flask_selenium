from flask import render_template

from app import app
from app.forms import LoginForm


@app.route("/")
def index():
    return "Hello World!"


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template("login.html", form=form)
