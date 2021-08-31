def FibonacciUpTo(maxVal):
    fibonacciList = [1, 1]
    while fibonacciList[len(fibonacciList) - 1] <= maxVal:
        fibonacciList.append(fibonacciList[len(fibonacciList) - 1] + fibonacciList[len(fibonacciList) - 2])
    fibonacciList.remove(fibonacciList[len(fibonacciList) - 1])
    return fibonacciList


def SumEvensInList(intList):
    ret = 0
    for i in intList:
        if i % 2 == 0:
            ret += i
    return ret
