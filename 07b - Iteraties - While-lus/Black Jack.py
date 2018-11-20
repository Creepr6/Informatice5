totaal_aantal_kaarten = 0
kaart = float(input('kaart met een waarde van 1 tot en met 11: '))

while kaart > 0 and kaart + totaal_aantal_kaarten < 21:
         totaal_aantal_kaarten += kaart
         kaart = float(input('kaart met een waarde van 1 tot en met 11: '))

if totaal_aantal_kaarten + kaart == 21:
    mess = 'Gewonnen!'
elif totaal_aantal_kaarten + kaart > 21:
    mess = 'Verbrand (' + str('{:.0f}'.format(totaal_aantal_kaarten + kaart)) + ')'
elif totaal_aantal_kaarten < 21:
    mess = 'Voorzichtig gespeeld (' + str('{:.0f}'.format(totaal_aantal_kaarten)) + ')'

print(mess)