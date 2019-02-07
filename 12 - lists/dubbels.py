def dubbels(lijst):

    nieuwe_lijst = []

    for i in range(0, len(lijst)):
        if lijst.count(lijst[i]) > 1 and lijst[i] not in nieuwe_lijst:
            nieuwe_lijst.append(lijst[i])

    return nieuwe_lijst

print(dubbels(['kaas', 'brokoli', 'kaas']))
