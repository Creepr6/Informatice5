def maaltijdprijs(maaltijdtype, aantal):
    maaltijdprijs = 0

    if maaltijdtype == 'middagmaal':
        maaltijdprijs += aantal * 5.3

    elif maaltijdtype == 'soep':
        maaltijdprijs += aantal * 1.7

    elif maaltijdtype == 'vieruurtje':
        maaltijdprijs += aantal * 2.3
    return maaltijdprijs

def dagprijs(bestelling):

    prijs = 0
    # overloop bestelling in stapjes van 2
    for i in range(0, len(bestelling), 2):

        prijs += maaltijdprijs(bestelling[i], bestelling[i + 1])


    return prijs

print(dagprijs(('middagmaal', 2, 'soep', 2, 'vieruurtje', 2)))

def weekprijs(bestelling):

    weekprijs = 0

    for dag in bestelling:
        weekprijs += dagprijs(dag)

    return weekprijs