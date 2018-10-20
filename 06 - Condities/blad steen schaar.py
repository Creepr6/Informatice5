#input
a = input("vorm die speler 1 achter zijn rug verbergt: ")
b = input("vorm die speler 2 achter zijn rug verbergt: ")
#berekenen
if a == b:
    print("onbeslist")
if a == "steen":
    if b == "blad":
        print("speler 2 wint")
    if b == "schaar":
        print("speler 1 wint")
if a == "blad":
    if b == "steen":
        print("speler 1 wint")
    if b == "schaar":
        print("speler 2 wint")
if a == "schaar":
    if b == "blad":
        print("speler 1 wint")
    if b == "steen":
        print("speler 2 wint")
