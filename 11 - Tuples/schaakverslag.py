def geldige_zet(zet):
    if len(zet) == 2:
        if zet[0] in 'abcdefgh' and zet[1] in '12345678':
           antwoord = True
        else:
           antwoord = False
    elif len(zet) == 3:
        if zet [0] in 'KDPLT' and zet[1] in 'abcdefgh' and zet[2] in '12345678':
           antwoord = True
        else:
           antwoord = False
    else:
        antwoord = False
    return antwoord

def geldige_zetten(zet):
    kaas = 0
    for i in range(0, len(zet)):
        if geldige_zet(zet[i]) == True:
            kaas += 1
    return kaas == len(zet)

#in de les:
def geldige_zet2(zet):

    #controleren of index 0 in K,L...
    if len(zet) == 3 and zet[0] in 'KDTLP' and zet[1] in 'abcdefgh' and zet[2] in '12345678':
        mes = True
    elif len(zet) == 2 and zet[0] in 'abcdefgh' and zet[1] in '12345678':
        mes = True
    else:
        mes = False
    return mes

def geldige_zetten2(zetten):

    i = 0

    while i < len(zetten) and geldige_zet2(zetten[i]):
        i += 1

    return i >= len(zetten)


