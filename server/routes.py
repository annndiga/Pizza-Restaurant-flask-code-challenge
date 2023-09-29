from flask import Flask, current_app, make_response, request, jsonify, g
from models.dbconfig import db  # Import the db object
from models.restaurant import Restaurant
from models.pizza import Pizza
from models.association import RestaurantPizza
from flask_cors import CORS
import os 


def create_app():
    # create the flask app 
    app = Flask(__name__)
    # allow CORS for all routes 
    CORS(app)
    app.config.from_object('config.Config')
    db.init_app(app)

    # sample request hook 
    @app.before_request
    def app_path():
        g.path = os.path.abspath(os.getcwd())

    # Route to get a list of restaurants
    @app.route('/restaurants', methods=['GET'])
    def get_restaurants():
        restaurants = Restaurant.query.all()
        restaurant_data = [
            {
                "id": restaurant.id,
                "name": restaurant.name,
                "address": restaurant.address
            }
            for restaurant in restaurants
        ]
        return jsonify(restaurant_data)

    # Route to get restaurant details by ID
    @app.route('/restaurants/<int:id>', methods=['GET'])
    def get_restaurant_by_id(id):
        restaurant = Restaurant.query.get(id)
        if restaurant:
            # Fetch associated pizzas for the restaurant
            pizzas = [
                {
                    "id": pizza.id,
                    "name": pizza.name,
                    "ingredients": pizza.ingredients
                }
                for pizza in restaurant.pizzas
            ]
            restaurant_data = {
                "id": restaurant.id,
                "name": restaurant.name,
                "address": restaurant.address,
                "pizzas": pizzas
            }
            return jsonify(restaurant_data)
        else:
            return jsonify({"error": "Restaurant not found"}), 404

    # Route to delete a restaurant by ID
    @app.route('/restaurants/<int:id>', methods=['DELETE'])
    def delete_restaurant_by_id(id):
        restaurant = Restaurant.query.get(id)
        if restaurant:
            # Delete associated restaurant pizzas
            RestaurantPizza.query.filter_by(restaurant_id=id).delete()
            # Delete the restaurant
            db.session.delete(restaurant)
            db.session.commit()
            return jsonify({}), 204
        else:
            return jsonify({"error": "Restaurant not found"}), 404

    # Route to get a list of pizzas
    @app.route('/pizzas', methods=['GET'])
    def get_pizzas():
        pizzas = Pizza.query.all()
        pizza_data = [
            {
                "id": pizza.id,
                "name": pizza.name,
                "ingredients": pizza.ingredients
            }
            for pizza in pizzas
        ]
        return jsonify(pizza_data)

    # Route to create a new restaurant pizza
    @app.route('/restaurant_pizzas', methods=['POST'])
    @app.route('/restaurant_pizzas', methods=['POST'])
    def create_restaurant_pizza():
        data = request.get_json()
        price = data.get('price')
        pizza_id = data.get('pizza_id')
        restaurant_id = data.get('restaurant_id')

        # Access the db object via current_app
        db = current_app.db

        # Validate input data here, e.g., check if pizza_id and restaurant_id exist

        # Create a new RestaurantPizza
        restaurant_pizza = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
        db.session.add(restaurant_pizza)

        try:
            db.session.commit()
            return jsonify({
                "id": restaurant_pizza.id,
                "name": restaurant_pizza.pizza.name,
                "ingredients": restaurant_pizza.pizza.ingredients
            }), 201
        except Exception as e:
            return jsonify({"errors": ["validation errors"]}), 400