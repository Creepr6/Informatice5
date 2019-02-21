def beweeg(coordinaat, pijltjestoets):
    #start coordinaten
    xcoordinaat = coordinaat[0]
    ycoordinaat = coordinaat[1]

    #beweging slang
    if pijltjestoets == '>':
        xcoordinaat += 1
    elif pijltjestoets == '<':
        xcoordinaat += -1
    elif pijltjestoets == '^':
        ycoordinaat += 1
    elif pijltjestoets == 'v':
        ycoordinaat += -1

    return xcoordinaat, ycoordinaat

def teruggekeerd(pijltjescombinatie):
    omhoog = pijltjescombinatie.count('^')
    omlaag = pijltjescombinatie.count('v')
    rechts = pijltjescombinatie.count('>')
    links = pijltjescombinatie.count('<')
    k = 0

    if omhoog == 1 and omlaag == 1:
        k += 1

    elif rechts == 1 and links == 1:
        k += 1

    return k == 1

def laatste_levende_positie(pijltjestoetsen):
    i = 1
    coordinaat = beweeg((0, 0), pijltjestoetsen[0])
    aantal_geldige_zetten = 1

    while i < len(pijltjestoetsen) and teruggekeerd([pijltjestoetsen[i - 1], pijltjestoetsen[i]]) is False:
        coordinaat = beweeg(coordinaat, pijltjestoetsen[i])
        i += 1
        aantal_geldige_zetten += 1

    return aantal_geldige_zetten, coordinaat[0], coordinaat[1]