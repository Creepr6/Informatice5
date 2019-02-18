def volgende_rij(rij):
    volgende_rij = []
    for i in range(len(rij) -1):
        if rij[i] == rij[i + 1]:
            volgende_rij.append(rij[i])
        else:
            hulp = ['G', 'R', 'Y']
            hulp.remove(rij[i])
            hulp.remove(rij[i + 1])
            volgende_rij.append(hulp[0])
    return volgende_rij

def driehoek(rij):
    antwoord = [rij]
    for i in range(1, len(rij)):
        antwoord.append(volgende_rij(antwoord[i -1]))

    return antwoord

def kleuren(kleurendriehoek):
    groen = 0
    geel = 0
    rood = 0
    for i in range(len(kleurendriehoek)):
        for k in range(len(kleurendriehoek[i])):
            if kleurendriehoek[i][k] == 'Y':
                geel += 1
            elif kleurendriehoek[i][k] == 'G':
                groen += 1
            elif kleurendriehoek[i][k] == 'R':
                rood += 1

    return groen, rood, geel
