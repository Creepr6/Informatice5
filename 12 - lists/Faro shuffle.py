def nieuw_kaartspel(kleuren, waarden):
    nieuw_kaartspel = []
    for i in range(0, len(kleuren)):
        for k in range(0, len(waarden)):
            kaart = kleuren[i] + waarden[k]
            nieuw_kaartspel.append(kaart)

    return nieuw_kaartspel

def splits_kaartspel(kaarten):
    if len(kaarten) % 2 == 0:
        kaartspel1 = kaarten[0: round(len(kaarten) / 2)]
        kaartspel2 = kaarten[round(len(kaarten) / 2): len(kaarten)]

    else:
        kaartspel1 = kaarten[0: round((len(kaarten) - 1) / 2)]
        kaartspel2 = kaarten[round((len(kaarten)) / 2): len(kaarten)]

    return kaartspel1, kaartspel2

def faro_shuffle(kaartspel1, kaartspel2):
    faro_kaartspel = []

    for i in range(0, len(kaartspel1)):
        faro_kaartspel.append(kaartspel1[i])
        faro_kaartspel.append(kaartspel2[i])

    if len(kaartspel2) > len(kaartspel1):
        faro_kaartspel.append(kaartspel2[len(kaartspel2) - 1])

    return faro_kaartspel