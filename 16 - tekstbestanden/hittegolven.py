def splits(bestand):

    with open('temperaturen.txt') as bestand:
        lijnen = bestand.readlines()



aantal25plus = 0
aantal30plus = 0
i = 0
datums = []
hittegolven = 0

for i in range(len(lijnen)):

    if lijnen[i] >= 30:
        aantal30plus += 1
        aantal25plus += 1

    elif lijnen[i] >= 25:
        aantal25plus += 1

    else:

        if aantal25plus >= 5 and aantal30plus >= 3:

            datums.append(i - aantal25plus, i - 1)
            hittegolven += 1

        aantal25plus = 0
        aantal25plus = 0
        i += 1



print(datums)

