squares_1 = []
for value in range(1, 11):
    value = value**2
    squares_1.append(value)
print(f" using method 1: {squares_1}")

squares_2 = []
for value in range(1, 11):
    squares_2.append(value**2)
print(f" using method 2: {squares_2}")

squares_3 = [value**2 for value in range(1, 11)]
print(f" using method 3: {squares_3}")

cubes = [x**3 for x in range(1, 11)]
print(cubes)
