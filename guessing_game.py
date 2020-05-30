import random


def guessing_game():
    count = 0
    while True:
        count += 1
        if count > 5:
            break
        try:
            n = int(input('Guess a number between 1 and 10: '))
            r = random.randint(1, 10)
            if n > 0 and n < 11:
                if r == n:
                    print(f'Congratulations! You are right. The correct number was {r}')
                    break
                else:
                    print(f"Try again the correct number was {r}. Tries left {5-count}")
            else:
                print('Please enter the number between 1 and 10')
        except ValueError:
            print('Gibberish? Please enter the number between 1 and 10')
            continue
    return 0

guessing_game()

