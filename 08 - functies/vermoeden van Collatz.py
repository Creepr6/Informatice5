def collatz(x):
     getal = 1
     while x != 1:
          if x % 2 == 0:
              x = (x / 2)
              getal += 1
          else :
              x = (3 * x) + 1
              getal += 1
     return getal


def volgend_collatz_getal(x):
    if x % 2 == 0:
        volgend = x // 2
    else:
        volgend = (3 * x) + 1
    return volgend


