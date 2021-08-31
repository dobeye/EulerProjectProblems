def MultipleSummer(maxVal):
    retList = []
    retSum = 0
    i = 1
    while i < maxVal:
        if i % 5 == 0:
            retList.append(i)
        elif i % 3 == 0:
            retList.append(i)
        i += 1
    for i in retList:
        retSum += i
    return retSum
