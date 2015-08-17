# -*- coding: utf-8 -*- 
# Labb 5 i tilpro
# Rita upp ett grÃ¤nssnitt

#!/usr/bin/python          

import socket, pickle, matriskoll, threading, time
from Tkinter import *

class Kryssruta(Button):
    """ Knapp som kryssas i/ur när man trycker på den """

    def __init__(self, master = None, nr = 0, rad = 7, kolumn = 7):
        Button.__init__(self, master)
        self.master = master
        self.nr = nr
        self.rad = rad
        self.kolumn = kolumn
        self.kryssad = False
        self["command"] = self.kryssa
        self["text"] = " " 

    def kryssa(self):
        nastaSpelare = self.master.hamtaNastaSpelare()
        if self.master.minTur():
            if not self.kryssad:
                if self.master.spelare == "X":
                    self.setTecken("X")
                    self.master.okaOmgang()
                elif self.master.spelare == "O":
                    self.master.okaOmgang()
                    self.setTecken("O")
                else:
                    self["text"] = "ERROR, okänd spelare"
                    return
                self.master.skickaSpelplan()
                self.master.matrisKontroll()
            else:
                print "Ruta upptagen"
                return
        else:
            print "Vänta på din tur"
            
    def setTecken(self, tecken):
        self.config(text = tecken)
        self.kryssad = True

    def hamtaTecken(self):
        return self["text"]

    def stangFonster(self):
        self.configure(command = lambda: self.master.master.destroy())
    
class KnappMatris(Frame):
    """En lista med kryssrutor som ritas som en matris"""
    def __init__(self, startar = True, rader = 10, kolumner = 10):
        self.master = Tk()
        Frame.__init__(self, self.master)
        self.grid()
        self.rader = rader
        self.kolumner = kolumner
        self.antal = rader*kolumner
        self.info = self.setInfo(startar)
        self.skapaKryssrutor()
        self.inforad = Label(self.master, textvariable = self.info)
        self.pynta(self.inforad, bredd = (self.kolumner+2)*3)
        self.inforad.grid(row = self.rader, column = 0)
        self.omgang = self.setStartnummer(startar)
        self.end = False
 
# Skapa spelplan 

    def setInfo(self, startar):
        info = StringVar()
        if startar == True:
            text = "Du är spelare X. Din tur."
            self.spelare = "X"
        else:
            text = "Du är spelare O. Motståndarens tur."
            self.spelare = "O"
        info.set(text)
        return info
    
    def skapaKryssrutor(self):
        self.knapplista = []
        for nr in range(self.antal):
            rad = nr//self.kolumner
            kolumn = nr%self.kolumner
            ny = Kryssruta(self, nr, rad, kolumn)
            self.pynta(ny)
            ny.grid(row = ny.rad, column = ny.kolumn)
            self.knapplista.append(ny)

    def pynta(self, komponent, bredd = 3, hojd = 1, bakgrundsfarg = "white", textfarg = "black", font = ("Calibri", 20, "normal")):
        komponent["width"] = bredd
        komponent["height"] = hojd
        komponent["bg"] = bakgrundsfarg
        komponent["fg"] = textfarg
        komponent["font"] = font

    def setStartnummer(self, startar):
        if startar == True:
            return 0
        else:
            return 1
# Hantera turer
    def okaOmgang(self):
        self.omgang += 1
        nasta = self.hamtaNastaSpelare()
        infostrang = nasta + " tur"
        self.bytInfo(infostrang)
            
    def hamtaNastaSpelare(self):
        if self.omgang%2 != 0:
            return "Motståndarens"
        else: 
            return "Din"

    def minTur(self):
        return self.omgang%2 == 0

    def bytInfo(self, text):
        self.info.set(text)
        
    def hamtaSpelare(self):
        if self.omgang%2 != 0:
            return "Din"
        else: 
            return "Motståndarens"

 # Skicka och ta emot       
    def skickaSpelplan(self):
        spelplan = self.hamtaKryssvektor()
        paket = pickle.dumps(spelplan)
        self.s.send(paket)
    
    def taEmotSpelplan(self):
        while True:
            if self.end == True: break
            mottaget = self.s.recv(1024)
            plan = pickle.loads(mottaget)
            self.setSpelplan(plan)
            mottaget = plan = None # Återställa variabler
 
    def setSpelplan(self, plan):
        for index, tecken in enumerate (plan):
            if not self.knapplista[index].kryssad == True and not tecken == " ": 
                self.knapplista[index].setTecken(tecken)
                self.okaOmgang()
        self.matrisKontroll()

# Kontrollera om vinst 
    def matrisKontroll(self):
        print "Kollar om vinst"
        matris = self.kryssmatris()
        resultat = matriskoll.kollaMatris(matris)
        if resultat == True:
            spelare = self.hamtaSlutSpelare()
            vinnarString = spelare + " vinner! Tryck för att avsluta."
            self.bytInfo(vinnarString)
            self.stoppaSpel()

    def kryssmatris(self):
        vektor = self.hamtaKryssvektor()
        matris = []
        for i in range(self.rader):
            rad_temp = []
            for j in range(self.kolumner):
                rad_temp.append(vektor[(i)*(self.kolumner)+j])
            matris.append(rad_temp)
        return matris

    def hamtaKryssvektor(self):
        """ Returnerar en lista med spelbanan """
        v = [" "]*self.antal
        index = 0
        for knapp in self.knapplista:
            if knapp.kryssad:
                v[index] = knapp.hamtaTecken()
            index += 1
        return v

# Avsluta
    def stoppaSpel(self):
        self.end = True
        for knapp in self.knapplista:
            knapp.stangFonster()

    def hamtaSlutSpelare(self):
        if self.omgang%2 != 0:
            return "Du"
        else: 
            return "Motståndaren" 

   
