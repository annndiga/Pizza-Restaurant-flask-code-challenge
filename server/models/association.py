## model.association.py
from .dbconfig import db


class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant-pizza'
    
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False, CheckConstraint('price >= 1 AND price <= 30'))
    
    # Define foreign keys
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)
    
    # Define relationships
    restaurant = db.relationship('Restaurant', back_populates='pizzas')
    pizza = db.relationship('Pizza', back_populates='restaurants')
