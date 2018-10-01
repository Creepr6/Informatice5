a = int(input(' bedrag = '))
r1 = a // 100
r2 = (a - (r1 * 100)) // 50
r3 = (a - (r1 * 100) - (r2 * 50)) // 20
r4 = (a - (r1 * 100) - (r2 * 50) - (r3 * 20)) // 10
r5 = (a - (r1 * 100) - (r2 * 50) - (r3 * 20) - (r4 * 10)) // 5
r6 = (a - (r1 * 100) - (r2 * 50) - (r3 * 20) - (r4 * 10) - (r5 * 5)) // 2
r7 = (a - (r1 * 100) - (r2 * 50) - (r3 * 20) - (r4 * 10) - (r5 * 5) - (r6 * 2)) // 1
resultaat = int(r5 + r1 + r2 + r3 + r4 + r6 + r7)
antwoord = str(a) + ' cent kan je omwisselen in ' + str(resultaat) + ' muntstukken'
print(antwoord)

