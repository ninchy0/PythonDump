#!/usr/bin/python3

import socket
import os

HOST = '127.0.0.1'
PORT = 666        

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    s.bind((HOST, PORT))
    s.listen()
    
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            command = os.system(input('Enter command: '))
            data = conn.recv(1024)
            print(data.decode())
