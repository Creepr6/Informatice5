#invoer
r = int(input('donneer getal groter dan 0 en kleiner dan 100: '))
som_veelvoud = 0
#overloop alle veelvouden van r
for i in range(r, 101, r):
    som_veelvoud += i

print(som_veelvoud)

