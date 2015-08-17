# -*- coding: utf-8 -*- 
import Kryssruta
import threading, socket

class Klient(Kryssruta.KnappMatris):
    def __init__(self):
        Kryssruta.KnappMatris.__init__(self, startar = True)
        self.connectToServer()
        self.startaTaEmot()
                
    def connectToServer(self):
        self.s = socket.socket()
        host = socket.gethostname()
        port = 12355
        self.s.connect((host, port))
        print "Connected!"
        
    def startaTaEmot(self):
        self.t = threading.Thread(target = self.taEmotSpelplan)
        self.t.start()

matris = Klient()
matris.mainloop()
