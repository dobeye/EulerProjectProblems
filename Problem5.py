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

# This is the dumbest and worst way possible to solve this problem, and makes absolutely no sense. I'm ok with that.
