def ontdubbelen(woord):
    nieuw_woord = ''
    for i in range(0, len(woord) - 1):
        if woord[i] == woord[i + 1]:
            nieuw_woord += ''
        else:
            nieuw_woord += woord[i]
    nieuw_woord += woord[len(woord) - 1]
    return nieuw_woord