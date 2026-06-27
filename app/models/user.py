from flask_login import UserMixin
from ..extensions import db


class User(
    UserMixin, db.Model
):  ##creates users table and the class should be singular as we are talking about single user object
    __tablename__ = "users"  # adding this line will allow us to specify the name of the table in the database, otherwise it will default to the name of the class and flask will automatically add an s

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(80), unique=True, nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    password = db.Column(db.String(120), nullable=False)

    role = db.Column(db.String(20), nullable=False, default="customer")

    shops = db.relationship("Shop", back_populates="owner")  # this will create a relationship between the user and the shop, so that we can access the shops of a user by using user.shops
    appointments = db.relationship("Appointment", back_populates="user")  # this will create a relationship between the user and the appointment, so that we can access the appointment of a user by using user.appointments
    #for now we'll use back_populates instead of backref


# now load model before returning the app
