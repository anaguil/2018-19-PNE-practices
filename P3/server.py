import socket
from seq import Seq

PORT = 8080
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
            msg = msg.remove(msg[0])
            for elem in msg:
                if elem == "len":
                    l_response.append(str(sequence.len()))
                elif elem == "complement":
                    complement = sequence.complement()
                    complement = complement.strbases
                    l_response.append(complement)
                elif elem == "reverse":
                    reverse = sequence.reverse()
                    reverse = reverse.strbases
                    l_response.append(reverse)
                elif elem == "countA":
                    l_response.append(str(sequence.count("A")))
                elif elem == "countC":
                    l_response.append(str(sequence.count("C")))
                elif elem == "countG":
                    l_response.append(str(sequence.count("G")))
                elif elem == "countT":
                    l_response.append(str(sequence.count("T")))
                elif elem == "percA":
                    l_response.append(str(sequence.perc("A")))
                elif elem == "percC":
                    l_response.append(str(sequence.perc("C")))
                elif elem == "percG":
                    l_response.append(str(sequence.perc("G")))
                elif elem == "percT":
                    l_response.append(str(sequence.perc("T")))
                else:
                    cs.send(str.encode("ERROR"))
                    cs.close()

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
