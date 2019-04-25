def synoniemen(tekst, synoniemenwoordenboek):
    tekst = tekst.split()
    nieuwe_tekst = []
    for i in range(len(tekst)):
        if tekst[i] in synoniemenwoordenboek:
            nieuwe_tekst.append(synoniemenwoordenboek[tekst[i]])
        else:
            nieuwe_tekst.append(tekst[i])

    nieuwe_tekst = ' '.join(nieuwe_tekst)

    return nieuwe_tekst
