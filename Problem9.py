def PythagTripBySum(sum):
    for a in range(1, sum):
        for b in range(1, sum - a):
            c = sum - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return a * b * c


def PythagTripBySum2(sum):
    for a in range(1, int(sum ** 0.5) + 1):
        for b in range(1, a):
            if 2 * a ** 2 + 2 * a * b == sum:
                return (a ** 4 - b ** 4) * 2 * a * b