fruitmand = {}
fruitstuk = input('fruitstuk: ')

while fruitstuk != 'stop':
    aantal = int(input('aantal: '))

    if fruitstuk in fruitmand:
        fruitmand[fruitstuk] += aantal
    else:
        fruitmand[fruitstuk] = aantal

    print(fruitmand)
    fruitstuk = input('fruitstuk: ')

fruitmand = {'kiwi': 3, 'bes': 12, 'peer': 5}

for fruit in fruitmand:
    print(fruit)
    print(fruit, fruitmand[fruit])

for key in fruitmand.keys():
    print(key)

for v in fruitmand.values():
    print(v)

for k, v in fruitmand.items():
    print('ik heb ' + str(v) + ' ' + k)

klas = {1: 'arnout', 2 : 'thibault', 'titularis': 'mr van der cruyssen'}

for k,v in klas.items():
    print(k, v)

cirkel = {'middelpunt': [0, 0], 'staal' : 5}

cirkel['middelpunt'][0] = 1
print(cirkel)



