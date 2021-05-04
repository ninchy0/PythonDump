

# This is a simple text-based adventure game.
import time


def ques_ans():

    global correct
    true = ['yes', 'y', 'Y', 'YES']
    false = ['no', 'n', 'N', 'NO']
    correct = 0  # Storing the correct answers

    print("\nButwal is the captial city of Nepal.")
    choice = input(">>> ")
    if choice in true:
        correct += 0  # If correct, the user gets one point
    else:
        correct += 1

    print("\nNepal is an island.")
    choice = input(">>> ")
    if choice in false:
        correct += 1
    else:
        correct += 0

    print("\nNepal is a Beautiful Country.")
    choice = input(">>> ")
    if choice in true:
        correct += 1
    else:
        correct += 0

    print("\nNepali is the primary language of Nepal.")
    choice = input(">>> ")
    if choice in false:
        correct += 0
    else:
        correct += 1

    print("\nPeople of Nepal are Nepalian.")
    choice = input(">>> ")
    if choice in true:
        correct += 0
    else:
        correct += 1


def game():
    name = input("What's your name?\n>>> ")  # Storing the user's name
    print("\nOK, " + name +
          ", let's get started. Remember, the following answers are only yes or no.")

    time.sleep(2)
    ques_ans()

    print("\nYou're finished, " + name +
          ". You got", correct, "out of 5 correct.")


if __name__ == '__main__':
    game()
    time.sleep(3)

    while True:

        yes = ['yes', 'y', 'Y', 'YES']
        no = ['no', 'n', 'N', 'NO']

        answer = input('\nDo you want to play the game again? (yes/no)\n>>> ')
        if answer in yes:
            game()

        else:
            print('Thanks for playing the game.')
            time.sleep(3)
            break
