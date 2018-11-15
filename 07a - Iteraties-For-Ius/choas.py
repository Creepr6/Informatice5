#invoer
Drie regels die achtereenvolgens de volgende informatie bevatten
d = int(input('de initiële populatiedichtheid: '))
r = int(input('de waarde van de vruchtbaarheidsparameter: '))
s = int(input('het aantal tijdsstappen waarover we de populatiedichtheid willen simuleren (inclusief het tijdstip t0): '))
t = 0
#berekenen
for i in range(-1, s):
    t += i
    d = (r * d * (1 - d))




