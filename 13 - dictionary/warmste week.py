def gift_inschrijven(klasbedrag, giften):

    if klasbedrag[0] in giften:
        giften[klasbedrag[0]] += klasbedrag[1]
    else:
        giften[klasbedrag[0]] = klasbedrag[1]

    return giften
