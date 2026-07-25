# Ex 5-8 and 5-9:
# usernames = ["admin", "khaled", "mariam", "halima", "fahim"]
# if usernames:
#     for user in usernames:
#         if user == "admin":
#             print("welcome back admin, should I load system diagnostics ?")
#     else:
#         print(f"hello {user}")
# else:
#     print("no username entered, please enter your username to login")

# Ex 5-10:
# current_usernames = ["khaled", "mariam", "halima", "fahim", "ibrahim"]
# new_usernames = ["kHaled", "mariam", "nabeel", "bilal", "shayan"]

# current_usernames_lower = [user.lower() for user in current_usernames]
# for new_user in new_usernames:
#     if new_user.lower() in current_usernames_lower:
#         print(
#             f"the username '{new_user}' is not valid, please choose a different one")
#     else:
#         print(f"valid username, hello {new_user}")

# Ex 5-11 printing ordinal numbers:

numbers = list(range(1, 10))
for number in numbers:
    if number == 1:
        ending = "st"
    elif number == 2:
        ending = "nd"
    elif number == 3:
        ending = "rd"
    else:
        ending = "th"
    print(f"{number}{ending}")
