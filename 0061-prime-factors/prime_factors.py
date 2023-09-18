def factors(value):
    factor = 2
    prime_factors = []
    while factor <= value:
        if value == 1:
            break
        if value % factor == 0:
            prime_factors.append(factor)
            value /= factor
        else:
            factor += 1

    return prime_factors


if __name__ == "__main__":
    print(factors(1), [])

    print(factors(2), [2])

    print(factors(3), [3])

    print(factors(9), [3, 3])

    print(factors(4), [2, 2])

    print(factors(8), [2, 2, 2])

    print(factors(27), [3, 3, 3])

    print(factors(625), [5, 5, 5, 5])

    print(factors(6), [2, 3])

    print(factors(12), [2, 2, 3])

    print(factors(901255), [5, 17, 23, 461])

    print(factors(93819012551), [11, 9539, 894119])
