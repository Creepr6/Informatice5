x = float(input('windsnelheid van orkaan in km/h = '))
if x >= 250:
    cat = "categorie " + str(5)
if x >= 119 and x <= 153:
    cat = "categorie " + str(1)
if x >= 154 and x <= 177:
    cat = "categorie " + str(2)
if x >= 178 and x <= 209:
    cat = "categorie " + str(3)
if x >= 210 and x <= 249:
    cat = "categorie " + str(4)
if x < 119:
    cat = "geen orkaan"
print(cat)