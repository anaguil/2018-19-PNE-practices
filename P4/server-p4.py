import socket

IP = "212.128.253.104"
PORT = 8080
MAX_OPEN_REQUESTS = 5


def process_client(cs):
    """Process the client request.
    Parameters:  cs: socket for communicating with the client"""

    # Read client message. Decode it as a string
    msg = cs.recv(2048).decode("utf-8")

    if msg == "":
        index = open("index.html")
        content = index.read()
        index.close()
    elif msg == "blue.html":
        blue = open("blue.html")
        content = blue.read()
        blue.close()
    elif msg == "pink.html":
        pink = open("pink.html")
        content = pink.read()
        pink.close()
    else:
        error = open("error.html")
        content = error.read()
        error.close()

    status_line = "HTTP/1.1 200 OK\r\n"
    header = "Content-Type: text/html\r\n"
    header += "Content-Length: {}\r\n".format(len(str.encode(content)))

    # Send the response
    response_msg = status_line + header + "\r\n" + content
    cs.send(str.encode(response_msg))

    # Close the socket
    cs.close()


# MAIN PROGRAM

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP and PORT
serversocket.bind((IP, PORT))

# Configure the server sockets
# MAX_OPEN_REQUESTS connect requests before refusing outside connections
serversocket.listen(MAX_OPEN_REQUESTS)

print("Socket ready: {}".format(serversocket))

while True:
    # accept connections from outside
    # The server is waiting for connections
    print("Waiting for connections at {}, {} ".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Connection received. A new socket is returned for communicating with the client
    print("Attending connections from client: {}".format(address))

    # Service the client
    process_client(clientsocket)
