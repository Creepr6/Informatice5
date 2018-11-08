

for i in range(350):
    print('beep, beep, papier komt uit printer, beep, stop')

for letter in 'lus':
    print(letter + '?')

fruit = input('Lievelingsfruit? ')
m = ' m'
for letter in fruit:
 print(letter + m)
 m += 'm'

for i in range(10):
    print(i)

for i in range(10, 0, -1):
    print(i)

print('raket vertrekt')

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
