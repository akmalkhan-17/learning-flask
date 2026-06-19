from flask_login import UserMixin
from .extensions import db


class User(
    UserMixin,
    db.Model
):  ##creates users table and the class should be singular as we are talking about single user object
    __tablename__ = "users"  # adding this line will allow us to specify the name of the table in the database, otherwise it will default to the name of the class and flask will automatically add an s

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(80), unique=True, nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    password = db.Column(db.String(120), nullable=False)


# now load model before returning the app
