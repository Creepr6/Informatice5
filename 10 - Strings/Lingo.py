def hint(gok, woord):
    nieuw_woord = ''
    for i in range(0, len(gok)):
        if gok[i] == woord[i]:
            nieuw_woord += gok[i].upper()
        elif gok[i] in woord and gok[i] != woord[i]:
            nieuw_woord += gok[i]
        else:
            nieuw_woord += '.'
    return nieuw_woord

print(hint('spoed', 'depri'))