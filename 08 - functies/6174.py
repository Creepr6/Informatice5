

def splits(x):
     from math import floor
     getal1 = floor(x / 1000)
     tussen_getal1 = x - (getal1 * 1000)
     getal2 = floor(tussen_getal1 / 100)
     tussen_getal2 = tussen_getal1 - (getal2 * 100)
     getal3 = floor(tussen_getal2/10)
     getal4 = tussen_getal2 - (getal3 * 10 )
     return getal1, getal2, getal3, getal4



def oplopende_cijfers(a,b,c,d):
    kaas = a, b, c, d
    antwoord = tuple(sorted(kaas))
    return antwoord



def op_af_getallen(a, b, c, d):
   oplopende = str(a) + str(b) + str(c) + str(d)
   aflopende = ''
   for letter in oplopende:
       aflopende = letter + aflopende
   return oplopende, aflopende



def verschil(x,y):
    w = int(x)
    z = int(y)
    verschil = str(w - z)
    return verschil


def kaprekar(n):
    bericht =''
    a = n // 1000
    b = (n - (a * 1000)) // 100
    c = (n - (a * 1000) - (b * 100)) // 10
    d = n - (a * 1000) - (b * 100) - (c * 10)
    getal1 = min(a, b, c, d)
    getal2 = max(min(a, b, c), min(b, c, d), min(a, b, d), min(a, c, d))
    getal3 = min(max(a, b, c), max(b, c, d), max(a, b, d), max(a, c, d))
    getal4 = max(a, b, c, d)
    oplopend = str(getal1) + str(getal2) + str(getal3) + str(getal4)
    aflopend = str(getal4) + str(getal3) + str(getal2) + str(getal1)

    if int(aflopend) - int(oplopend) == 6174:
        bericht = '{} - {} = {}'.format(aflopend, oplopend, int(aflopend) - int(oplopend))
    else:

        while int(aflopend) - int(oplopend) != 6174:
            bericht += '{} - {} = {}\n'.format(aflopend, oplopend, int(aflopend) - int(oplopend))
            n = int(aflopend) - int(oplopend)
            a = n // 1000
            b = (n - (a * 1000)) // 100
            c = (n - (a * 1000) - (b * 100)) // 10
            d = n - (a * 1000) - (b * 100) - (c * 10)
            getal1 = min(a, b, c, d)
            getal2 = max(min(a, b, c), min(b, c, d), min(a, b, d), min(a, c, d))
            getal3 = min(max(a, b, c), max(b, c, d), max(a, b, d), max(a, c, d))
            getal4 = max(a, b, c, d)
            oplopend = str(getal1) + str(getal2) + str(getal3) + str(getal4)
            aflopend = str(getal4) + str(getal3) + str(getal2) + str(getal1)
        a = n // 1000
        b = (n - (a * 1000)) // 100
        c = (n - (a * 1000) - (b * 100)) // 10
        d = n - (a * 1000) - (b * 100) - (c * 10)
        getal1 = min(a, b, c, d)
        getal2 = max(min(a, b, c), min(b, c, d), min(a, b, d), min(a, c, d))
        getal3 = min(max(a, b, c), max(b, c, d), max(a, b, d), max(a, c, d))
        getal4 = max(a, b, c, d)
        oplopend = str(getal1) + str(getal2) + str(getal3) + str(getal4)
        aflopend = str(getal4) + str(getal3) + str(getal2) + str(getal1)
        bericht += '{} - {} = {}'.format(aflopend, oplopend, int(aflopend) - int(oplopend))
    return bericht
