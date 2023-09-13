def rows(letter):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    outer_spaces = alpha.index(letter)
    alpha = alpha[: outer_spaces + 1]
    inner_spaces = 1
    line_a = f"{' ' * outer_spaces}A{' ' * outer_spaces}"
    diamond_shape_lst = []

    # append expanding diamond
    for char in alpha:
        if char == "A":
            diamond_shape_lst.append(line_a)
            outer_spaces -= 1
        else:
            diamond_shape_lst.append(
                f"{' ' * outer_spaces}{char}{' ' * inner_spaces}{char}{' ' * outer_spaces}"
            )
            outer_spaces -= 1
            inner_spaces += 2

    # append contracting diamond
    # reverse diamond_shape_lst except for last item
    for row in diamond_shape_lst[-2::-1]:
        diamond_shape_lst.append(row)

    return diamond_shape_lst


if __name__ == "__main__":
    print(rows("G"))
