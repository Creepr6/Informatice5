def vergeten_woorden(tekst, verplicht):

    zin = set(tekst.split())

    aantal_verplicht = len(verplicht)

    aantal_vergeten = len(verplicht.difference(zin))

    st = set(zin)
    st.discard(' ')
    aantal_gebruikte =


    return aantal_verplicht, aantal_vergeten, aantal_gebruikte

print(vergeten_woorden('',{'python', 'world', 'hello', 'java'}))