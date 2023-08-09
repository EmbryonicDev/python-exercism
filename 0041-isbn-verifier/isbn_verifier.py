def is_valid(isbn):
    isbn = isbn.replace("-", "")
    if len(isbn) != 10 or not isbn[:-1].isdigit():
        return False

    check_digit = isbn[-1]
    if check_digit != "X" and not check_digit.isdigit():
        return False

    digits = [int(char) if char.isdigit() else 10 for char in isbn]
    total = sum(d * (10 - i) for i, d in enumerate(digits))

    return total % 11 == 0


"""
Formula to determine answer (d = digit)
(d₁ * 10 + d₂ * 9 + d₃ * 8 + d₄ * 7 + d₅ * 6 + d₆ * 5 + d₇ * 4 + d₈ * 3 + d₉ * 2 + d₁₀ * 1) mod 11 == 0
"""


if __name__ == "__main__":
    print(is_valid("3-598-21508-8"), True)

    print(is_valid("3-598-21508-9"), False)

    print(is_valid("3-598-21507-X"), True)

    print(is_valid("3-598-21507-A"), False)

    print(is_valid("3-598-P1581-X"), False)

    print(is_valid("3598215088"), True)

    print(is_valid("359821507X"), True)

    print(is_valid("359821507"), False)

    print(is_valid("3598215078X"), False)

    print(is_valid("3-598-21507"), False)

    print(is_valid("3-598-21515-X"), False)

    print(is_valid("3132P34035"), False)
    print(is_valid("134456729"), False)
    print(is_valid("98245726788"), False)
    print(is_valid("4-598-21507-B"), False)
    print(is_valid("00"), False)
    print(is_valid(""), False)
    print(is_valid("3-598-2X507-9"), False)

    print(is_valid("3598P215088"), False)
