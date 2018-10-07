#invoer
r = float(input('afstand tussen satelliet en middelpunt aarde (in m) = '))
v = float(input('de snelheid van de satelliet ten opzichte van de Aarde (in meter/seconde) = '))

#noodzakelijkheden voor formule
u = 398600.4418 * (10**9)

#berekenen
a = (r * u) /((2 * u) - ((v**2)*r))
from math import pi, sqrt
p = (2 * pi) * sqrt(((a**3) / u))

#periode omzeten in dagen uren en minuten
from math import floor
d = floor(((p / 60) / 60) / 24)
x = p - (((d * 24) * 60 ) * 60)
u = floor((x / 60) / 60)
y = x - ((u * 60) *60)
m = floor(y / 60)

#antwoord
antwoord1 = 'grote as: ' + str(a) + ' meter'
antwoord2 = 'periode: ' + str(p) + ' seconden'
antwoord3 = 'periode: ' + str(d) + ' dagen, ' + str(u) + ' uren en ' + str(m) + ' minuten'

#uitvoer
print(antwoord1)
print(antwoord2)
print(antwoord3)
