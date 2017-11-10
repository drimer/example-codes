from datetime import datetime

from database import db


class Person(db.Model):
    __tablename__ = 'Person'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(300))
    phone_number = db.Column(db.String(30), unique=True)
    created = db.Column(db.DateTime, default=datetime.now)
