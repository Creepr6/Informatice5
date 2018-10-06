#invoer
rk = float(input('straal kleine cirkel = '))
rg = float(input('straal grote cirkel = '))

#aantal cirkels die erin passen benaderen
from math import floor
x = 0.83 * ((rg**2)/(rk**2)) - 1.9
n = floor(x)

#beddekingsgraad berekenen
from math import pi
oppk = (rk ** 2) * pi
oppg = (rg ** 2) * pi
procent = ((n * oppk) / oppg) * 100
bedekingsgraad = '{:.2f}'.format(procent)

#antwoord
antwoord = str(n) + ' kleine cirkels bedekken ' + str(bedekingsgraad) + '%' + ' van de grote cirkel'

#uitvoer
print(antwoord)