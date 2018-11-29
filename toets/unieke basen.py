#invoer
x = int(input('aantal basen: '))
woord = ''
aantal_basen = 0

#berekenen
for i in range(x):
    base = input('getal: ')
    if base in 'ATCG' and base not in woord:
        aantal_basen += 1
        woord += base + ' '

#antwoorden
if aantal_basen == 1:
    antwoord = 'De DNA-keting bevat ' + str(aantal_basen) + ' soort base: ' + woord

elif aantal_basen > 1:
    antwoord = 'De DNA-keting bevat ' + str(aantal_basen) + ' verschillende soorten basen: ' + woord

#uitvoer
print(antwoord)
