def hoogtemeters(hoogtes):
    antwoord = []
    i = 0
    while i < len(hoogtes) - 1:
        verschil = hoogtes[i + 1] - hoogtes[i]
        antwoord.append(verschil)
        i += 1
    return antwoord

def dalen_en_stijgen(hoogtes):
    stijgen = 0
    dalen = 0

    for i in range(0, len(hoogtes)):
        if hoogtes[i] < 0:
            dalen += hoogtes[i]
        elif hoogtes[i] > 0:
            stijgen += hoogtes[i]

    return abs(dalen), stijgen