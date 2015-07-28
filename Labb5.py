# -*- coding: utf-8 -*-    # Behövs i python 2 för åäö
# Labb 5 i tilpro
# Rita upp ett gränssnitt

from Tkinter import *
import matriskoll

class Kryssruta(Button):
    """ Knapp som kryssas i/ur när man trycker på den """

    def __init__(self, master = None, nr = 0, rad = 0, kolumn = 0):
        Button.__init__(self, master)
        self.master = master
        self.nr = nr
        self.rad = rad
        self.kolumn = kolumn
        self.kryssad = False
        self["command"] = self.kryssa
        #self["text"] = str(self.rad)+","+str(kolumn)
        
    def kryssa(self):
        if not self.kryssad:
            self["text"] = "X"
            self.kryssad = True
        elif self["text"] == "X":
            self["text"] = "O"
        elif self["text"] == "O":
            self["text"] = "X"
        self.master.matrisKontroll()
        self.master.bytInforad()
        
class KnappMatris(Frame):
    """En lista med kryssrutor som ritas som en matris"""
    def __init__(self, master = None, rader = 5, kolumner = 5):
        Frame.__init__(self, master)
        self.grid()
        self.rader = rader
        self.kolumner = kolumner
        self.antal = rader*kolumner
        self.skapaKryssrutor()
        self.info = self.setInfo()
        self.inforad = Label(master, textvariable = self.info)
        self.pynta(self.inforad, bredd = (self.kolumner+2)*3)
        self.inforad.grid(row = self.rader, column = 0)

    def setInfo(self):
        info = StringVar()
        info.set("X tur")
        return info

    def bytInforad(self):
        if self.info.get() == "X tur":
            self.info.set("O:s tur")
        else:
            self.info.set("X tur")
    
    def pynta(self, komponent, bredd = 3, hojd = 1, bakgrundsfarg = "white", textfarg = "black", font = ("Ubuntu Mono", 20, "normal")):
        komponent["width"] = bredd
        komponent["height"] = hojd
        komponent["bg"] = bakgrundsfarg
        komponent["fg"] = textfarg
        komponent["font"] = font

    def skapaKryssrutor(self):
        self.knapplista = []
        for nr in range(self.antal):
            rad = nr//self.kolumner
            kolumn = nr%self.kolumner
            ny = Kryssruta(self, nr, rad, kolumn)
            self.pynta(ny)
            ny.grid(row = ny.rad, column = ny.kolumn)
            self.knapplista.append(ny)

    def kryssvektor(self):
        """ Returnerar en lista med pspelbanan """
        v = [" "]*self.antal
        index = 0
        for knapp in self.knapplista:
            if knapp.kryssad:
                v[index] = knapp["text"]
            index += 1
        return v

    def kryssmatris(self):
        """ Returnerar en matris med spelbanan """
        vektor = self.kryssvektor()
        matris = []
        for i in range(self.rader):
            rad_temp = []
            for j in range(self.kolumner):
                rad_temp.append(vektor[(i-1)*(self.kolumner)+j])
            matris.append(rad_temp)
        return matris

    def matrisKontroll(self):
        matris = self.kryssmatris()
        resultat = matriskoll.kollaMatris(matris)
        matriskoll.skrivaMatris(matris)
        if resultat == True:
            print "Vi har en vinnare!"
        else:
            print "Ingen har vunnit än..."
        
def main():
    rot = Tk()
    matris = KnappMatris(rot, rader = 10, kolumner = 10)
    matris.matrisKontroll()
    matris.mainloop()

main()
    

        
    
