def WrittenLengthSum(maxVal):
    ret = 0
    for i in range(1, maxVal + 1):
        ret += WrittenNumberLength(i)
    return ret


def WrittenNumberLength(writeNum):
    if writeNum == 0:
        return 0
    if writeNum == 1:
        return 3
    if writeNum == 2:
        return 3
    if writeNum == 3:
        return 5
    if writeNum == 4:
        return 4
    if writeNum == 5:
        return 4
    if writeNum == 6:
        return 3
    if writeNum == 7:
        return 5
    if writeNum == 8:
        return 5
    if writeNum == 9:
        return 4
    if writeNum == 10:
        return 3
    if writeNum == 11:
        return 6
    if writeNum == 12:
        return 6
    if writeNum == 13:
        return 8
    if writeNum == 14:
        return 8
    if writeNum == 15:
        return 7
    if writeNum == 16:
        return 7
    if writeNum == 17:
        return 9
    if writeNum == 18:
        return 8
    if writeNum == 19:
        return 8
    if writeNum == 20:
        return 6
    if writeNum == 30:
        return 6
    if writeNum == 40:
        return 5
    if writeNum == 50:
        return 5
    if writeNum == 60:
        return 5
    if writeNum == 70:
        return 7
    if writeNum == 80:
        return 6
    if writeNum == 90:
        return 6
    if writeNum < 100:
        return WrittenNumberLength(int(str(writeNum)[0]) * 10) + WrittenNumberLength(int(str(writeNum)[1]))
    if writeNum < 1000:
        if int(str(writeNum)[1:]) != 0:
            return WrittenNumberLength(int(str(writeNum)[0])) + 10 + WrittenNumberLength(int(str(writeNum)[1:]))
        return WrittenNumberLength(int(str(writeNum)[0])) + 7
    if writeNum < 10000:
        return WrittenNumberLength(int(str(writeNum)[0])) + 8 + WrittenNumberLength(int(str(writeNum)[1:]))