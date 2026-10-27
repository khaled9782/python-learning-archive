# Ex 5-3:
# V1 (false):
# alien_color = "red"
# if alien_color == "green":
#     print("you have earned 5 points")

# V2 (true):
# alien_color = "green"
# if alien_color == "green":
#     print("you shot a green alien, you have earned 5 points")

# # Ex 5-4 (false):
# alien_color = "yellow"
# if alien_color == "green":
#     print("you shot a green alien, you have earned 5 points")
# else:
#     print("you havent shot a green alien so you have earned 10 points")

# # Ex 5-4 (true):
# alien_color = "green"
# if alien_color == "green":
#     print("you shot a green alien, you have earned 5 points")

# Ex 5-5:
# alien_color = "green"
# if alien_color == "green":
#     points = 5
# elif alien_color == "yellow":
#     points = 10
# elif alien_color == "red":
#     points = 15
# print(f"you have shot a {alien_color} alien, you earned {points} points")

# Ex 5-6:
age = 70
if age < 2:
    stage_of_life = "baby"
elif age < 4:
    stage_of_life = "toddler"
elif age < 13:
    stage_of_life = "kid"
elif age < 20:
    stage_of_life = "teenager"
elif age < 65:
    stage_of_life = "adult"
elif age >= 65:
    stage_of_life = "elder"
print(
    f"the person's stage of life is {stage_of_life} as they are {age} yrs old")
