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