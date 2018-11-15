#invoer
kaas = int(input('aantal getallen:'))

#berekenen
x = grootste
grootste = int(input('getal: '))
for i in range(kaas - 1):
   getal = int(input('getal: '))
   x += getal
   gemiddelde = (x / kaas)
   if getal > grootste:
      grootste = getal

#antwoorden
antwoord = 'Het grootste getal is ' + str(grootste) + ' en het gemiddelde is ' + '{:.2f}'.format(gemiddelde)

#uitvoer
print(antwoord)
