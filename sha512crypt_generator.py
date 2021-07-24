#!/usr/bin/python3

import random 
import string
import crypt
import time

def password_generator(length):

    password = ''
    characters = string.ascii_letters
    digits = string.digits
    special = '!@#$%'
    container = characters + digits + special

    
    for i in range(length):
        password = password + random.choice(container)
    
    return password


def hash_generator(password):

    hashed = crypt.crypt(password)
    return hashed


def main():

    print('\nDUMB HASH GENERATOR CREATED BY @ninchy0.\n')
    print('Enter 0 for custom password.')
    print('\nEnter 1 for random password.\n')
    choice = int(input('>>> '))

    if choice == 0:
        password = input('\nEnter password: ')
        confirm_password = input('Confirm password: ')

        if confirm_password == password:
            hashed_password = hash_generator(password)

            print(f'\n\nYour password = {password}')
            print(f'Your hash = {hashed_password}\n')
        
        else:
            print('\nPasswords didn\'t match. Please re-run the program again.\n')

    elif choice == 1:
        
        print('\nPassword length more 16 is GOOD FOR HEALTH.\n')

        password_length = int(input('Enter the length of password: '))
        password = password_generator(password_length)
        hashed_password = hash_generator(password)
    
        print(f'\n\nYour password = {password}')
        print(f'Your hash = {hashed_password}')
    
    else:
        print('\nLMAO.....')
        time.sleep(5)
        print('\n\n\tBYE.')



if __name__ == "__main__":
    main()          # calling the main function, as simple as that :)
