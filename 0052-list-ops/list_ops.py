def append(list1, list2):
    return list1 + list2


def concat(lists):
    return [num for nested_lst in lists for num in nested_lst]


def filter(function, list):
    return [num for num in list if function(num)]


def length(list):
    return sum(1 for x in list)


def map(function, list):
    return [function(item) for item in list]


def foldl(function, list, initial):
    for el in list:
        initial = function(initial, el)
    return initial


def foldr(function, list, initial):
    for item in list[::-1]:
        initial = function(initial, item)
    return initial


def reverse(list):
    return list[::-1]


if __name__ == "__main__":
    print(append([], []), [])

    print(append([], [1, 2, 3, 4]), [1, 2, 3, 4])

    print(append([1, 2, 3, 4], []), [1, 2, 3, 4])

    print(append([1, 2], [2, 3, 4, 5]), [1, 2, 2, 3, 4, 5])

    print(concat([]), [])

    print(concat([[1, 2], [3], [], [4, 5, 6]]), [1, 2, 3, 4, 5, 6])

    print(
        concat([[[1], [2]], [[3]], [[]], [[4, 5, 6]]]),
        [[1], [2], [3], [], [4, 5, 6]],
    )

    print(filter(lambda x: x % 2 == 1, []), [])

    print(filter(lambda x: x % 2 == 1, [1, 2, 3, 5]), [1, 3, 5])

    print(length([]), 0)

    print(length([1, 2, 3, 4]), 4)

    print(map(lambda x: x + 1, []), [])

    print(map(lambda x: x + 1, [1, 3, 5, 7]), [2, 4, 6, 8])

    print(foldl(lambda acc, el: el * acc, [], 2), 2)

    print(foldl(lambda acc, el: el + acc, [1, 2, 3, 4], 5), 15)

    print(foldl(lambda acc, el: el / acc, [1, 2, 3, 4], 24), 64)

    print(foldr(lambda acc, el: el * acc, [], 2), 2)

    print(foldr(lambda acc, el: el + acc, [1, 2, 3, 4], 5), 15)

    print(foldr(lambda acc, el: el / acc, [1, 2, 3, 4], 24), 9)

    print(reverse([]), [])

    print(reverse([1, 3, 5, 7]), [7, 5, 3, 1])

    print(reverse([[1, 2], [3], [], [4, 5, 6]]), [[4, 5, 6], [], [3], [1, 2]])

    # Additional tests for this track
    print(
        foldr(lambda acc, el: el + acc, ["e", "x", "e", "r", "c", "i", "s", "m"], "!"),
        "exercism!",
    )

    print(reverse(["xyz", 4.0, "cat", 1]), [1, "cat", 4.0, "xyz"])
