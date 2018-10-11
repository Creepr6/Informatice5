#invoer
l = float(input('breedte veld = '))
b = float(input('lengte veld = '))
c = float(input('aantal kubieke meter graan per hectare = '))
r = float(input('straal silo = '))
h = float(input('hoogte silo = '))

#berekeningen
from math import pi, floor
volume_silo = pi * (r**2) * h
hoeveelheid_graan = c * ((l * b) / 10000)
aantal_silos = floor(hoeveelheid_graan / volume_silo)
overschot = hoeveelheid_graan - (aantal_silos * volume_silo)
hoogte_overschot = overschot / (pi * (r**2))

#uitvoeren
print(aantal_silos)
print(hoogte_overschot)

