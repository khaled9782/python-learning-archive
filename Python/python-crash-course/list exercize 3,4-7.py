# inviting guests for dinner
guest_list = ["bilal", "nabeel", "hasann"]
print(f"would you like to join me for dinner {guest_list[0].title()} ?")
print(f"would you like to join me for dinner {guest_list[1].title()} ?")
print(f"would you like to join me for dinner {guest_list[2].title()} ?")
# hasann wont be able to join
print(f"{guest_list[2].title()} wont be abe to attend \n sooo....")
guest_list[2] = "shayan"
print(f"would you like to join me for dinner {guest_list[2].title()} ?")
# found a bigger table so we can invite moer people over
print("chat, i found another place where the food is better and cheaper so we'll be inviting more people")
guest_list.insert(0, "abdul")
guest_list.insert(2, "mehul")
guest_list.insert(4, "radi")
print(f"would you like to join me for dinner {guest_list[0].title()} ?")
print(f"would you like to join me for dinner {guest_list[1].title()} ?")
print(f"would you like to join me for dinner {guest_list[2].title()} ?")
print(f"would you like to join me for dinner {guest_list[3].title()} ?")
print(f"would you like to join me for dinner {guest_list[4].title()} ?")
print(f"would you like to join me for dinner {guest_list[5].title()} ?")
# food wont arrive on time, onl 2 ppl alloed then
print("food wont arrive on time, onl 2 ppl allowed")
name = guest_list.pop()
print(f"sorry {name.title()}, there is no room")
name = guest_list.pop()
print(f"sorry {name.title()}, there is no room")
name = guest_list.pop()
print(f"sorry {name.title()}, there is no room")
name = guest_list.pop()
print(f"sorry {name.title()}, there is no room")

name = guest_list[0]
print(f"{name.title()}, pls come for dinner")
name = guest_list[1]
print(f"{name.title()}, pls come for dinner")
del guest_list[0]
del guest_list[0]
print(guest_list)
