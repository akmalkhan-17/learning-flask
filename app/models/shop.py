from ..extensions import db


class Shop(db.Model):
    __tablename__ = "shops"

    id = db.Column(db.Integer, primary_key=True)
    
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    name = db.Column(db.String(80), unique=True, nullable=False)

    phone_number = db.Column(
        db.String(20), unique=True, nullable=False
    )  # we are not refrencing user number here as we would like the shop to have its own number

    address = db.Column(db.String(200), nullable=False)

    latitude = db.Column(db.Float, nullable=False)

    longitude = db.Column(db.Float, nullable=False)

    opening_time = db.Column(db.Time, nullable=False)

    closing_time = db.Column(db.Time, nullable=False)

    description = db.Column(db.Text, nullable=True)

    image_url = db.Column(db.String(200), nullable=True)

    owner = db.relationship("User", back_populates="shops") #this will help us do user.shops which will return all the shops of user and this is also not needed to use foreign key it is just convenient

    appointments = db.relationship("Appointment", back_populates="shop")  # this will create a relationship between the shop and the appointment, so that we can access the appointment of a shop by using shop.appointments

    services = db.relationship("Service", back_populates="shop", cascade="all, delete-orphan") # cascade all willl delete all the services if parent shop is deleted  
    
    
