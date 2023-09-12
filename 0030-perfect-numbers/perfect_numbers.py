def aliquot_sum(number):
    factor_sum = 1
    for factor in range(2, number):
        if number % factor == 0:
            factor_sum += factor
    return factor_sum


def classify(number):
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    rendered_num = aliquot_sum(number)

    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    if number > rendered_num or number == 1:
        return "deficient"
    if number == rendered_num:
        return "perfect"
    return "abundant"


if __name__ == "__main__":
    print(classify(1), "perfect")

    print(classify(28), "perfect")

    print(classify(33550336), "perfect")

    print(classify(12), "abundant")

    print(classify(30), "abundant")

    print(classify(33550335), "abundant")

    print(classify(2), "deficient")

    print(classify(4), "deficient")

    print(classify(32), "deficient")

    print(classify(33550337), "deficient")

    print(classify(1), "deficient")

    # print(classify(0), "Value Error!")

    # print(classify(-1), "Value Error!")
