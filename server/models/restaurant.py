##restaurant.py

from .dbconfig import db

class Restaurant(db.Model):
    __tablename__ = 'restaurant'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    
    # Define the relationship with RestaurantPizza
    pizzas = db.relationship('RestaurantPizza', back_populates='restaurant')
