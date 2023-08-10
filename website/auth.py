from flask import Blueprint, render_template, redirect, url_for
from website.forms import LoginForm

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = form.username.data
        return redirect(url_for("views.home", user=user))
    return render_template("login.html", form=form)


@auth.route("/logout", methods=["GET", "POST"])
def logout():
    return "logout"


@auth.route("/sign-up", methods=["GET", "POST"])
def signup():
    return render_template("sign_up.html")
