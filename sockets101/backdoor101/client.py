 #!/usr/bin/env python3

import socket
import sys

target = '127.0.0.1'
port = 666

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((target, port))
    print("Connection established")
    try:
        while True:
            message = input()
            s.send(message.encode())
    except KeyboardInterrupt:
        print('\n\nSession ends here.')
        sys.exit()
