import socket

# SERVER IP, PORT
IP = "212.128.253.86"
PORT = 8081


msg = "AG\nlen"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))
s.send(str.encode(msg))

# Receive the servers response
response = s.recv(2048).decode()

# Print the server's response
print("Response: {}".format(response))


s.close()
