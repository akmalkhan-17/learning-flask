from ..extensions import db

class Service(db.Model):
		__tablename__ = "services"

		id = db.Column(db.Integer, primary_key=True)
		shop_id = db.Column(db.Integer, db.ForeignKey("shops.id"), nullable=False)
		name = db.Column(db.String(80), nullable=False)
		price = db.Column(db.Float, nullable=False)
		duration = db.Column(db.Integer, nullable=False)  # duration in minutes

		shop = db.relationship("Shop", back_populates="services")
		appointment = db.relationship("Appointment", back_populates="service")  