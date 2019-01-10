def germaniseer(zin):

    # alle letters overlopen
    for i in range(0, len(zin)):

        # is het een spatie?
        if zin[i] == ' ':
            #ja -> de volgende letter wordt een hoofdletter
            zin = zin[0: i + 1] + zin[i + 1].upper() + zin[i + 2:]

    return zin

#OF voor als op teinde spatie sta, twerkt wel nie
def germaniseer(zin):

    # alle letters overlopen
    for i in range(0, len(zin - 1)):

        # is het een spatie?
        if zin[i] == ' ':
            #ja -> de volgende letter wordt een hoofdletter
            zin = zin[0: i + 1] + zin[i + 1].upper() + zin[i + 2:]

    return zin






