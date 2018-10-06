# rechthoekszijdes vragen
a = float(input('rechthoekszijde 1 = '))
b = float(input('rechthoekszijde 2 = '))

#schuine zijde
ck = (a**2) + (b**2)
from math import sqrt
c = sqrt(ck)

#antwoord
antwoord = 'In een rechthoekige driehoek met rechthoekszijden a = ' + '{:.2f}'.format(a) + ' en b = ' + '{:.2f}'.format(b) + ' is de schuine zijde ' + '{:.2f} '.format(c)

#uitvoeren
print(antwoord)
