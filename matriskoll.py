#-*- coding: utf-8 -*-
# Kollar efter 5 i rad

import copy

def kollaMatris(matris):
    resultat = kollaHor(matris)
    if resultat == True:
        return True
    resultat = kollaVer(matris)
    if resultat == True:
        return True
    return False

def kollaRad(vektor):
    counter = 0
    antal_i_rad = 5
    for i in range(len(vektor)):
        # Startklausul
        if i == 0:
            counter += 1
            continue
        if vektor[i] == vektor[i-1]:
            counter += 1
        else:
            counter = 1
        print counter
        if counter == antal_i_rad:
            return True
    return False

def kollaHor(matris):
    for rad in matris:
        resultat = kollaRad(rad)
        if resultat == True:
            return True
    return False

def kollaVer(matris):
    vertMatris = raderTillKolumner(matris)
    resultat = kollaHor(vertMatris)
    return resultat

def kollaDiagonal(matris):
    """Kollar både höger och vänster diagonal"""
    antal_i_rad = 5
    rader = len(matris)
    kolumner = len(matris[0])
    maxRader = rader - (antal_i_rad - 1)
    maxKolumner = kolumner - (antal_i_rad - 1)
    # Kolla alla diagonaler som startar i kolumn 0 utom [0,0]
    diagonalRader = range(maxRader)
    diagonalRader.remove(0)
    for i in diagonalRader:
        diagonal = hamtaDiagonal(matris, rad = i)
        print(diagonal)
        resultat = kollaRad(diagonal)
        if resultat == True:
            return True
    # Kolla alla diagonaler som startar i rad 0
    for i in range(maxKolumner):
        print "i=" + str(i)
        diagonal = hamtaDiagonal(matris, kolumn = i)
        print(diagonal)
        resultat = kollaRad(diagonal)
        if resultat == True:
            return True
    return False
    
def hamtaDiagonal(matris, rad = 0, kolumn = 0):
    antal_i_rad = 5
    rader = len(matris)
    kolumner = len(matris[0])
    vektor = []
    while rad<=(rader-1) and kolumn<=(kolumner-1):
        element = matris[rad][kolumn]
        vektor.append(element)
        rad += 1
        kolumn += 1
    return vektor

def raderTillKolumner(matris):
    flippadMatris = copy.deepcopy(matris)
    rader = len(matris)
    kolumner = len(matris)
    for i in range(rader):
        for j in range(kolumner):
            flippadMatris[j][i] = matris[i][j]
    return flippadMatris

def horisontellSpeglingMatris(matris):
    speglad_temp = zip(*matris[::-1])
    speglad = copy.deepcopy(speglad_temp)
    return speglad
    

def koraTest(test):
    """ Skriver ut snygga tester"""
    print 'Kör test: ' + test['name']
    print 'Förväntat utfall: ' + test['out']
    outcome = kollaVer(test['vektor'])
    print 'Utfall blev: ' + str(outcome) + '\n'

def skrivaMatris(matris):
    """ Skriver ut matriser snyggare än med print"""
    print 'Skriver ut matris...'
    for row in matris:
        print row

def main():
    verTrue = [['x', 'x', '0', 4, 'h', 3, 1, 5, 3],
               ['x', 'c', 'f', '0', 'h', 3, 1, 5, 3],
               ['r', '4', 'f', 4, '0', 3, 1, 5, 3],
               ['x', 'x', 'x', 'x', '0', '0', 1, 5, 3],
               ['x', 'c', 'f', 4, 'h', 3, '0', '0', 3],
               ['x', 'c', 'f', 4, 'h', 3, 1, 5, '0']]

    falseMatrix = [['x', 'x', '0', 4, 'h'],
                    ['x', 'c', 'f', 't', 'h'],
                    ['x', '4', 'f', 4, 'h'],
                    ['e', 'x', 'x', 'x', 'x'],
                    ['x', 'c', 'f', 4, 'h']]


    res = kollaDiagonal(verTrue)
    print res
main()
