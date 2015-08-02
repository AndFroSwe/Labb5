#!/usr/bin/python          

import socket, pickle              
from Tkinter import *
import Kryssruta

def connectToKlient():
   s = socket.socket()        
   host = socket.gethostname()
   port = 12345               
   s.bind((host, port))       
   s.listen(5)
   c, mess = s.accept()     # Establish connection with client.
   print mess
   return c

def main():
   c = connectToKlient()
   rot = Tk()
   

   mainloop()




   while True:
      message = raw_input('-->')
      gurka = pickle.dumps(message)
      c.send(gurka)
      if message == "exit":
         break   
   c.close()

main()
