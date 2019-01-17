def dronken_voeren(woord):
    dronken_woord = woord[0]
    for i in range(1, len(woord)):
        if i % 2 == 0:
            dronken_woord += woord[i].upper()
        elif dronken_woord[i - 1] in 'AEOIU':
            dronken_woord += woord[i].upper()
        else:
            dronken_woord += woord[i].lower()

    return dronken_woord




