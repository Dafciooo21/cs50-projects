import random

# main program - asking for a level, then generating random number within that level and making the user guess the number until he/she gets it
def main():
    level = get_level()
    number = generate_random_number(level)
    guessing_game(number)

# guessing part - if wrong number or not intiger -> ask again
def guessing_game(number):
    while True:
        try:
            guess = int(input("Guess: "))

            if guess == number:
                print("Just right!")
                break
            elif guess > number:
                print("Too large!")
            else:
                print("Too small!")
        except ValueError:
            print("Invalid input. Please enter a number.")

# level part - if number <= 1 or negative or not intiger -> ask again
def get_level():
    while True:
        try:
            level = int(input("Level: "))

            if level >= 1:
                return level
        except ValueError:
            print("Invalid input. Please enter a number.")

# generator from the range (1, level), where level is number inputed by the user before
def generate_random_number(level):
    number = random.randint(1, level)
    return number

if __name__ == "__main__":
    main()
