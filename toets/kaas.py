n = int(input('getal: '))
cijfers, ontbreken = '', ''
for i in range(1, 11):
 cijfers += str(n * i)
for c in '0123456789':
 if c not in cijfers:
    ontbreken += c
if len(ontbreken) == 0:
 print('Tafel van ' + str(n) + ' is een mooie tafel')
else:
 print('In de tafel van ' + str(n) + ' ontbre(e)k(t)en ' + ontbreken)

getal = int(input(''))
boodschap = 'l is geen perfect getal'
som = 1
delers = '1 '

for i in range (2, getal):
    if getal%1 == 0:
        som += 1
        i = '[]' .format(i)
        delers = str(delers) +str(1) + ''
if som == getal and getal != 1:
    boodschap = '...'
if som != getal and getal != 1:
    boodschap = '...'
print(boodschap)