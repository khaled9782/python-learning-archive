# level 2 ex 1
# def evens_and_odds(n):
#     even = 0
#     odd = 0
#     for i in range(1, n+1):
#         if i % 2 == 0:
#             even += 1
#         else:
#             odd += 1
#     print(f"there are {even} numbers and {odd} numbers")


# evens_and_odds(100)

# Ex 2
# def factorial(n):
#     i = n-1
#     while i != 0:
#         n *= i
#         i -= 1
#     print(n)
# factorial(5)

# def show_args(**kwargs):
#     for k, v in kwargs.items():
#         print(f"{k}:{v}", end=", ")

# show_args(name="Alice", age=30, city="New York")

# level 3 Ex 1
# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True


# print(is_prime(10))

# Ex 2
def unique(items):
    seen = []
    for item in items:
        if item in seen:
            return False
        seen.append(item)
    return True


num = [1, 2, 2, 3, 4, 5]
print(unique(num))
