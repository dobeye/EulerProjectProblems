def PrimesUpToVal(maxVal):
    i = 3
    primeList = [2]
    while True:
        if primeList[-1] >= maxVal:
            primeList.remove(primeList[-1])
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

# This seems to be slow as balls, but since I don't have a better way of doing this I give up.
