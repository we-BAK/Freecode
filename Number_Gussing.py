import random

target = random.randint(1, 100)
attempts = 0

print("Guess a number between 1 and 100!")

while True:
    guess = int(input("Your guess: "))
    attempts += 1

    if guess < target:
        print("Too low!")
    elif guess > target:
        print("Too high!")
    else:
        print(f"You got it in {attempts} tries!")
        break