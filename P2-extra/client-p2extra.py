# Creating a client that sends a sequence to the server and retrieves the complement donde by the server

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Configuration of the server and connecting to it
PORT = 8080
IP = "212.128.253.64" #this is the IP of the computer that is working as a client
s.connect((IP, PORT))

sequence = input("Enter the sequence : ")

# Send the sequence to the server
s.send(str.encode(sequence))

# Recieve the complement of the sequence from the server
msg = s.recv(2048).decode("utf-8")
msg2 = s.recv(2048).decode("utf-8")
print(msg , msg2)
s.close()
