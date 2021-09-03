def FibonacciUpTo(maxVal):
    fibonacciList = [1, 1]
    while fibonacciList[-1] <= maxVal:
        fibonacciList.append(fibonacciList[-1] + fibonacciList[-2])
    fibonacciList.remove(fibonacciList[-1])
    return fibonacciList


def SumEvensInList(intList):
    ret = 0
    for i in intList:
        if i % 2 == 0:
            ret += i
    return ret
