def FindPalindromeProduct(digitAmount):
    ret = 0
    i = 10 ** digitAmount - 1
    while i >= 1:
        if ret >= i ** 2:
            return ret
        j = i
        while j >= 1:
            contender = i * j
            if contender > ret and CheckPalindrome(contender):
                ret = contender
                break
            j -= 1
        i -= 1
    return ret


def Ex(exponent):
    return 10 ** exponent


def CheckPalindrome(contender):
    k = 1
    while k <= len(str(contender)) / 2:
        nK = len(str(contender)) - k
        if int(contender / Ex(nK) - int(contender / Ex(nK + 1)) * 10) != int(
                contender / Ex(k - 1) - int(contender / Ex(k)) * 10):
            return False
        k += 1
    return True
