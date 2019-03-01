import socket

IP = "212.128.253.94"
PORT = 8080
MAX_OPEN_REQUESTS = 5


def process_client(cs):
    """Process the client request.
    Parameters:  cs: socket for communicating with the client"""

    # Read client message. Decode it as a string
    msg = cs.recv(2048).decode("utf-8")
    print(msg)
    # Take only the header from the entire request
    msg = msg.split("\n")[0]
    # Take the second element that contains the name of the page that the client is requesting
    try:
        msg = msg.split()[1]
    except IndexError:
        return
    print(msg)
    if msg.endswith("/") or msg.endswith("/index.html"):
        f = open("index.html")
        content = f.read()
    elif msg.endswith("/blue.html"):
        f = open("blue.html")
        content = f.read()
    elif msg.endswith("/pink.html"):
        f = open("pink.html")
        content = f.read()
    else:
        f = open("error.html")
        content = f.read()

    f.close()
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
