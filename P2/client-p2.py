# Creating a client that sends a dna sequence to a server

from seq import Seq
import socket

# Create a loop
while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Configuration of the server
    PORT = 8080
    IP = "212.128.253.80"
    
    # Connect to the server
    s.connect((IP, PORT))
    
    # Convert the sequence entered into the class Seq
    sequence = Seq(input("Enter the sequence: "))
    
    # To obtain the complement and the reverse of the sequence
    seq_c = sequence.complement()
    seq_r = sequence.reverse()
    
    # Transform it from object to sequence (string)
    complement = seq_c.strbases
    reverse = seq_r.strbases
    
    # Send the message to the server
    s.send(str.encode("The complement sequence is: "))
    s.send(str.encode(complement))
    s.send(str.encode("\nThe reverse sequence is: "))
    s.send(str.encode(reverse))
    s.close()
    
