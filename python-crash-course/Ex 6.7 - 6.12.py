# Ex 6.7:
# people = {
#     "bilal": {
#         "first_name": "bilal",
#         "second_name": "ahmed",
#         "Age": 18,
#         "birthplace": "kuwait"},

#     "nabeel": {
#         "first_name": "nabeel",
#         "second_name": "waleed",
#         "Age": 19,
#         "birthplace": "pakistan"},

#     "shayan": {
#         "first_name": "shayan",
#         "second_name": "raghib",
#         "Age": 21,
#         "birthplace": "kuwait"}

# }

# for person, info in people.items():
#     print(f"\n Heres all the info for {person.title()}: ")
#     print(
#         f"Full Name: {info["first_name"].title()} {info["second_name"].title()}\t Place of Birth: {info["birthplace"].title()} ")

# Ex 6.8:

# pets = []
# pet = {"name": "max",
#        "species": "dog",
#        "owner": "mariam"}
# pets.append(pet)

# pet = {"name": "mittens",
#        "species": "chinchilla",
#        "owner": "khaled"}
# pets.append(pet)

# pet = {"name": "ernstein",
#        "species": "parrot",
#        "ownner": "fahim"}

# pets.append(pet)

# for pet in pets:
#     print(f"\nHeres all I know about {pet["name"].title()}:")
#     for key, value in pet.items():
#         print(f"\t {key}:{value}")

# Ex 6.9:

# favorite_places = {
#     "khaled": ["river cities in venice", "notre dame", "taj mahal"],
#     "mariam": ["shibuya dustrict", "angel falls", "leaning tower of pisa"],
#     "nabeel": ["burj khalifa", "global village", "Miracle garden"],
# }
# for name, places in favorite_places.items():
#     print(f"\n {name.title()} likes the following places:")
#     for place in places:
#         print(f"\t- {place.title()}")
