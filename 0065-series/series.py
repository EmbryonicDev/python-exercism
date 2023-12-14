def slices(series, length):
    if length == 0:
        raise ValueError("slice length cannot be zero")

    if length < 0:
        raise ValueError("slice length cannot be negative")

    if not series:
        raise ValueError("series cannot be empty")

    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")

    answer = []
    while len(series) >= length:
        answer.append(series[:length])
        series = series[1:]
    return answer


if __name__ == "__main__":
    print(slices("1", 1), ["1"])

    print(slices("12", 1), ["1", "2"])

    print(slices("35", 2), ["35"])

    print(slices("9142", 2), ["91", "14", "42"])

    print(slices("777777", 3), ["777", "777", "777", "777"])

    print(
        slices("918493904243", 5),
        ["91849", "18493", "84939", "49390", "93904", "39042", "90424", "04243"],
    )
