import random

class NumberGuessingGame:
    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.target = random.randint(lower_bound, upper_bound)
        self.attempts = 0

    def make_guess(self, guess):
        self.attempts += 1
        if guess < self.target:
            return "Too low!"
        elif guess > self.target:
            return "Too high!"
        else:
            return f"Correct! It took you {self.attempts} attempts."

    def play(self):
        print(f"Guess the number between {self.lower_bound} and {self.upper_bound}")
        while True:
            try:
                guess = int(input("Enter your guess: "))
                result = self.make_guess(guess)
                print(result)
                if "Correct" in result:
                    break
            except ValueError:
                print("Please enter a valid number.")

def main():
    game = NumberGuessingGame(1, 100)
    game.play()

if __name__ == "__main__":
    main()
