

# Simple Number Guessing Program
import random
import time


def numberguess():

    # Generating random numbers from 0 to 10.
    random_number = random.randrange(10+1)
    guess_count = 0

    while guess_count < 3:
        print(f'Number of guesses left: {3 - guess_count}')
        guess = int(input('Guess the number (0-10)\n>>> '))

        if guess <= 10:

            if guess == random_number:
                print('Yay! Hoorah, you guessed the correct number.')
                print(f'{random_number} was indeed the correct number.\n')
                break

            else:
                print('Opps! Try again harder :V\n')
                guess_count += 1
                continue
        else:
            print('Please enter (0-10) only.\n')


if __name__ == '__main__':

    while True:
        answer = input('Enter y/n to play or to exit.\n>>> ')

        if answer in ['y', 'Y']:
            time.sleep(3)
            numberguess()

        else:
            time.sleep(3)
            break
