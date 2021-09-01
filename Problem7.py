def PrimesUpTo(listLen):
    i = 3
    primeList = [2]
    while True:
        if len(primeList) == listLen:
            return primeList
        primeList.append(i)
        for val in primeList:
            if val <= int(i ** 0.5) + 1:
                if i % val == 0:
                    primeList.remove(i)
                    break
            else:
                break
        i += 1
