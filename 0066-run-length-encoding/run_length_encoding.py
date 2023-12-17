def encode_str(char_dict, encoded_str):
    for key, value in char_dict.items():
        encoded_str = f'{encoded_str}{value}{key}' if value > 1 \
            else encoded_str + key
    return encoded_str


def decode(string):
    num_str = 1
    decoded_str = ''

    for char in string:
        if char in '1234567890':
            num_str = char if num_str == 1 else num_str + char
            continue
        decoded_str += char * int(num_str)
        num_str = 1

    return decoded_str


def encode(string):
    my_dict = {}
    encoded_str = ''

    for char in string:
        if char not in my_dict:
            encoded_str = encode_str(my_dict, encoded_str)
            my_dict = {char: 1}
        else:
            my_dict[char] += 1

    return encode_str(my_dict, encoded_str)


if __name__ == "__main__":
    print(encode(""), "")

    print(encode("XYZ"), "XYZ")

    print(encode("AABBBCCCC"), "2A3B4C")

    print(
            encode("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"),
            "12WB12W3B24WB",
        )

    print(encode("  hsqq qww  "), "2 hs2q q2w2 ")

    print(encode("aabbbcccc"), "2a3b4c")
    #
    print(decode(""), "")

    print(decode("XYZ"), "XYZ")

    print(decode("2A3B4C"), "AABBBCCCC")

    print(
            decode("12WB12W3B24WB"),
            "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB",
        )

    print(decode("2 hs2q q2w2 "), "  hsqq qww  ")

    print(decode("2a3b4c"), "aabbbcccc")

    print(decode(encode("zzz ZZ  zZ")), "zzz ZZ  zZ")