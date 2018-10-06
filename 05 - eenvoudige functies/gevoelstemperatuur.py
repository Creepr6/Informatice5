#invoer
t = float(input('luchttemperatuur in graden Celsius = '))
w = float(input('windsnelheid in km/u = '))

#noodzakelijke aanpassingen voor formule
x = w / 3.6

#gevoelstemperatuur
gevoelstemperatuur = 13.12 + (0.6215 * t) + (((0.3965 * t) - 11.37) * ((3.6 * x)**0.16))

#uitvoer
print(gevoelstemperatuur)