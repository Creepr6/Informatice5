def is_letter(l):
    if l in 'abcdefghijklmnopqrstuvw'  or l in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        return 'True'

    else:
        return 'False'

x = str(input(''))
y = int(input('kaas'))
def roteer_letter(x,y):
    letter = chr(ord(x) + y)
    return letter

print(roteer_letter(x,y))