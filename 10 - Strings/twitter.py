tweet = input('donneer tweet: ')
antwoord = ''
for i in range(0, len(tweet)):
    if tweet[i] == '#':
        k = tweet.find(' ')
    antwoord += tweet[i + 1: k] + '\n'

print(antwoord)


