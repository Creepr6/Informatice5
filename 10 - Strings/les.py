def is_palindroom(woord):

    i = 0

    while woord[i] == woord[-i - 1] and i < len(woord) // 2:
          i += 1

    return i == (len(woord) // 2)

tweet = input('wat is de tweet?: ')

i_hashtag = tweet.find('#')
#als ie geen vind dan zegtie -1 dus
while i_hashtag != -1:
    # tweet afknippen net na #teken
    tweet = tweet[i_hashtag + 1:]
    i_spatie = tweet.find(' ')

    #hastag uitknippen en printen
    print(tweet[:i_spatie])

    #terug op zoek naar #
    i_hastag = tweet.find('#')

def positie_laagste_ascii(tekst):

    p_laagste = 0
    ord_laagste = ord(tekst[0])

    for i in range(1, len(tekst)):
        if(ord[tekst[i]] < ord_laagste):
            p_laagste = i
            ord_laagste = ord(tekst[i])
    return p_laagste

print(positie_laagste_ascii('vincent'))

def sorteer(tekst):
    s_tekst = ''

    while len(tekst) > 0:
        i = positie_laagste_ascii(tekst)
        s_tekst += tekst[i]
        tekst = tekst [:i] + tekst[i + 1:]

    return s_tekst

def is_alfabetisch(tekst):
    return tekst == sorteer(tekst)