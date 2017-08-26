import socket

def main():
    conHost = '127.0.0.1'
    conPort = 5001

    s = socket.socket()
    s.connect((conHost, conPort))

    while True:


if __name__ == '__main__':
    main()

