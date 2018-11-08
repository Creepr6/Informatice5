#invoer
t = float(input('aantal uren na opname XTC: '))

#berekeningen
from math import pi, floor
c = (pi * t)
c /= ((t * t) + 2)
k = floor(c / 10)
#antwoord
antwoord = str(k)
#uitvoeren
print(antwoord)
