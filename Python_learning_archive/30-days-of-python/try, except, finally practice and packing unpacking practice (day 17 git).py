# try:
#     name = input('Enter your name:')
#     year_born = input('Year you were born:')
#     age = 2026 - int (year_born)
#     print(f'You are {name}. And your age is {age}.')
# except TypeError as e:
#     print (e)
#     print('Type error occured')
# except ValueError as e:
#     print('Value error occured')
#     print (e)
# except ZeroDivisionError as e:
#     print('zero division error occured')
#     print (e)
# finally:
#     print ("this always prints")


# def packing_person_info(**kwargs):
#     for key in kwargs:
#         print(f"{key} = {kwargs[key]}")
#     return kwargs

# print(packing_person_info(name="Asabeneh",
#       country="Finland", city="Helsinki", age=250))


names = ['Finland', 'Sweden', 'Norway',
         'Denmark', 'Iceland', 'Estonia', 'Russia']
*nordic_countries, es, ru = names
print(f"nordic countries: {nordic_countries}")
print(es.title())
print(ru.title())


# countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
# fin, sw, nor, *rest = countries
# print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']
# numbers = [1, 2, 3, 4, 5, 6, 7]
# one, *middle, last = numbers
# print(one, middle, last)      #  1 [2, 3, 4, 5, 6] 7
