#kaas
kaas = int(input('donneer getal: '))
a = 2
b = 1

while a < kaas:
    if (kaas % a ) == 0:
        mess = '{} is geen priemgetal'.format(kaas)
        b = 0
    a += 1
if b and kaas != 1:
    mess = '{} is een priemgetal'.format(kaas)
elif kaas == 1:
    mess = '{} is geen priemgetal'.format(kaas)

print(mess)
#klas
getal = int(input('getal: '))
#zolang je het niet kan delen door 2,3,4 is het allicht een priemgetal
deler = 2

while getal % deler != 0 and getal != 1:
    deler += 1
    print(deler)
if deler == getal:
    print('priemgetal')
else:
    print('geen priemgetal')
