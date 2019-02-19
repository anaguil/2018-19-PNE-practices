import socket
import termcolor

PORT = 8080
IP = "212.128.253.77"
MAX_OPEN_REQUEST = 5
loop = True

def process_client(cs):
    """Function to read the info of the client and process it"""

    # Reading the message from the client. We decode to transform from bytes to string
    msg = cs.recv(2048).decode("utf-8")

    if msg == "EXIT":
        loop = False
        cs.close()

    else:
        print("Message from the client: ")
        termcolor.cprint(msg, 'yellow')

        # Sending the message back to the client. We encode from string to bytes
        cs.send(str.encode(msg))
        cs.close()


# Create a socket to connect to the clients (internet, type of socket created (type string))
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding our socket to this parameter (tuple)
serversocket.bind((IP, PORT))

# Change the type of socket to listen to requests from clients
serversocket.listen(MAX_OPEN_REQUEST)

print("Socket ready: {}", format(serversocket))

while loop == True:
    print("Waiting for connections at: {}, {}".format(IP, PORT))

    # Method that will block the server and wait until the client is connected,
    # it returns a client socket and the IP address of the client
    (clientsocket, address) = serversocket.accept()

    # -- Process the client request
    print("Attending client: {}".format(address))

    process_client(clientsocket)
