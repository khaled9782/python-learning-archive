# number check:
# number = 21
# if number < 10:
#     print("true")
# else:
#     print("false")

# vegetable check:
# vegetable = "tomato"
# print("is the item a tomato ?")
# if vegetable == "tomato":
#     print("yes")
# else:
#     print("no")
# print("\nis the item a raddish ?")
# if vegetable == "raddish":
#     print("true")
# else:
#     print("no")

# two number check:
# x = 10
# y = 25
# print(f"X={x} Y={y}\n")
# print("are both numbers greater than 5 ?")
# if x and y > 5:
#     print("true\n")
# else:
#     print("false\n")

# print("is the number X not 2 ?")
# if x != 2:
#     print("yes\n")
# else:
#     print("no\n")

# print("is at least one of them less than 20 ? ")
# if x or y < 20:
#     print("yes\n")
# else:
#     print("no\n")

# conditional tests with lists:
vegetables = ["tomato", "raddish", "onion"]
vegetable = "Potato"
print(vegetables)
print(f"this is the selected vegetable: {vegetable}\n")
print(f"is the vegetable {vegetable} present in the list ?")
if vegetable in vegetables:
    print("yes, its present\n")
else:
    print("nope, its not there\n")

vegetable = "Tomato"
print(f"is the vegetable {vegetable} present in the list ?")
if vegetable.lower() in vegetables:
    print("yes, its present")
else:
    print("nope, its not there")
