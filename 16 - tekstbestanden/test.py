bestand = open('klas.txt')

#om bestand op het einde terug te sluiten: bestand.close()

lijn = bestand.readline()
stukvanlijn = bestand.readline(2)


while lijn != '':
    print(lijn)
    lijn = bestand.readline()

bestand.close()
#veel beter:
lijnen = []

with open('klas.txt') as bestand:
    lijnen = bestand.readlines()

for naam in lijnen:
    #omgekeerd printen
    print(naam[::-1])

print('er zitten ' + str(len(lijnen)) + ' personen in de klas')

nieuwe_leerlingen = ['Alice', 'Baptiste']
a is voor append, w is vo write
with open('klas.txt', 'a') as bestand:
    bestand.write('\n' + '\n'.join(nieuwe_leerlingen))

