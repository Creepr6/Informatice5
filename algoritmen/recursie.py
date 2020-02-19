def faculteit(n):
    if n == 1:
        return 1
    else:
        print('{} * faculteit({})'.format(n, n- 1))
        res = faculteit(n - 1)
        print('{} * {} = {}'.format(n, res, n *res))
        return n * res

def is_palindroom(woord):

    if len(woord) == 1 or len(woord) == 0:
        return True

    else:
        print('{} == {} and is_palindroom({})'.format(woord[0], woord[-1], woord[1:-1]))
        res = is_palindroom(woord[1:-1])
        print('{} and {}'.format(woord[0] == woord[-1], res))
        return woord[0] == woord[-1] and res

print(is_palindroom('het diner'))

