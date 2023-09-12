"""
This exercise stub and the test suite contain several enumerated constants.
 
Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).
 
You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""
# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "SUBLIST"
SUPERLIST = "SUPERLIST"
EQUAL = "EQUAL"
UNEQUAL = "UNEQUAL"


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    if is_sublist(list_one, list_two):
        return SUBLIST
    if is_sublist(list_two, list_one):
        return SUPERLIST
    return UNEQUAL


def is_sublist(lst_a, lst_b):
    len_a = len(lst_a)
    len_b = len(lst_b)

    for i in range(len_b - len_a + 1):
        if lst_a == lst_b[i : i + len_a]:
            return True


if __name__ == "__main__":
    print("test:", 1)
    print(sublist([], []), EQUAL)

    print("test:", 2)
    print(sublist([], [1, 2, 3]), SUBLIST)

    print("test:", 3)
    print(sublist([1, 2, 3], []), SUPERLIST)

    print("test:", 4)
    print(sublist([1, 2, 3], [1, 2, 3]), EQUAL)

    print("test:", 5)
    print(sublist([1, 2, 3], [2, 3, 4]), UNEQUAL)

    print("test:", 6)
    print(sublist([1, 2, 5], [0, 1, 2, 3, 1, 2, 5, 6]), SUBLIST)

    print("test:", 7)
    print(sublist([1, 1, 2], [0, 1, 1, 1, 2, 1, 2]), SUBLIST)

    print("test:", 8)
    print(sublist([0, 1, 2], [0, 1, 2, 3, 4, 5]), SUBLIST)

    print("test:", 9)
    print(sublist([2, 3, 4], [0, 1, 2, 3, 4, 5]), SUBLIST)

    print("test:", 10)
    print(sublist([3, 4, 5], [0, 1, 2, 3, 4, 5]), SUBLIST)

    print("test:", 11)
    print(sublist([0, 1, 2, 3, 4, 5], [0, 1, 2]), SUPERLIST)

    print("test:", 12)
    print(sublist([0, 1, 2, 3, 4, 5], [2, 3]), SUPERLIST)

    print("test:", 13)
    print(sublist([0, 1, 2, 3, 4, 5], [3, 4, 5]), SUPERLIST)

    print("test:", 14)
    print(sublist([1, 3], [1, 2, 3]), UNEQUAL)

    print("test:", 15)
    print(sublist([1, 2, 3], [1, 3]), UNEQUAL)

    print("test:", 16)
    print(sublist([1, 2], [1, 22]), UNEQUAL)

    print("test:", 17)
    print(sublist([1, 2, 3], [3, 2, 1]), UNEQUAL)

    print("test:", 18)
    print(sublist([1, 0, 1], [10, 1]), UNEQUAL)

    # Additional tests for this track
    print("test:", 19)
    print(len(set([SUBLIST, SUPERLIST, EQUAL, UNEQUAL])), 4)

    print("test:", 20)
    print(sublist(["a c"], ["a", "c"]), UNEQUAL)

    print("test:", 21)
    print(
        sublist(
            list(range(1000)) * 1000 + list(range(1000, 1100)),
            list(range(900, 1050)),
        ),
        SUPERLIST,
    )

    print("test:", 22)
    print(sublist(list(range(3, 200, 3)), list(range(15, 200, 15))), UNEQUAL)
