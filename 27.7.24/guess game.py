import random

def game():
    number = random.randint(1, 100)
    attempts = 0
    guess = None

    print("Guess the number between 1 and 100")

    while guess != number:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
        except ValueError:
            print("Please enter a valid number.")

    print(f"Congratulations! You guessed the number {number} in {attempts} attempts.")

game()
