def FindDigitMultiple(largeNum, digitAmount):
    if len(str(largeNum)) < digitAmount:
        return "That not something you can input into this function, I don't think you know how this works."
    ret = 0
    for i in range(len(str(largeNum)) - digitAmount):
        contender = 1
        for j in range(digitAmount):
            contender *= int(str(largeNum)[i + j])
        if contender > ret:
            ret = contender
    return ret
