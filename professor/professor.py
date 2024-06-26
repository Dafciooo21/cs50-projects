import random


def main():
    eqn = 10
    score = 0
    chances = 3
    level = get_level()
    while eqn != 0:
        if chances == 3:
            x, y = generate_integer(level)
        try:
            user_answer = int(input(f"{x} + {y} = "))
            answer = x + y
            if user_answer == answer:
                eqn = eqn - 1
                score = score + 1
                chances = 3
                continue
            else:
                raise ValueError
        except (ValueError, NameError):
            print("EEE")
            chances = chances - 1
            pass
        if chances == 0:
            print((f"{x} + {y} = {answer}"))
            chances = 3
            eqn = eqn - 1
            continue
    print(f"Score: {score}")

#prompts the user for a level
#if the user does not input 1, 2, or 3, the program should prompt again
def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if 1 <= n <= 3:
                return n
        except:
            pass

#randomly generates ten (10) math problems formatted as X + Y =
#each of X and Y is a non-negative integer with digits
def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y

if __name__ == "__main__":
    main()
