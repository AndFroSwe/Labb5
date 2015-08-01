#!/usr/bin/python           # This is server.py file
# modified http://www.tutorialspoint.com/python/python_networking.htm

import socket               # Import socket module
import pickle

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.

#lista = [1, 2, 5]           #! datastruktur
#x = pickle.dumps(lista)     #! paketera med pickle

c, mess = s.accept()     # Establish connection with client.
print mess

while True:
   message = raw_input('-->')
   gurka = pickle.dumps(message)
   c.send(gurka)
   if message == "exit":
      break   
   
c.close()