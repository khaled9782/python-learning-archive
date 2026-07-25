# Ex 4-10:
# players = ["arnold", "rahul", "oliver", "reemus",
#            "ramesh", "swethan", "betty", "sujesh"]
# print(f"the first three items in the list are {players[:3]}")
# print(f"\n three items from the middle of the list are {players[2:5]}")
# print(f"\nthe last three items from the list are {players[-3:]}")

# Ex 4-11:
# pizzas = ["pepperonni", "spicy chicken ranch", "mixed beef"]
# friend_pizza = pizzas[:]
# pizzas.append("ultimate cheese")
# friend_pizza.append("huwaiian")


# print(f"My favourite pizzas are:")
# for pizza in pizzas:
#     print(f"-{pizza.capitalize()} Pizza")
# print(f"\n My friend's favourite pizzas are:")
# for pizza in friend_pizza:
#     print(f"-{pizza.capitalize()} Pizza")

# Ex 4-13:
buffet_menu = ("sushi", "chicken wings", "french fries", "hummus", "soup")
print("todays items in the menu are:")
for item in buffet_menu:
    print(f"-{item.title()}")

buffet_menu = ("sushi", "chicken wings", "french fries",
               "chese cake", "milkshake")
print("\nour menu had an update, these are items in the revised menu :")
for item in buffet_menu:
    print(f"-{item.title()}")
