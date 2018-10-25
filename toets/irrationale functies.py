#invoer
x =  float(input('een getal x∈R: '))

#berekeningen
from math import sqrt
if x < 2:
    mes = '{:.2f}'.format(x) + ' ∉ dom(f)'
if x == 2:
    mes =  '{:.2f}'.format(x) + ' is nulpunt van f'
if x > 2:
    y = sqrt(x - 2)
    mes = 'f(' + '{:.2f}'.format(x) + ')' + ' = ' +  '{:.2f}'.format(y)

#uitvoer
print(mes)




