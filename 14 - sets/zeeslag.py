def boot_overlappend(x, y):
    hulp = x.union(y)
    return len(hulp) != (len(x) + len(y))

def boot_toevoegen(boot, opstelling):

    if boot_overlappend(boot, opstelling) == False:
        antwoord = opstelling.union(boot)
    else:
        antwoord = opstelling

    return antwoord

def vuur(vakje, rooster):
    x = len(rooster)
    rooster.add(vakje)

    if len(rooster) > x:
        kaas = False
        rooster.remove(vakje)

    else:
        rooster.remove(vakje)
        kaas = True

    return kaas, rooster

