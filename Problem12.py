import Utils


def TriNumberByDivisor(divisorNum):
    a = 2
    while True:
        contender = 0
        for i in range(a):
            contender += i
        if Utils.NumFactors(contender) > divisorNum:
            return contender
        a += 1
