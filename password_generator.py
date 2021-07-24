#!/usr/bin/python3

import random 
import string

def generator(length):

    password = ''
    characters = string.ascii_letters
    digits = string.digits
    special = '!@#$%'
    container = characters + digits + special

    
    for i in range(length):
        password = password + random.choice(container)
    
    print(f'Generated password = {password}')



if __name__ == "__main__":

    print('Password Generator created by @ninchy0.')
    print('Password length more 16 is GOOD FOR HEALTH.\n\n')
    

    password_length = int(input('Enter the length of password: '))
    generator(password_length)
