bedrag = 0
product = 1
while product > 0:
      bedrag += product
      product = float(input('bedrag: '))

x = bedrag - 1

print('De totale prijs is € {:.2f}'.format(x))
