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


pizza1 = Pizza(name="Cheese", ingredients="Dough, Tomato Sauce, Cheese")
pizza2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
pizza3 = Pizza(name="Margarita", ingredients="Dough, Tomato Sauce, Cheese, Basil")
pizza4 = Pizza(name="Vegetarian", ingredients="Dough, Tomato Sauce, Cheese, Vegetables")
pizza5 = Pizza(name="Hawaiian", ingredients="Dough, Tomato Sauce, Cheese, Ham, Pineapple")
pizza6 = Pizza(name="Meat Lover's", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni, Sausage, Bacon")


db.session.add_all([restaurant1, restaurant2, restaurant3, pizza1, pizza2, pizza3, pizza4, pizza5, pizza6])


price1 = 10.99
price2 = 12.99
price3 = 9.99
price4 = 11.99
price5 = 14.99
price6 = 13.99

restaurant_pizza1 = RestaurantPizza(restaurant=restaurant1, pizza=pizza1, price=price1)
restaurant_pizza2 = RestaurantPizza(restaurant=restaurant2, pizza=pizza2, price=price2)
restaurant_pizza3 = RestaurantPizza(restaurant=restaurant3, pizza=pizza3, price=price3)
restaurant_pizza4 = RestaurantPizza(restaurant=restaurant1, pizza=pizza4, price=price4)
restaurant_pizza5 = RestaurantPizza(restaurant=restaurant2, pizza=pizza5, price=price5)
restaurant_pizza6 = RestaurantPizza(restaurant=restaurant3, pizza=pizza6, price=price6)


db.session.add_all([restaurant_pizza1, restaurant_pizza2, restaurant_pizza3, restaurant_pizza4, restaurant_pizza5, restaurant_pizza6])


db.session.commit()

print("Sample restaurants, pizzas, and prices seeded successfully.")