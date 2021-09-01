def DivisibilityCheck(checkedNum):
    for i in range(1, 21):
        if checkedNum % i != 0:
            return False
    return True


def FindNumber():
    i = 1
    while True:
        if DivisibilityCheck(i):
            return i
        i += 1


# This is the 2nd dumbest and 2nd worst way possible to solve this problem, and makes absolutely no sense. I'm ok
# with that.


def FindGCD(a, b):
    if a % b == 0:
        return b
    if a % b == 1:
        return 1
    return FindGCD(b, a % b)


def DivisibilityCheck2(rangeMax):
    ret = 1
    for i in range(1, rangeMax + 1):
        ret *= i / FindGCD(ret, i)
    return ret


# So this is a slightly better way to solve this, no idea if it's optimal but it's certainly better.
