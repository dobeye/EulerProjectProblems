import math


def SumList(retList):
    retSum = 0
    for i in retList:
        retSum += i
    return retSum


def Ex(exponent):
    return 10 ** exponent


def NewtonsBinomial(a, b):
    return math.factorial(a) / (math.factorial(b) * math.factorial(a - b))


def NumDivisors(inputNum):
    ret = 1
    for i in range(1, int(inputNum / 2) + 1):
        if inputNum % i == 0:
            ret += 1
    return ret

# This method of finding factors sucks absolute balls, and I cannot express my happiness at having found a much better method


def ListPrimeFactors(inputNum):
    primeList = []
    for i in range(2, int(inputNum ** 0.5) + 1):
        if inputNum % i == 0:
            primeList.append(int(i))
            primeList.extend(ListPrimeFactors(int(inputNum / i)))
            break
    if len(primeList) == 0:
        primeList.append(inputNum)
    ret = []
    for i in primeList:
        inserted = False
        for j in ret:
            if i == j[0]:
                j[1] += 1
                inserted = True
                break

        if not inserted:
            ret.append([i, 1])

    return ret


def PrimeListtoFactors(primeList):
    if primeList == [[1, 1]]:
        return 1
    ret = 1
    for i in primeList:
        ret *= (i[1] + 1)
    return ret


def NumFactors(baseVal):
    return PrimeListtoFactors(ListPrimeFactors(baseVal))


def ListSum(inputList):
    ret = 0
    for i in inputList:
        ret += i
    return ret