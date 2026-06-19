# ill be handling auth related routes here
from flask import Blueprint, render_template, request
from .models import User
from .extensions import db, bcrypt


auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/")
def home():
    return render_template("home.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if not email or not password:
          return "All fields are required."
    
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
          return f"Welcome back, {user.username}!"
        else:
            return "Invalid email or password."

    return render_template("login.html")


@auth_bp.route("/usersdb")
def usersdb():
    users = User.query.all()
    return render_template("usersdb.html", users=users)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Handle form submission
        # print(request.form)  # Debugging: print the form data to the console
        username = request.form.get("username")
        email = request.form["email"]
        password = request.form["password"]

        # integrity checks
        existing_user = (
            User.query.filter_by(email=email).first()
            or User.query.filter_by(username=username).first()
        )  # Check if a user with the same email or username already exists

        if existing_user:
            return "A user with that email or username already exists."
        if not username or not email or not password:
            return "All fields are required."

        # hashinggg
        hashed_password = bcrypt.generate_password_hash(password).decode(
            "utf-8"
        )  # Hash the password decode converts the bytes object to a string

        user = User(  # this simply created a python object of the User class
            username=username, email=email, password=hashed_password
        )

        db.session.add(
            user
        )  # this like adding the user temporarily like adding something to cart
        db.session.commit()

        # users = User.query.all()
        # for user in users:
        #     print(user.username, user.email, user.password)  # Debugging: print all users to the console

        # Here you would typically save the user to the database
        return f"User registered: {username}, {email}"
    return render_template("register.html")
