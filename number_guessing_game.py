import random

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")

number = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    attempts += 1
    
    if guess < 1 or guess > 100:
        print("Please guess a number between 1 and 100.")
        continue
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Correct! You guessed it in {attempts} attempts.")
        break
