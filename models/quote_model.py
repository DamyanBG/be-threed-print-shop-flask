from sqlalchemy import func

from db import db


class QuoteModel(db.Model):
    __tablename__ = "quotes"

    pk = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.DateTime, server_default=func.now())
    customer_names = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255))
    file_path = db.Column(db.String(255), nullable=False)
