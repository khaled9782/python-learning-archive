import random
import string

# def random_user_id ():
#     characters = string.ascii_letters + string.digits
#     user_id = "".join(random.choices(characters,k=6))
#     return user_id

# print (random_user_id())

""" def user_id_gen_by_user ():

    num_char = int(input ("how long do you want the user ID to be ?: " ))
    num_of_id = int(input ("How many ID's do you want ?: "))

    characters = string.ascii_letters + string.digits
    print ("- OUTPUT:")
    for i in range((num_of_id)):
        user_id = "".join(random.choices(characters,k=num_char))
        print (user_id)

user_id_gen_by_user() """

# def rgb_color_gen ():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     print (f"rgb({r},{g},{b})")

# rgb_color_gen()


def list_of_hexa_colors(num):
    colors = []
    for i in range(num):
        hex = random.choices(string.hexdigits, k=6)
        hex_color = "#" + "".join(hex).lower()
        colors.append(hex_color)
    return (colors)


def list_of_rgb_colors(num):
    rgb_color = []
    for i in range(num):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        rgb_value = f"rgb({r},{g},{b})"
        rgb_color.append(rgb_value)
    return rgb_color


# print(list_of_rgb_colors(6))


def generate_colors(type, num):
    if type == "rgb":
        return (list_of_rgb_colors(num))
    elif type == "hexa":
        return (list_of_hexa_colors(num))
    else:
        return "pleae input a supported colour type"


# print(generate_colors("rgb", 3))

# def shuffle_list (list):


color = ["red", "yellow", "green", "blue"]
print(random.choices(color, k=3))
