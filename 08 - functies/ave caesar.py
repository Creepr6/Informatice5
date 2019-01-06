def is_letter(l):
    if l in 'abcdefghijklmnopqrstuvwxyz'  or l in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        return True

    else:
        return False


def roteer_letter(x, y):
    if x in 'abcdefghijklmnopqrstuvwxyz':
        if (ord(x) + y) > ord('z'):
            k = (ord(x) + y) - ord('z')
            letter = chr(ord('a') - 1 + k)
        else:
            letter = chr(ord(x) + y)
    else:
        if (ord(x) + y) > ord('Z'):
            k = (ord(x) + y) - ord('Z')
            letter = chr(ord('A') - 1 + k)
        else:
            letter = chr(ord(x) + y)
    return letter


def versleutel(x, y):
    boodschap = x
    nieuwe_boodschap = ''
    for letter in boodschap:
        if is_letter(letter) == True:
            nieuwe_letter = roteer_letter(letter, y)
            nieuwe_boodschap += nieuwe_letter
        else:
            nieuwe_boodschap += letter
    return nieuwe_boodschap

