# Programming a client

import socket

while True:
    # Create a socket to connect with internet (AF_INET) and with the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    PORT = 8080
    IP = "212.128.253.80"

    # Connect to the server
    s.connect((IP, PORT))
    
    # Sending info to the server but in bytes. Must transform the string into bytes
    msg = input("Enter a message:")
    s.send(str.encode(msg))
    s.close()
