def welkom(naam):
 print('Welkom terug ' + naam)
welkom('lieve sint')

def discriminant(a, b, c):
 return (b ** 2) - (4 * a * c)

print(discriminant(2 , 4, 2))

def is_priem(n):
 i = 2
 while i <= floor(sqrt(n)) and n % i != 0:
 i += 1
 return i == floor(sqrt(n)) + 1

appel = 'appel'
banaan = 'banaan'
kers = 'kers'
def print_fruit(appel):
 banaan = 'aapje'
 print(appel, banaan, kers)
print_fruit(banaan)
print(appel, banaan, kers)