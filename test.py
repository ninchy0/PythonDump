# Simple Dice Rolling Simulator

import random
import time


def dice_roll(num):
    if num == 1:
        print("[-----]")
        print("[	 ]")
        print("[ 0 ]")
        print("[	 ]")
        print("[-----]")

    if num == 2:
        print("[-----]")
        print("[ 0 ]")
        print("[	 ]")
        print("[ 0 ]")
        print("[-----]")

    if num == 3:
        print("[-----]")
        print("[	 ]")
        print("[0 0 0]")
        print("[	 ]")
        print("[-----]")

    if num == 4:
        print("[-----]")
        print("[0 0]")
        print("[	 ]")
        print("[0 0]")
        print("[-----]")

    if num == 5:
        print("[-----]")
        print("[0 0]")
        print("[ 0 ]")
        print("[0 0]")
        print("[-----]")

    if num == 6:
        print("[-----]")
        print("[0 0 0]")
        print("[	 ]")
        print("[0 0 0]")
        print("[-----]")


if __name__ == '__main__':

    true = ['yes', 'YES', 'y', 'Y']

    # Generates a random number
    # between 1 and 6 (including
    # both 1 and 6)
    random_number = random.randint(1, 6)

    print('\n[*] Dice is rolling...')

    time.sleep(3)
    dice_roll(random_number)

    while True:

        play_again = input(
            "\n[+] Do you want to roll the dice again? (yes/no)\n>>> ")

        if play_again in true:

            random_number = random.randint(1, 6)
            print('\n[*] Dice is rolling...')

            time.sleep(3)
            dice_roll(random_number)

        else:
            time.sleep(3)
            print('\n[+] See you again, bye :)')
            break
