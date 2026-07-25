# Ex 7.8 and 7.9:

sandwich_orders = ["pastrami", "BLT", "grilled cheese", "turkey",
                   "swiss", "pastrami", "tuna salad", "club", "cheese", "egg salad", "pastrami"]
finished_sandwiches = []
processed_sandwish = ""

"""removes all pastra orders """
print("sorry but we are out of patrami\n")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

""" making sandwiches and adding them to the finished list"""
while sandwich_orders:
    processed_sandwish = sandwich_orders.pop()
    print(f"your {processed_sandwish.title()} Sangweesh has been prepared")
    finished_sandwiches.append(processed_sandwish)

""" list all the prepared sandwiches"""
print("\nthese are all the sandwiches that has been made:")
for sandwich in finished_sandwiches:
    print(f"{sandwich}")
