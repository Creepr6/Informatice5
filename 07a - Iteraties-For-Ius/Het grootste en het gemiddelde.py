#invoer
kaas = int(input('aantal getallen:'))

#berekenen
from math import unlimited
x = 0
grootste = -10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
for i in range(kaas):
   getal = int(input('getal: '))
   x += getal
   gemiddelde = (x / kaas)
   if getal > grootste:
      grootste = getal

#antwoorden
antwoord = 'Het grootste getal is ' + str(grootste) + ' en het gemiddelde is ' + '{:.2f}'.format(gemiddelde)

#uitvoer
print(antwoord)







