#!/usr/bin/python           # This is client.py file
# modified http://www.tutorialspoint.com/python/python_networking.htm

import socket               # Import socket module
import pickle

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.connect((host, port))

while True:
    x = s.recv(1024)            #! Spara mottaget data i x
    if x:
            print "Mottagit meddelande"
            lista = pickle.loads(x)     #! packa upp med pickle
            print lista
            if lista == "exit":
                break
            x = None

s.close                     # Close the socket when done