from datetime import datetime
from ..extensions import db


class Appointment(db.Model):
    __tablename__ = "appointments"

    id = db.Column(db.Integer, primary_key=True)
    shop_id = db.Column(db.Integer, db.ForeignKey("shops.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey("services.id"), nullable=False)
    appointment_time = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), nullable=False, default="pending")
    queue_number = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    user = db.relationship("User",back_populates="appointments")  # this will create a relationship between the appointment and the user, so that we can access the user of an appointment by using appointment.user
    
    shop = db.relationship("Shop", back_populates="appointments")  # this will create a relationship between the appointment and the shop, so that we can access the shop of an appointment by using appointment.shop
    
    service = db.relationship("Service", back_populates="appointment")


class AppointmentStatus :
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELED = "canceled"
    COMPLETED = "completed"
    
		# now this will allow us to do status = AppointmentStatus.PENDING
    
