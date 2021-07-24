#!/usr/bin/python3

import random 
import string

def generator(length):  
    special = ''
    password = ''

    characters = string.ascii_letters
    digits = string.digits
    s_characters = ['!', '@', '#', '$', '%']
    for i in s_characters:
        special = special + i

    container = characters + digits + special

    for i in range(length):
        password = password + random.choice(container)
    print(f'Generated password = {password}')




if __name__ == "__main__":
    print('''Password Generator created by @ninchy0.
Passowrd length more than 16 is good for health

    ''')
    password_length = int(input('Enter the length of password: '))
    generator(password_length)
