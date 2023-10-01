from flask import Flask
from flask_cors import CORS
from dbconfig import db  
from flask_migrate import Migrate
from models import Pizza, Restaurant, RestaurantPizza
import os 

app = Flask(__name__)
CORS(app, resources={r"/restaurants*": {"origins": "http://localhost:3000"}})


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurant.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return 'Happy Pizza Shopping!'

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
                "name": pizza.pizza.name,  
                "ingredients": pizza.pizza.ingredients
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

    if restaurant is None:
        return jsonify({'message': 'Restaurant not found'}), 404

    # Delete the restaurant from the database
    db.session.delete(restaurant)
    db.session.commit()

    return jsonify({'message': 'Restaurant deleted successfully'}), 200

@app.route('/pizzas', methods=['GET'])
def get_all_pizzas():
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

@app.route('/restaurant_pizzas', methods=['GET'])
def get_all_restaurant_pizzas():
    # Fetch all RestaurantPizza entries
    restaurant_pizzas = RestaurantPizza.query.all()
    
    #  a list to store the response data
    response_data = []

    for restaurant_pizza in restaurant_pizzas:
        # Get data from the RestaurantPizza entry
        pizza_id = restaurant_pizza.pizza_id
        restaurant_id = restaurant_pizza.restaurant_id

        # Fetch associated Pizza and Restaurant data
        pizza = Pizza.query.get(pizza_id)
        restaurant = Restaurant.query.get(restaurant_id)

        if pizza and restaurant:
            # a dictionary for the response data
            entry_data = {
                "pizza_id": pizza_id,
                "restaurant_id": restaurant_id,
                "price": restaurant_pizza.price,
                "pizza": {
                    "id": pizza.id,
                    "name": pizza.name,
                    "ingredients": pizza.ingredients
                },
                "restaurant": {
                    "id": restaurant.id,
                    "name": restaurant.name,
                    "address": restaurant.address
                }
            }
            response_data.append(entry_data)

    return jsonify(response_data), 200

@app.route('/restaurant_pizzas/<int:id>', methods=['GET'])
def get_restaurant_pizza_by_id(id):
    # Fetch the RestaurantPizza entry by ID
    restaurant_pizza = RestaurantPizza.query.get(id)

    if restaurant_pizza:
        # Get data from the RestaurantPizza entry
        pizza_id = restaurant_pizza.pizza_id
        restaurant_id = restaurant_pizza.restaurant_id

        # Fetch associated Pizza and Restaurant data
        pizza = Pizza.query.get(pizza_id)
        restaurant = Restaurant.query.get(restaurant_id)

        if pizza and restaurant:
            # a dictionary for the response data
            response_data = {
                "pizza_id": pizza_id,
                "restaurant_id": restaurant_id,
                "price": restaurant_pizza.price,
                "pizza": {
                    "id": pizza.id,
                    "name": pizza.name,
                    "ingredients": pizza.ingredients
                },
                "restaurant": {
                    "id": restaurant.id,
                    "name": restaurant.name,
                    "address": restaurant.address
                }
            }
            return jsonify(response_data), 200
        else:
            return jsonify({"error": "Pizza or Restaurant not found"}), 404
    else:
        return jsonify({"error": "RestaurantPizza not found"}), 404

@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    try:
        data = request.get_json()  

      
        price = data.get('price')
        pizza_id = data.get('pizza_id')
        restaurant_id = data.get('restaurant_id')

       
        restaurant_pizza = RestaurantPizza(
            price=price,
            pizza_id=pizza_id,
            restaurant_id=restaurant_id
        )

       
        db.session.add(restaurant_pizza)
        db.session.commit()

        pizza = Pizza.query.get(pizza_id)
        if pizza:
            pizza_data = {
                "id": pizza.id,
                "name": pizza.name,
                "ingredients": pizza.ingredients
            }
            return jsonify(pizza_data), 201  

        return jsonify({"error": "Pizza not found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 400 

if __name__ == '__main__':
    app.run(port=5555, debug=True)
   

        