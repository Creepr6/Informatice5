temp = input('Temperaturen: ')
aantal_stijgingen = 0

for i in range(0, len(temp) - 1):
    if temp[i] < temp[i + 1]:
        aantal_stijgingen += 1

antwoord = "Sequentie '" + str(temp) + "' telt " + str(aantal_stijgingen) + " stijgingen."

print(antwoord)
