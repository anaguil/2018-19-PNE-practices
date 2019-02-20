import socket
from seq import Seq

PORT = 8081
IP = "212.128.253.86"
MAX_OPEN_REQUEST = 5
l_response = list()

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((IP, PORT))
serversocket.listen(MAX_OPEN_REQUEST)
print("Socket ready: {}", format(serversocket))

def process_client(cs):
    """Function to read the info of the client and process it"""
    msg = cs.recv(2048).decode("utf-8")
    msg = msg.split("\n")
    if msg[0] == "":
        cs.send(str.encode("Alive"))
        cs.close()
    else:
        counter = 0
        for base in msg[0]:
            if base != "A" and base != "C" and base != "G" and base != "T":
                counter += 1
        if counter > 0:
            cs.send(str.encode("ERROR"))
            cs.close()
        else:
            l_response.append("OK")
            sequence = Seq(msg[0])
            for elem in msg[1:]:
                if msg == "len":
                    l_response.append("\n")
                    l_response.append(str(sequence.len()))
                elif msg == "complement":
                    l_response.append("\n")
                    l_response.append(sequence.complement())

        message = ""
        for element in l_response:
            message = message + element + "\n"
        cs.send(str.encode(message))
        cs.close()


while True:
    print("Waiting for connections at: {}, {}".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    print("Attending client: {}".format(address))

    process_client(clientsocket)
