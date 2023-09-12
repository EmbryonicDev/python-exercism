def label(colors):
    clr_check = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9,
    }
    total_zeros = int(clr_check[colors.pop()])
    digits = ""

    # convert colors to numbers as a string
    for color in colors:
        digits += str(clr_check[color])

    # Round off to nearest 10
    if int(digits) > 99:
        digits = str(round(int(digits) / 10) * 10)

    # add zeros based on last color then convert to int
    digits += "0" * total_zeros
    digits = int(digits)

    # Define and apply ratings
    ratings = {1: "kilo", 2: "mega", 3: "giga"}
    if digits > 1000_000_000:
        return f"{int(digits/1000_000_000)} {ratings[3]}ohms"
    if digits > 1000_000:
        return f"{int(digits/1000_000)} {ratings[2]}ohms"
    if digits > 1000:
        return f"{int(digits/1000)} {ratings[1]}ohms"

    return f"{int(digits)} ohms"


if __name__ == "__main__":
    print(label(["orange", "orange", "black"]), "33 ohms")

    print(label(["blue", "grey", "brown"]), "680 ohms")

    print(label(["red", "black", "red"]), "2 kiloohms")

    print(label(["green", "brown", "orange"]), "51 kiloohms")

    print(label(["yellow", "violet", "yellow"]), "470 kiloohms")

    print(label(["blue", "violet", "blue"]), "67 megaohms")

    print(label(["black", "black", "black"]), "0 ohms")

    print(label(["white", "white", "white"]), "99 gigaohms")

    print(label(["black", "grey", "black"]), "8 ohms")

    print(label(["blue", "green", "yellow", "orange"]), "650 kiloohms")
