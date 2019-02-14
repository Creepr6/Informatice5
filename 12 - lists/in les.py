def ik_heb_gemoord(lijst, moordenaar):
    # slachtoffer schrappen
    index_moordenaar = lijst.index(moordenaar)
    # rest van index gedeeld door len lijst (hier: 0 = 0 , 1=1, 2 = 2, 3=3, 4=0 )
    index_slachtoffer = (index_moordenaar + 1) % len(lijst)

    lijst[index_slachtoffer: index_slachtoffer + 1]

    #nieuw doel aan moordenaar geven
    index_moordenaar = lijst.index(moordenaar)
    index_nieuw_doel = (index_moordenaar + 1) % len(lijst)

    return lijst, lijst[index_nieuw_doel]

