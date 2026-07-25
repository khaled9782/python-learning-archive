"""NUMBER GAME"""
from random import randint as rndint

print("we are going to play a number game")
print("you will get 6 tries to guess a number between 1 and 20")
secret_number = rndint(1, 20)

for guesses_taken in range(1, 7):
    guess = int(input("Take a guess: "))

    if guess > secret_number:
        print(f"{guess} is too high, try lower")
    elif guess < secret_number:
        print(f"{guess} is too low, try higher")
    else:
        break

if guess == secret_number:
    print(
        f"congrats ! {secret_number} is the correct guesss and you got it in {guesses_taken} guesses")
else:
    print(f"Nope, the secret number was {secret_number}")
