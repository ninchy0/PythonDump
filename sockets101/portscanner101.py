#!/usr/bin/python3

import socket

target = input('Enter ip address: ')
port_range = input('Enter the port range to scan (e.g 0-100): ')

low_port = int(port_range.split('-')[0])
high_port = int(port_range.split('-')[1])

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    for port in range(low_port, high_port):
        status = s.connect_ex((target, port))

        if status == 0:
            print(f'PORT {port} - OPEN.')

        else:
            print(f'PORT {port} - CLOSED.')
