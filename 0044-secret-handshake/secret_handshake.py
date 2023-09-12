def commands(binary_str):
    actions = [
        "jump",
        "close your eyes",
        "double blink",
        "wink",
    ]

    # Remove binary_str[0] to get action digits
    binary_str_copy = binary_str[1:]

    # Get actions list
    handshake_actions = [
        actions[i] for i in range(3, -1, -1) if binary_str_copy[i] == "1"
    ]

    # Reverse if required
    if binary_str[0] == "1":
        return handshake_actions[::-1]

    return handshake_actions


"""
00001 = "wink"
00010 = "double blink"
00100 = "close your eyes"
01000 = "jump"
10000 = Reverse the order of the operations in the secret handshake.
"""


if __name__ == "__main__":
    print(commands("00001"), ["wink"])

    print(commands("00010"), ["double blink"])

    print(commands("00100"), ["close your eyes"])

    print(commands("01000"), ["jump"])

    print(commands("00011"), ["wink", "double blink"])

    print(commands("10011"), ["double blink", "wink"])

    print(commands("11000"), ["jump"])

    print(commands("10000"), [])

    print(commands("01111"), ["wink", "double blink", "close your eyes", "jump"])

    print(commands("11111"), ["jump", "close your eyes", "double blink", "wink"])

    print(commands("00000"), [])
