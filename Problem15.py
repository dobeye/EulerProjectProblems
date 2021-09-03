import math

def LatticePathsBad(x, y):
    ret = 0
    if y == 1:
        return x + 1
    if x == 0:
        return 1
    for i in range(x + 1):
        ret += LatticePathsBad(i, y - 1)
    return ret


def LatticePaths(x, y):
    return int(math.factorial(x + y) / (math.factorial(x) * math.factorial(y)))