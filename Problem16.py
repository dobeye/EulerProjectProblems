def DigitSum2ExponentBad(exponent):
    ret = 0
    for i in str(2 ** exponent):
        ret += int(i)
    return ret

# I feel a deep hatred towards this solution, because it has nothing to do with neither programming nor mathematics.
