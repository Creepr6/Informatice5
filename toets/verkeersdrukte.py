# invoer
a = float(input('De verkeersdichtheid van het vrachtvervoer op het eerste rijvak: '))
b = float(input('De snelheid van het vrachtverkeer op het eerste rijvak: '))
c = float(input('De verkeersdichtheid van het personenvervoer op het tweede rijvak: '))
d = float(input('De snelheid van de personenwagens op het tweede rijvak: '))

# noodzakelijke berekeningen
k1 = (a * b) / 40
pv = min(k1, 1)
k2 = (c * d) / 40
pa = min(k2, 1)
t = abs(pv - pa)

# berekenen van kleurcode
if min(pv, pa) > 0.7:
    kleurcode = 'zwart'
elif max(pv, pa) > 0.7 and t < 0.2:
    kleurcode = 'rood'
elif t > 0.7:
    kleurcode = 'geel'
else:
    kleurcode = 'groen'

# uitvoer
print(kleurcode)

