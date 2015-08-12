#!/usr/bin/python           
import socket, pickle
from Tkinter import *

def connectToServer(port):
    s = socket.socket()        
    host = socket.gethostname()       
    s.connect((host, port))
    return s

def main():
    port = 12345
    s = connectToServer(port)
    
    while True:
        x = s.recv(1024)            #! Spara mottaget data i x
        if x:
            lista = pickle.loads(x)
            print lista
            if lista == "exit":
                break
            x = None
        s.close

main()
