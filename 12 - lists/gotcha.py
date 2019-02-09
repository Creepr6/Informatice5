def ik_heb_gemoord(opdrachtenlijst, moordenaar):
    k = opdrachtenlijst.index(moordenaar)
    if k == len(opdrachtenlijst) - 2:
        nieuwe_opdracht = opdrachtenlijst[0]
        nieuwe_opdrachtenlijst = opdrachtenlijst[0: len(opdrachtenlijst) - 1]

    elif len(opdrachtenlijst) == 1:
        nieuwe_opdracht = opdrachtenlijst[k]
        nieuwe_opdrachtenlijst = opdrachtenlijst

    elif k == len(opdrachtenlijst) - 1:
        nieuwe_opdracht = opdrachtenlijst[1]
        nieuwe_opdrachtenlijst = opdrachtenlijst[1: len(opdrachtenlijst)]

    else:
        nieuwe_opdracht = opdrachtenlijst[k + 2]
        nieuwe_opdrachtenlijst = opdrachtenlijst[0:k + 1] + opdrachtenlijst[k + 2:len(opdrachtenlijst)]

    return nieuwe_opdracht, nieuwe_opdrachtenlijst

def ik_ben_vermoord(opdrachtenlijst, vermoorde):
    positie = opdrachtenlijst.index(vermoorde)
    return ik_heb_gemoord(opdrachtenlijst, opdrachtenlijst[positie-1])