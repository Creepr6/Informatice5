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




