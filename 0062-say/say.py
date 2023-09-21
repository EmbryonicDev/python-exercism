ones = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}


teens = {
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}


tens = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety",
}


bases = {2: "thousand", 3: "million", 4: "billion"}


def create_grouped_lst(num):
    str_num = str(num)
    paired_lst = []

    while str_num:
        if len(str_num) <= 3:
            paired_lst.insert(0, int(str_num))
            str_num = ""
        else:
            paired_lst.insert(0, int(str_num[-3:]))
            str_num = str_num[:-3]

    return paired_lst


def convert_below_100(number):
    num_str = str(number)
    if number >= 20:
        tens_text = tens[int(num_str[0])]
        ones_text = ones[int(num_str[1])]
        if number % 10 == 0:
            return tens_text
        return f"{tens_text}-{ones_text}"
    if number >= 10:
        return teens[number]
    # if number < 10
    return ones[number]


def say(number):
    if number > 999_999_999_999 or number < 0:
        raise ValueError("input out of range")

    if number == 0:
        return "zero"

    # Break number up into chunks of thousands
    chunks = create_grouped_lst(number)

    # create list in format of [1, 'billion', 234, 'million', 567, 'thousand', 890] for 1234567890
    chunk_len = len(chunks)
    based_lst = []
    for chunk in chunks:
        if chunk == 0:
            continue
        if chunk_len > 1:
            based_lst += [chunk, bases[chunk_len]]
        else:
            based_lst.append(chunk)
        chunk_len -= 1

    # convert the integers in based_list to converted format
    final_converted_list = []
    for item in based_lst:
        new_item = ""
        str_item = str(item)

        # only modify items in list that isdigit()
        if str_item.isdigit():
            if len(str_item) == 3:
                # convert the total hundreds to text, add to final_converted_list, then slice the remaining 2 stringed integer for further processing
                new_item += convert_below_100(int(str_item[0])) + " hundred "
                str_item = str_item[1:]
            # if the stringed number is < 100, convert to text and add to new_item
            # or do the same for the sliced stringed integer from previous step
            # skip if number is zero
            if len(str_item) < 3 and int(str_item) > 0:
                new_item += convert_below_100(int(str_item))
            final_converted_list.append(new_item)
        # append to list if not stringed integer (from bases dict)
        else:
            final_converted_list.append(item)

    # convert final_converted_list to text and remove trailing " "
    return " ".join(final_converted_list).strip()


if __name__ == "__main__":
    print(say(0), "zero")

    print(say(1), "one")

    print(say(14), "fourteen")

    print(say(20), "twenty")

    print(say(22), "twenty-two")

    print(say(30), "thirty")

    print(say(99), "ninety-nine")

    print(say(100), "one hundred")

    print(say(123), "one hundred twenty-three")

    print(say(200), "two hundred")

    print(say(123_456_789_04), "nine hundred ninety-nine")

    print(say(1000), "one thousand")

    print(say(1234), "one thousand two hundred thirty-four")

    print(say(1000000), "one million")

    print(say(1002345), "one million two thousand three hundred forty-five")

    print(say(1000000000), "one billion")

    print(
        say(987654321123),
        "nine hundred eighty-seven billion six hundred fifty-four million three hundred twenty-one thousand one hundred twenty-three",
    )

    # Additional tests for this track
    print(say(170), "one hundred seventy")
