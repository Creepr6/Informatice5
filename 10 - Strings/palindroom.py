def is_palindroom(woord):
    t = ''
    for i in range(0, len(woord)):
        if woord[i] == woord[(len(woord) - 1 - i)]:
            t += '1'
        else:
            t += '2'
    if '2' in t:
        return False
    else:
        return True

