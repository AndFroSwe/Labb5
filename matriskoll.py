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
    vertMatris = flippaMatris(matris)
    resultat = kollaHor(vertMatris)
    return resultat

def kollaDia(matris):
    """Kollar både höger och vänster diagonal"""
    resultat = kollaHoger(matris)
    if resultat == True:
        return True
    resultat = kollaVanster(matris)
    if resultat == True:
        return True
    return False

def kollaHoger(matris, rad = 0, kolumn = 0):
    antal_i_rad = 5
    rader = len(matris)
    kolumner = len(matris[0])
    maxRader = rader - (antal_i_rad - 1)
    maxKolumner = kolumner - (antal_i_rad - 1)
    vektor = []
    while rad<=(rader-1) and kolumn<=(kolumner-1):
        element = matris[rad][kolumn]
        vektor.append(element)
        rad += 1
        kolumn += 1
    return vektor
        
def hamtaDiagonal(matris, radStart, kolumnStart):
    vektor = []
    rader = len(matris)
    kolumner = len(matris[0])
    maxRader = rader - (antal_i_rad - 1)
    maxKolumner = kolumner - (antal_i_rad - 1)

def flippaMatris(matris):
    flippadMatris = copy.deepcopy(matris)
    rader = len(matris)
    kolumner = len(matris)
    for i in range(rader):
        for j in range(kolumner):
            flippadMatris[j][i] = matris[i][j]
    return flippadMatris
    

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
    verTrue = [['x', 'x', '0', 4, 'h'],
               ['x', 'c', 'f', 4, 'h'],
               ['r', '4', 'f', 4, 'h'],
               ['x', 'x', 'x', 'x', 'x'],
               ['x', 'c', 'f', 4, 'h']]

    falseMatrix = [['x', 'x', '0', 4, 'h'],
                    ['x', 'c', 'f', 't', 'h'],
                    ['x', '4', 'f', 4, 'h'],
                    ['e', 'x', 'x', 'x', 'x'],
                    ['x', 'c', 'f', 4, 'h']]


    res = kollaHoger(verTrue, rad = 4)
    print res
main()
