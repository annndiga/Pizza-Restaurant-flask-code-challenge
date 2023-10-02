from app import app, db
from models import Restaurant, Pizza, RestaurantPizza

# Initialize the app context
app.app_context().push()


db.create_all()


restaurant1 = Restaurant(name="Sottocasa NYC", address="298 Atlantic Ave, Brooklyn, NY 11201")
restaurant2 = Restaurant(name="PizzArte", address="69 W 55th St, New York, NY 10019")
restaurant3 = Restaurant(name="Slice Pizzeria", address="123 Main St, Boston, MA 02101")
restaurant4 = Restaurant(name="Pizza Palace", address="456 Elm St, San Francisco, CA 94101")
restaurant5 = Restaurant(name="Mama Mia's", address="789 Oak St, Chicago, IL 60601")
restaurant6 = Restaurant(name="Pizza Hut", address="123 Elm St, Los Angeles, CA 90001")
restaurant7 = Restaurant(name="Domino's Pizza", address="456 Oak St, Miami, FL 33101")
restaurant8 = Restaurant(name="Little Caesars", address="789 Maple St, Denver, CO 80201")


pizza1 = Pizza(name="Cheese", ingredients="Dough, Tomato Sauce, Cheese")
pizza2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
pizza3 = Pizza(name="Margarita", ingredients="Dough, Tomato Sauce, Cheese, Basil")
pizza4 = Pizza(name="Vegetarian", ingredients="Dough, Tomato Sauce, Cheese, Vegetables")
pizza5 = Pizza(name="Hawaiian", ingredients="Dough, Tomato Sauce, Cheese, Ham, Pineapple")
pizza6 = Pizza(name="Meat Lover's", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni, Sausage, Bacon")
pizza7 = Pizza(name="Veggie Delight", ingredients="Dough, Tomato Sauce, Cheese, Mixed Vegetables")
pizza8 = Pizza(name="BBQ Chicken", ingredients="Dough, BBQ Sauce, Cheese, Chicken, Red Onion")
pizza9 = Pizza(name="Supreme", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni, Sausage, Green Pepper, Onion, Olives")

db.session.add_all([restaurant1, restaurant2, restaurant3, pizza1, pizza2, pizza3, pizza4, pizza5, pizza6])


price1 = 10.99
price2 = 12.99
price3 = 9.99
price4 = 11.99
price5 = 14.99
price6 = 13.99
price7 = 15.99
price8 = 13.49
price9 = 14.99

restaurant_pizza1 = RestaurantPizza(restaurant=restaurant1, pizza=pizza1, price=price1)
restaurant_pizza2 = RestaurantPizza(restaurant=restaurant2, pizza=pizza2, price=price2)
restaurant_pizza3 = RestaurantPizza(restaurant=restaurant3, pizza=pizza3, price=price3)
restaurant_pizza4 = RestaurantPizza(restaurant=restaurant1, pizza=pizza4, price=price4)
restaurant_pizza5 = RestaurantPizza(restaurant=restaurant2, pizza=pizza5, price=price5)
restaurant_pizza6 = RestaurantPizza(restaurant=restaurant3, pizza=pizza6, price=price6)
restaurant_pizza7 = RestaurantPizza(restaurant=restaurant4, pizza=pizza7, price=price7)
restaurant_pizza8 = RestaurantPizza(restaurant=restaurant5, pizza=pizza8, price=price8)
restaurant_pizza9 = RestaurantPizza(restaurant=restaurant6, pizza=pizza9, price=price9)

db.session.add_all([restaurant6, restaurant7, restaurant8, pizza7, pizza8, pizza9,
                    restaurant_pizza7, restaurant_pizza8, restaurant_pizza9])


db.session.commit()

print("Sample restaurants, pizzas, and prices seeded successfully.")