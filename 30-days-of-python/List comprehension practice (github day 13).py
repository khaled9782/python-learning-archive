# numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
# even_pos = [i for i in range(21) if i%2 == 0 and i>0]
# print (even_pos)

# list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# flattened_list = [ number for row in list_of_lists for number in row]
# print(flattened_list)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# print ((lambda a, b: a + b)(3,3))

# numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
# neg_zero = [i for i in numbers if i<=0]
# print(neg_zero)

# list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# flatten = [n for row in list_of_lists for n in row]
# print (flatten)


# lst = [(n,1,n,n**2,n**3,n**4,n**5) for n in range(10)]
# for item in lst:
#     print (item)

# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

# formatted = lambda country, city: [country.upper(), country[:3].upper(), city.upper()]

# result = [formatted(country,city) for sublist in countries for country, city in sublist]
# print (result)


# names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

# result = [f"{first} {last}" for sublist in names for first, last in sublist]
# print (result)

# countries = [[('Finland', 'Helsinki')], [
#     ('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# form = [(lambda country, city: {"country": country.upper(), "city": city.upper()})(
#     country, city) for sublist in countries for country, city in sublist]
# print(form)
