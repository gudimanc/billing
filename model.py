from enum import unique
from flask import current_app as app
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
class Products(db.Model):
    id = db.Column('product_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    price = db.Column(db.Integer())  

    def __init__(self,name,price):
        self.name=name
        self.price=price