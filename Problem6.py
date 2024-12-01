def SumSquares(maxVal):
    ret = 0
    for i in range(1, maxVal + 1):
        ret += i ** 2
        # benshloush
    return ret


def SumSquareDif(maxVal):
    return int((maxVal * (maxVal + 1) / 2) ** 2 - SumSquares(maxVal))
