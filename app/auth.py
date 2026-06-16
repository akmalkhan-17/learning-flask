# ill be handling auth related routes here
from flask import Blueprint
from flask import render_template

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login")
def login():
    return render_template("login.html")


@auth_bp.route("/register")
def register():
    return "Register Page"
