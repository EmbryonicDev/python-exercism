def resistor_label(colors):
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

    tolerance_guide = {
        "grey": "0.05%",
        "violet": "0.1%",
        "blue": "0.25%",
        "green": "0.5%",
        "brown": "1%",
        "red": "2%",
        "gold": "5%",
        "silver": "10%",
    }

    if len(colors) < 4:
        return "0 ohms"

    tolerance = f"±{tolerance_guide[colors.pop()]}"
    total_zeros = int(clr_check[colors.pop()])
    digits = ""

    # convert colors to numbers as a string
    for color in colors:
        digits += str(clr_check[color])

    # add zeros based on 2nd last color then convert to int
    digits += "0" * total_zeros
    digits = int(digits)

    def get_f_string(nums, rating):
        # remove float if number is whole
        nums = int(nums) if nums % 1 == 0 else nums

        return f"{nums} {rating} {tolerance}"

    # Define and apply ratings
    ratings = {1: "kilo", 2: "mega", 3: "giga"}

    if digits > 1000_000_000:
        return get_f_string(digits / 1000_000_000, f"{ratings[3]}ohms")

    if digits > 1000_000:
        return get_f_string(digits / 1000_000, f"{ratings[2]}ohms")

    if digits > 1000:
        return get_f_string(digits / 1000, f"{ratings[1]}ohms")

    return f"{(digits)} ohms {tolerance}"


if __name__ == "__main__":
    print(resistor_label(["orange", "orange", "black", "red"]), "33 ohms ±2%")

    print(resistor_label(["blue", "grey", "brown", "violet"]), "680 ohms ±0.1%")

    print(resistor_label(["red", "black", "red", "green"]), "2 kiloohms ±0.5%")

    print(resistor_label(["green", "brown", "orange", "grey"]), "51 kiloohms ±0.05%")

    print(resistor_label(["black"]), "0 ohms")

    print(
        resistor_label(["orange", "orange", "yellow", "black", "brown"]), "334 ohms ±1%"
    )

    print(
        resistor_label(["red", "green", "yellow", "yellow", "brown"]),
        "2.54 megaohms ±1%",
    )

    print(
        resistor_label(["blue", "grey", "white", "brown", "brown"]), "6.89 kiloohms ±1%"
    )

    print(resistor_label(["violet", "orange", "red", "grey"]), "7.3 kiloohms ±0.05%")

    print(
        resistor_label(["brown", "red", "orange", "green", "blue"]),
        "12.3 megaohms ±0.25%",
    )
