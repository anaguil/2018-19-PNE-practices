import socket

# SERVER IP, PORT
IP = "212.128.253.77"
PORT = 8080


while True:
    # Only connect to the server when you have data to send.
    msg = input("Enter a message: ")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    # Send the request message to the server
    s.send(str.encode(msg))

    # Receive the servers response
    response = s.recv(2048).decode()

    # Print the server's response
    print("Response: {}".format(response))

    s.close()
