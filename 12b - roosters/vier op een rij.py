def printbaar_rek(zetten):
    antwoord = ''
    for i in range(len(zetten)):
        if len(zetten) - i == 1:
            hulp = zetten[0]
            for p in range(len(hulp)):
                antwoord += hulp[p]
        else:
            hulp = zetten[len(zetten) - 1 - i]
            for p in range(len(hulp)):
                antwoord += hulp[p]
            antwoord += '\n'

    return antwoord

def speel(kleur, positie, rekje):
    al_gespeeld = 0
    i = 0
    while al_gespeeld == 0 and i < len(rekje):
        if rekje[i][positie] == '0':
            rekje[i][positie] = kleur
            al_gespeeld += 1
        i += 1
    return rekje


