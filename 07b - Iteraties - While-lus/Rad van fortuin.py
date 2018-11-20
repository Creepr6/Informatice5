w = str(input('het verborgen woord: '))
g = int(input('het gedraaide geldbedrag'))
l = str(input('letter: '))
gewonnen = 0
woord = ''
while l in w and l not in woord:
    gewonnen += g
    woord += l
    l = str(input('letter: '))

print(str(gewonnen))
