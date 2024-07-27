import random

def hangman():
    words = ['python', 'hangman', 'programming', 'challenge']
    word = random.choice(words)
    guessed = set()
    attempts = 6
    display = ['_'] * len(word)

    print("Welcome to Hangman!")

    while attempts > 0 and '_' in display:
        print(' '.join(display))
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        if guess in guessed:
            print("You already guessed that letter.")
            continue
        guessed.add(guess)
        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    display[i] = guess
        else:
            attempts -= 1
            print(f"Wrong guess. {attempts} attempts left.")

    if '_' not in display:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Game over. The word was: {word}")

hangman()
