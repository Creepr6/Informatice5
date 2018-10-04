#twee willekeurige getallen vragen
a = float(input('getal 1 = '))
b = float(input('getal 2 = '))

#linkerlid en rechterlid berekenen
ll = abs(abs(a) - abs(b))
rr = abs(a - b)

#antwoord
antwoord = '{:.4f} ≤ {:.4f}' .format(ll,rr)

#oplossen
print(antwoord)