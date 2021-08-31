def FindLargestFactor(startingInt):
    i = 2
    while i < startingInt:
        if startingInt % i == 0 and FindLargestFactor(startingInt / i) == startingInt / i:
            return startingInt / i
        i += 1
    return startingInt