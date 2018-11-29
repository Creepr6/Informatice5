#invoer
ss = float(input('De sneheid van Stijn uitgedrukt in m/s; '))
sk = float(input('De snelheid van Kaat uitgedrukt in m/s: '))
a = float(input('De afstand tussen beide huizen uitgedrukt in m: '))
afstand_tussen_beiden = a
aantal_seconden = 0

#berekenen
while afstand_tussen_beiden > 0:
    afstand_tussen_beiden -= (ss + sk)
    aantal_seconden += 1

#antwoord
antwoord = 'Na ' + str(aantal_seconden) + ' s hebben Stijn en Kaat elkaar ontmoet.'

#uitvoeren
print(antwoord)


