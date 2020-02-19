def is_priemgetal(getal):
    deler = 2
    while getal % deler != 0 and getal != 1:
        deler += 1
    return deler == getal

n = int(input('aantal priemgetallen: '))
getal = 1
i = 1
som = 0

while i < n + 1:
    if is_priemgetal(getal) is True:
        som += getal
        getal += 1
        i += 1
    else:
        getal += 1

print(som)
