a = float(input(' bedrag = '))
resultaat = str(a) + ' cent kan je omwisselen in ' + str(b) + ' muntstukken'
b = (a//100) + ((a%100)//50) + (((a%100)%50)//20) + ((((a%100)%50)%20)//10) + (((((a%100)%50)%20)%10)//5) + ((((((a%100)%50)%20)%10)%5)//2) + (((((((a%100)%50)%20)%10)%5)%2)//1)
print(resultaat)
