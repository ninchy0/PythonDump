 #!/usr/bin/env python3
import socket
import sys
ip_addr = '127.0.0.1'
port = 1234

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((ip_addr, port))
    print("Connection established")
    try:
        while True:
            message = input('Enter your message: ')
            s.sendall(message.encode())
    except KeyboardInterrupt:
        print('\n\nSession ends here.')
        sys.exit()
