#invoer
t = float(input('tijd in nanoseconden = '))

#andere getallen voor in formule
c = 299792458
n = 1.000277
tt = t * (10**-9)

#formule
formule = c * tt
formule /= 2 * n

#antwoord
antwoord = str(formule) + ' meter'

#uitvoeren
print(antwoord)