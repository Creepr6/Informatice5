def afstand(x, y):
    from math import sqrt
    afstand = sqrt(((x[0] - y[0])**2) + ((x[1] - y[1])**2))
    return afstand

def binnen_of_buiten(m, c, p):
    straal = afstand(m, c)
    afstand_punt = afstand(m, p)
    if straal == afstand_punt:
        plaats = 'op'
    elif straal > afstand_punt:
        plaats = 'binnen'
    else:
        plaats = 'buiten'
    return plaats , round(afstand_punt, 4)

print(binnen_of_buiten((0, 0),(1, 1),(-1, -1)))