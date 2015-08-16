# -*- coding: utf-8 -*- 
import Kryssruta
import threading, socket

class Klient(Kryssruta.KnappMatris):
    def __init__(self):
        Kryssruta.KnappMatris.__init__(self)
        self.connectToServer()
        self.startaTaEmot()

    def startaTaEmot(self):
        self.t = threading.Thread(target = self.taEmotSpelplan)
        self.t.start()
    
    def connectToServer(self):
        self.s = socket.socket()
        host = socket.gethostname()
        port = 12345
        self.s.connect((host, port))
        print "Connected!"

matris = Klient()
matris.mainloop()
