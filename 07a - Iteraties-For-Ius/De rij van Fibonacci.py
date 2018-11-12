n = int(input('een getal n∈N0: '))

if n == 1 or n == 2:
    print(str(1))
elif n == 0:
    print(str(0))
else:
    def fib(n):
        a = 1
        b = 1
        for _ in range (n-1):
            a,b = b, a+b
        return a
    print(fib(n))

