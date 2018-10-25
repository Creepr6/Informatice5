#input
a = float(input("aantal ogen dobbelsteen 1 aanvaller: "))
b = float(input("aantal ogen dobbelsteen 2 aanvaller: "))
c = float(input("aantal ogen dobbelsteen 3 aanvaller: "))
d = float(input("aantal ogen dobbelsteen 1 verdediger: "))
e = float(input("aantal ogen dobbelsteen 2 verdediger: "))

#sorteren
f = max(a, b, c)
g = max(d, e)
h = a + b + c - f - min(a, b , c)
i = d + e - g

#winnar bepalen
if f > g and h > i:
    x = 0
    y = 2
    antwoord = "aanvaller verliest " + str(x) + " legers, verdediger verliest " + str(y) + " legers"
    print(antwoord)
if f <= g and h <= i:
    x = 2
    y = 0
    antwoord = "aanvaller verliest " + str(x) + " legers, verdediger verliest " + str(y) + " legers"
    print(antwoord)
if f <= g and h > i or f > g and h <= i:
    x = 1
    y = 1
    antwoord2 = "aanvaller verliest " + str(x) + " leger, verdediger verliest " + str(y) + " leger"
    print(antwoord2)

if laatste ding ist lastigst dus die adk else moetn doen e matsko
werk ook me mes = 'aanvaller verliest x leger, verdediger verliest y legers' en dan opt einde printn doen ipv zo elke
keer op aparte regel te doen zie schaal van saffir simpson, doe ook de tweede regel elif ipv else das beter je
ne sais pas wrm me die guy doe da ook