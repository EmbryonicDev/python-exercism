def is_paired(input_string):
    stack = []
    brackets = {"(": ")", "[": "]", "{": "}"}

    for char in input_string:
        if char in brackets.keys():
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False

    return not stack


if __name__ == "__main__":
    print(is_paired("[]"), True)

    print(is_paired(""), True)

    print(is_paired("[["), False)

    print(is_paired("}{"), False)

    print(is_paired("{]"), False)

    print(is_paired("{ }"), True)

    print(is_paired("{[])"), False)

    print(is_paired("{[]}"), True)

    print(is_paired("{}[]"), True)

    print(is_paired("([{}({}[])])"), True)

    print(is_paired("{[)][]}"), False)

    print(is_paired("([{])"), False)

    print(is_paired("[({]})"), False)

    print(is_paired("[({}])"), False)

    print(is_paired("{}["), False)

    print(is_paired("[]]"), False)

    print(is_paired(")()"), False)

    print(is_paired("{)()"), False)

    print(is_paired("(((185 + 223.85) * 15) - 543)/2"), True)

    print(
        is_paired(
            "\\left(\\begin{array}{cc} \\frac{1}{3} & x\\\\ \\mathrm{e}^{x} &... x^2 \\end{array}\\right)"
        ),
        True,
    )
