# vraag 2 natuurlijke getallen van het interval ]0,20]

a = float(input('natuurlijk getal 1 element van ]0,20]: '))
b = float(input('natuurlijk getal 2 element van ]0,20]: '))

#bewerkingen a
bewerking = int(((10**0)*a))
bewerking2 = int(((10**1)*a))
bewerking3 = int(((10**2)*a))
bewerking4 = int(((10**3)*a))
bewerking5 = int(((10**4)*a))

#bewerkingen b
bbewerking = int(((10**0)*b))
bbewerking2 = int(((10**1)*b))
bbewerking3 = int(((10**2)*b))
bbewerking4 = int(((10**3)*b))
bbewerking5 = int(((10**4)*b))

#som
som = int(((10**0)*a) + ((10**0)*b))
som2 = int(((10**1)*a) + ((10**1)*b))
som3 = int(((10**2)*a) + ((10**2)*b))
som4 = int(((10**3)*a) + ((10**3)*b))
som5 = int(((10**4)*a) + ((10**4)*b))

#antwoorden
antwoord = str(bewerking) + ' + ' + str(bbewerking) + ' = ' + str(som)
antwoord2 = str(bewerking2) + ' + ' + str(bbewerking2) + ' = ' + str(som2)
antwoord3 = str(bewerking3) + ' + ' + str(bbewerking3) + ' = ' + str(som3)
antwoord4 = str(bewerking4) + ' + ' + str(bbewerking4) + ' = ' + str(som4)
antwoord5 = str(bewerking5) + ' + ' + str(bbewerking5) + ' = ' + str(som5)

#uitvoeren
print(antwoord)
print(antwoord2)
print(antwoord3)
print(antwoord4)
print(antwoord5)
