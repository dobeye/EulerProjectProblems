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


def CheckPalindrome(contender):
    conLength = len(str(contender))
    k = 1
    while k <= conLength / 2:
        if int(contender / (10 ** (conLength - k)) - int(contender / (10 ** (conLength - k + 1))) * 10) != int(
                contender / (10 ** (k - 1)) - int(contender / (10 ** k)) * 10):
            return False
        k += 1
    return True
