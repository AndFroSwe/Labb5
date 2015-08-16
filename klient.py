# -*- coding: utf-8 -*- 
import Kryssruta
import threading, socket

class Klient(Kryssruta.KnappMatris):
    def __init__(self):
        Kryssruta.KnappMatris.__init__(self, False)
        self.connectToServer()
        self.startaTaEmot()
                
    def connectToServer(self):
        self.s = socket.socket()
        host = socket.gethostname()
        port = 12345
        self.s.connect((host, port))
        print "Connected!"

matris = Klient()
matris.mainloop()
