# Programming a client

import socket


while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    PORT = 8080
    IP = "212.128.253.79"
    # Connect to the server
    s.connect((IP, PORT))
    msg = input("Enter a message:")
    s.send(str.encode(msg))
    s.close()
