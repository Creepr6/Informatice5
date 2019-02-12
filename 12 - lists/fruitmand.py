def fruitstuk_toevoegen(fruitmand, fruitstuk):
    nieuwe_fruitmand = []
    if len(fruitmand) == 1:
        if len(fruitmand[0]) != len(fruitstuk) and fruitmand != fruitstuk:
            nieuwe_fruitmand.append(fruitstuk)
            nieuwe_fruitmand.append(fruitmand[0])
        else:
            nieuwe_fruitmand.append(fruitstuk)

    else:
        if fruitmand.count(fruitstuk) == 0:
            nieuwe_fruitmand.append(fruitstuk)

        for i in range(0, len(fruitmand)):


            if len(fruitmand[i]) != len(fruitstuk):
                nieuwe_fruitmand.append(fruitmand[i])
    nieuwe_fruitmand.sort(key=len)

    return nieuwe_fruitmand

def maak_fruitmand(fruitstukken):

    fruitmand = []
    fruitmand.append(fruitstukken[0])

    if len(fruitstukken) != 1:
        for i in range(0, len(fruitstukken)):
            fruitmand = fruitstuk_toevoegen(fruitmand, fruitstukken[i])

    return fruitmand