def versleutel_woord(woord, n):
    nieuw_woord = ''
    for i in range(0, len(woord)):
        hoofdletter = woord[i].upper()
        hulp = chr(ord(hoofdletter) + n)
        if hulp == '@':
            hulp = ' '
        nieuw_woord += hulp
    return nieuw_woord

def versleutel_zin(zin, n):
    nieuwe_zin_hulp = versleutel_woord(zin, n)
    nieuwe_zin = ''
    for i in range(0, len(nieuwe_zin_hulp)):
        if nieuwe_zin_hulp[i] == chr(ord(' ') + n):
            nieuwe_zin += '@'
        else:
            nieuwe_zin += nieuwe_zin_hulp[i]
    return nieuwe_zin


#in de les
def versleutel_zin(zin, n):

    indexspatie = zin.find(' ')
    code = ''
    #tot er geen spaties meer zijn
    while indexspatie != -1:
        woord = zin[:indexspatie]
        zin = zin[indexspatie + 1:]

        code += '@' + versleutel_woord(zin, getal)
        indexspatie = zin.find(' ')

    if len(zin) > 0:
        code += '@' + versleutel_woord(zin, getal)

    return code
