from time import time
from random import randint
import matplotlib.pyplot as plt

def genereer_rij(aantal):
    rij = []
    for i in range(aantal):
        rij.append(randint(0, aantal))
    return rij

def insertion_sort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i +1] = a[i]
            i = i - 1
        a[i + 1] = key

    return a


def bubble_sort(rij):
    A = rij
    for i in range(0,len(A) - 1):
        for j in range(len(A) - 1, i, -1):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]

    return A

i, n, t_insertion, t_python, t_bubble = 10, [], [], [], []
while i < 2000:
    rij_1 = genereer_rij(i)
    rij_2 = rij_1.copy()
    rij_3 = rij_1.copy()

    #insertion sort testen
    start = time()
    insertion_sort(rij_1)
    stop = time()
    t_insertion.append(stop - start)

    #sorteerfunctie python testen
    start = time()
    rij_2.sort()
    stop = time()
    t_python.append(stop - start)

    #bubble sort testen
    start = time()
    bubble_sort(rij_3)
    stop = time()
    t_bubble.append(stop - start)

    n.append(i)
    i += 50

plt.plot(n, t_insertion, '-bd')
plt.plot(n, t_python, '-r')
plt.plot(n, t_bubble, '-gs')
plt.xlabel('N')
plt.ylabel('t')
plt.title('Tijdsmeting')
plt.gca().legend(('ingertion sort', 'python sort', 'bubble sort'))
plt.gcf().canvas.set_window_title('Warre Veys')
plt.show()