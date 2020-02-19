def bestaat_weg(vertrek, aankomst, kaart):
    setaankomst = {aankomst}
    for key in kaart.keys():
        if key == vertrek:
            if setaankomst.issubset(kaart[key]):
                antwoord = True
            else:
                antwoord = False

    return antwoord


def geen_dubbelburen(stad, steeed, kaart):
    antwoord = kaart[stad].difference(kaart[steeed]).union(kaart[steeed].difference(kaart[stad]))
    antwoord.discard(stad)
    antwoord.discard(steeed)
    return antwoord


def bereikbaarheid_meest_afgelegen_stad(kaart):
    kleinste = 9999999999999999999999999999999999999999999999999999999999
    for key in kaart.keys():
        if len(kaart[key]) < kleinste:
            kleinste = len(kaart[key])

    return kleinste

def bestaat_route(lijst, kaart):
    bestaat = 0
    for i in range(len(lijst) - 1):
        if bestaat_weg(lijst[i], lijst[i + 1], kaart) is True:
            bestaat += 1

    return bestaat == len(lijst) - 1
