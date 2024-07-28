import random

def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def play_turn(player):
    print(f"{player}'s turn")
    input("Press Enter to roll the dice...")
    roll = roll_dice()
    print(f"{player} rolled a {roll}")
    return roll

def check_winner(score1, score2):
    if score1 >= 20:
        return "Player 1 wins!"
    elif score2 >= 20:
        return "Player 2 wins!"
    return None

def main():
    score1, score2 = 0, 0
    while True:
        score1 += play_turn("Player 1")
        if (result := check_winner(score1, score2)) is not None:
            print(result)
            break
        score2 += play_turn("Player 2")
        if (result := check_winner(score1, score2)) is not None:
            print(result)
            break

if __name__ == "__main__":
    main()
