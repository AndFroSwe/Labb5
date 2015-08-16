# -*- coding: utf-8 -*- 
import Kryssruta
import socket, threading

class Server(Kryssruta.KnappMatris):
    def __init__(self):
        Kryssruta.KnappMatris.__init__(self, True)
        self.connectToClient()
        self.startaTaEmot()
                
    def connectToClient(self):
        self.sock = socket.socket()
        host = socket.gethostname()
        port = 12345
        self.sock.bind((host, port))        # Bind to the port
        self.sock.listen(5)                 # Now wait for client connection.
        self.s, mess = self.sock.accept()     # Establish connection with client.
        print "Connected!"

matris = Server()
matris.mainloop()
