import socket
import sys


def usage():
    print('''Example:
    1. python3 get_ip_by_domain.py -d <url> 
            ''')


def get_ip(url):
    url_ip = socket.gethostbyname(url)
    print(f'URL = {url}\nIPv4 = {url_ip}')


def main():

    try:
        if sys.argv[1] == '-h':
            usage()

        elif sys.argv[1] == '-d':
            get_ip(str(sys.argv[2]))

        else:
            usage()

    except IndexError:
        usage()


if __name__ == '__main__':
    main()
