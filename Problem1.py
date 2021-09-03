def MultipleSummer(maxVal):
    retSum = 0
    i = 1
    while i < maxVal:
        if i % 5 == 0:
            retSum += i
        elif i % 3 == 0:
            retSum += i
        i += 1
    return retSum
