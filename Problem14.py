def CollatzLongestInRangeBad(maxVal):
    ret = 0
    retSteps = 0
    for i in range(1, maxVal, 2):
        contender = i
        steps = 0
        while contender > 1:
            if contender % 2 == 0:
                contender /= 2
            else:
                contender = 3 * contender + 1
            steps += 1
        if steps > retSteps:
            retSteps = steps
            ret = i
    if ret < maxVal / 2:
        ret *= 2
        retSteps += 1

    return [ret, retSteps]

# it would be far smarter to remember the results of previous numbers and then if a previous number shows up
# you can just add their collatz number to the current count. Sadly I am far too lazy to do that.


def CollatzFunction(contender, answerKey):
    if len(answerKey) >= contender:
        return answerKey[contender - 1][1]
    if contender == 1:
        return 0
    steps = 0
    if contender % 2 == 0:
        contender /= 2
    else:
        contender = 3 * contender + 1
    steps += CollatzFunction(int(contender), answerKey) + 1

    return steps


def CollatzLongestInRange(maxVal):
    ret = 0
    retSteps = 0
    answerKey = []
    for i in range(1, maxVal):
        steps = CollatzFunction(i, answerKey)
        answerKey.append([i, steps])
        if steps > retSteps:
            ret = i
            retSteps = steps

    return [ret, retSteps]
