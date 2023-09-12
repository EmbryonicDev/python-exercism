def flatten(iterable):
    """Flattens a nested list and returns a single flattened list with all values except nil/null."""
    flattened_list = []
    for item in iterable:
        if item is None:
            continue
        if isinstance(item, list):
            flattened_list.extend(flatten(item))
        else:
            flattened_list.append(item)
    return flattened_list


if __name__ == "__main__":
    inputs = []
    expected = []
    print(flatten(inputs), expected)

    inputs = [0, 1, 2]
    expected = [0, 1, 2]
    print(flatten(inputs), expected)

    inputs = [[[]]]
    expected = []
    print(flatten(inputs), expected)

    inputs = [1, [2, 3, 4, 5, 6, 7], 8]
    expected = [1, 2, 3, 4, 5, 6, 7, 8]
    print(flatten(inputs), expected)

    inputs = [0, 2, [[2, 3], 8, 100, 4, [[[50]]]], -2]
    expected = [0, 2, 2, 3, 8, 100, 4, 50, -2]
    print(flatten(inputs), expected)

    inputs = [1, [2, [[3]], [4, [[5]]], 6, 7], 8]
    expected = [1, 2, 3, 4, 5, 6, 7, 8]
    print(flatten(inputs), expected)

    inputs = [1, 2, None]
    expected = [1, 2]
    print(flatten(inputs), expected)

    inputs = [None, None, 3]
    expected = [3]
    print(flatten(inputs), expected)

    inputs = [1, None, None, 4]
    expected = [1, 4]
    print(flatten(inputs), expected)

    inputs = [0, 2, [[2, 3], 8, [[100]], None, [[None]]], -2]
    expected = [0, 2, 2, 3, 8, 100, -2]
    print(flatten(inputs), expected)

    inputs = [None, [[[None]]], None, None, [[None, None], None], None]
    expected = []
    print(flatten(inputs), expected)
