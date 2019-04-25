def bereken_prijs(boodschappenlijst):
    prijs = 0
    for item in boodschappenlijst:
        prijs += item[1]

    return prijs


def winkelbriefje(boodschappenlijst):
    producten = []
    for item in boodschappenlijst:
        producten.append(item[0])

    return producten

def sorteer(boodschappenlijst):
    from operator import itemgetter
    boodschappenlijst.sort(key=itemgetter(1))

    return boodschappenlijst

