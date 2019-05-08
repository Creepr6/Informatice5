def fruitmand_maken(lijst):
    nieuw = {}
    for element in lijst:
        nieuw[len(element)] = element
    return nieuw

def fruitmand_inpakken(lijst):
    lengtes, nieuw = list(lijst), []
    lengtes.sort()
    for element in lengtes:
        nieuw.append(lijst[element])
    return nieuw