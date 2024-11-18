# Adam Lindberg
# UWYO COSC 1010
# 11/12/24
# Lab 09
# Lab Section: 10
# Sources, people worked with, help given to:
# Your
# Comments
# Here

# Classes
# For this assignment, you will be creating two classes:
# One for Pizza
# One for a Pizzeria


# You will be creating a Pizza class. It should have the following attributes:
# - Size
# - Sauce
# - Toppings, which should be a list
# You need to create one method that corresponds with each of the above attributes
# which returns the corresponding attribute, just the value.
# For the size and toppings attributes, you will need to have a method to set them.
# - For Size, ensure it is an int > 10 (inches)
#   - If it is not, default to a 10" pizza (you can store ten). These checks should occur in init as well.
# - For toppings, you will need to add the toppings.
#   - This method needs to be able to handle multiple values.
#   - Append all elements to the list.
# Create a method that returns the amount of toppings.
# In your __init__() method, you should take in size and sauce as parameters.
# - Sauce should have a default value of red.
# - Size will not have a default value; use the parameter with the same safety checks defined above (you can use the set method).
# Within __init__(), you will need to:
# - Assign the parameter for size to a size attribute.
# - Assign the parameter for sauce to the attribute.
# - Create the toppings attribute, starting off as a list only holding cheese.

class Pizza:
    """Model of a pizza."""
    def __init__(self, size, sauce="red"):
        self.set_size(size)
        self.sauce = sauce
        self.toppings = ["cheese"]
    def set_size(self, size):
        """Sets the size of a pizza."""
        if not size.isdigit() or int(size) < 10:
            self.size = 10
        else:
            self.size = int(size)
    def get_size(self):
        return self.size
    def set_sauce(self, sauce):
        self.sauce = sauce
    def get_sauce(self):
        return self.sauce
    def set_toppings(self, toppings):
        for topping in toppings:
            self.toppings.append(topping)
    def get_toppings(self):
        return self.toppings
    def num_of_toppings(self):
        return len(self.toppings)
    
# You will be creating a Pizzeria class with the following attributes:
# - orders, the number of orders placed. Should start at 0.
# - price_per_topping, a static value for the price per topping of 0.30.
# - price_per_inch, a static value of 0.60 to denote how much the pizza cost per inch of diameter.
# - pizzas, a list of all the pizzas with the last ordered being the last in the list.
# You will need the following methods:
# - __init__()
#   - This one does not need to take in any extra parameters.
#   - It should create and set the attributes defined above.
# - placeOrder():
#   - This method will allow a customer to order a pizza.
#     - Which will increment the number of orders.
#   - It will need to create a pizza object.
#   - You will need to prompt the user for:
#     - the size
#     - the sauce, tell the user if nothing is entered it will default to red sauce (check for an empty string).
#     - all the toppings the user wants, ending prompting on an empty string.
#     - Implementation of this is left to you; you can, for example:
#       - have a while loop and append new entries to a list
#       - have the user separate all toppings by a space and turn that into a list.
#   - Upon completion, create the pizza object and store it in the list.
# - getPrice()
#   - You will need to determine the price of the pizza.
#   - This will be (pizza.getSize() * price_per_inch) + pizza.getAmountOfToppings() * price_per_topping.
#   - You will have to retrieve the pizza from the pizza list.
# - getReceipt()
#   - Creates a receipt of the current pizza.
#   - Show the sauce, size, and toppings.
#   - Show the price for the size.
#   - The price for the toppings.
#   - The total price.
# - getNumberOfOrders()
#   - This will simply return the number of orders.

class Pizzeria:
    """Model of pizzeria business."""
    def __init__(self, orders, price_per_topping, price_per_inch, pizzas):
        self.orders = 0
        self.price_per_topping = 0.30
        self.price_per_inch = 0.60
        self.pizzas = []
    def placeOrder(self):
        self.orders += 1
        pizzas = self.pizzas
        while True:
            sauce = input("What sauce would you like on your pizza?"
            "If no sauce is entered, it will default to red.\n")
            if sauce == "":
                sauce = "red"
            break
        
        while True:
            size = input("What size of pizza would you like?"
            "The minimum size is a 10 inch pizza.\n")
            try:
                int(size) >= 10
            except ValueError:
                continue
            else:
                if int(size) < 10:
                    continue
                else:
                    break
        while True:
            toppings = []
            tops = input("What toppings would you like? Separate toppings with a space. Enter q as the last entry to continue.\n")
            tops = tops.split(" ")
            for top in tops[:-1]:
                toppings.append(top)
            if tops[-1] == "q":
                break
        pizza = Pizza(size,sauce)
        pizza.toppings = toppings
        pizzas.append(pizza)
    def getPrice(self, pizzas):
        pizzas = self.pizzas
        prices = []
        for pizza in pizzas:
            price = (pizza.get_size() * self.price_per_inch) + (pizza.num_of_toppings() * self.price_per_topping)
            prices.append(price)
        total = 0
        for i in range(0,len(prices)):
            total += prices[i]
        return total
    def getReceipt(self, pizzas):
        pizzas = self.pizzas
        pizza = pizzas[-1]
        num_of_toppings = pizza.num_of_toppings()
        toppingsPrice = num_of_toppings * self.price_per_topping
        price = (pizza.get_size() * self.price_per_inch) + (pizza.num_of_toppings() * self.price_per_topping)
        receipt = [pizza.sauce, pizza.size, pizza.toppings, round(toppingsPrice,2), round(price,2)]
        print(f"You ordered a {receipt[1]} inch pizza with {receipt[0]} sauce.")
        print(f"The toppings you selected were {receipt[2]} which added ${receipt[3]} to your total.")
        print(f"The total price for your pizza is ${receipt[4]}.")
    def getNumberOfOrders(self):
        pizzas = self.pizzas
        total = round(self.getPrice(pizzas),2)
        print(f"You ordered {self.orders} pizzas that total to ${total}.")
# - Declare your pizzeria object.
# - Enter a while loop to ask if the user wants to order a pizza.
# - Exit on the word `exit`.
# - Call the placeOrder() method with your class instance.
# - After the order is placed, call the getReceipt() method.
# - Repeat the loop as needed.
# - AFTER the loop, print how many orders were placed.

papaspizzeria = Pizzeria(0,.3,.6,[])
while True:
    order = input(f"Would you like to place an order? exit to exit\n")
    if order.lower() == "exit":
        break
    else:
        pizza = papaspizzeria.placeOrder()
        papaspizzeria.getReceipt(pizza)
print(papaspizzeria.getNumberOfOrders())

    
    

# Example output:
"""
Would you like to place an order? exit to exit
yes
Please enter the size of pizza, as a whole number. The smallest size is 10
20
What kind of sauce would you like?
Leave blank for red sauce
garlic
Please enter the toppings you would like, leave blank when done
pepperoni
bacon

You ordered a 20" pizza with garlic sauce and the following toppings:
                                                                  cheese
                                                                  pepperoni
                                                                  bacon
You ordered a 20" pizza for 12.0
You had 3 topping(s) for $0.8999999999999999
Your total price is $12.9

Would you like to place an order? exit to exit
"""