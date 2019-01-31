#min en max bij woorden vergelijkt alfabetisch, ook tupple1 > tupple3 en zo

gewesten = ('vlaanderen', 'wallonie', 'brussel')

for gewest in gewesten:
    print(gewest.upper())

for i in range(len(gewesten)):
    print(gewesten[i].upper())

#gaat niet(tuple niet veranderbaar):
gewesten[0] = 'Flandern'
gewesten += 'zeeuws vlaanderen'

