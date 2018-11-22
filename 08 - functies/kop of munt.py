from random import randint
def gooi_muntstuk():
 rg = randint(0, 2)
 if rg == 0:
    muntstuk = 'kop'
 else:
    muntstuk = 'munt'
 return muntstuk
print(gooi_muntstuk())