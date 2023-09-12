def square_root(number):
    start = 1
    while start * start != number:
        start += 1
    return start


if __name__ == "__main__":
    print(square_root(1), 1)

    print(square_root(4), 2)

    print(square_root(25), 5)

    print(square_root(81), 9)

    print(square_root(196), 14)

    print(square_root(65025), 255)
