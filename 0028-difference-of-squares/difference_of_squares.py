def square_of_sum(number):
    start = 1
    answer = 0
    if number < 2:
        return 1
    while start <= number:
        answer += start
        start += 1
    return answer**2


def sum_of_squares(number):
    start = 1
    answer = 0
    while start <= number:
        answer += start**2
        start += 1
    return answer


def difference_of_squares(number):
    if number < 2:
        return 0
    x = square_of_sum(number)
    y = sum_of_squares(number)

    return x - y


if __name__ == "__main__":
    print(square_of_sum(1), 1)

    print(square_of_sum(5), 225)

    print(square_of_sum(100), 25502500)

    print(sum_of_squares(1), 1)

    print(sum_of_squares(5), 55)

    print(sum_of_squares(100), 338350)

    print(difference_of_squares(1), 0)

    print(difference_of_squares(5), 170)

    print(difference_of_squares(100), 25164150)
