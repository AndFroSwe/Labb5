#-*- coding: utf-8 -*-
# Kollar efter 5 i rad

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

def koraTest(test):
    """ Skriver ut snygga tester"""
    print 'Kör test: ' + test['name']
    print 'Förväntat utfall: ' + test['out']
    outcome = kollaRad(test['vektor'])
    print 'Utfall blev: ' + str(outcome) + '\n'

def main():
    test1 = {'name':'test1', 'vektor':['x', 'x', 'x', 'x', 'x'], 'out':'True'} 
    test2 = {'name':'test2', 'vektor':[' ', ' ', 'x', 'x', 'x', 'x', 'x'], 'out':'True'}
    test3 = {'name':'test3', 'vektor':['x', 'x', 'x', ' ', 'x'], 'out':'False'}
    koraTest(test1)
    koraTest(test2)
    koraTest(test3)

main()
