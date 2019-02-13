# Server that recieves a sequence from a client. The server calculates its complement and sends it back to the client

from seq import Seq
import socket

# Configure the Server's IP and PORT
PORT = 8080
IP = "212.128.253.64" #this IP is the IP of the computer that is doing the server function (can be the same as client)
MAX_OPEN_REQUESTS = 5

# Counting the number of connections
number_con = 0

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    serversocket.bind((IP, PORT))
    # become a server socket
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        # accept connections from outside
        print("Waiting for connections at {}, {} ".format(IP, PORT))
        (clientsocket, address) = serversocket.accept()

        # Another connection!
        number_con += 1

        # Print the conection number
        print("CONNECTION: {}. From the IP: {}".format(number_con, address))

        # Read the message from the client, if any
        msg = clientsocket.recv(2048).decode("utf-8")
        print("The input sequence is : {}".format(msg))
        
        # Transform it into class Seq and calculate its complement
        msg = Seq(msg)
        message = msg.complement()
        message = message.strbases
        
        # Send the message
        send_bytes = str.encode(message)
        
        # We must write bytes, not a string
        clientsocket.send(str.encode("The complement sequence is : "))
        clientsocket.send(send_bytes)
        clientsocket.close()

except socket.error:
    print("Problems using port {}. Do you have permission?".format(PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()
