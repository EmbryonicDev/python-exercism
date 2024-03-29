def translate(text):
    suffix = "ay"
    lst_text = text.split()
    temp_list = []

    for word in lst_text:
        copied_word = word
        pre_suffix = ""
        first_2letters = copied_word[0:2]

        if first_2letters == "xr":
            temp_list.append(copied_word + pre_suffix + suffix)
            continue

        if first_2letters == "ye":
            temp_list.append(copied_word[1:] + "y" + suffix)
            continue

        # move leading consonants to the back & add suffix
        while copied_word[0] not in "aeiouy":
            # "qu" are handled together
            if copied_word[0:2] == "qu":
                pre_suffix += "qu"
                copied_word = copied_word[2:]
                continue
            # moving single letters
            pre_suffix += copied_word[0]
            copied_word = copied_word[1:]

        temp_list.append(copied_word + pre_suffix + suffix)

    return " ".join(temp_list)


if __name__ == "__main__":
    print(translate("apple"), "appleay")

    print(translate("ear"), "earay")

    print(translate("igloo"), "iglooay")

    print(translate("object"), "objectay")

    print(translate("under"), "underay")

    print(translate("equal"), "equalay")

    print(translate("pig"), "igpay")

    print(translate("koala"), "oalakay")

    print(translate("xenon"), "enonxay")

    print(translate("qat"), "atqay")

    print(translate("chair"), "airchay")

    print(translate("queen"), "eenquay")

    print(translate("square"), "aresquay")

    print(translate("therapy"), "erapythay")

    print(translate("thrush"), "ushthray")

    print(translate("school"), "oolschay")

    print(translate("yttria"), "yttriaay")

    print(translate("xray"), "xrayay")

    print(translate("yellow"), "ellowyay")

    print(translate("rhythm"), "ythmrhay")

    print(translate("my"), "ymay")

    print(translate("quick fast run"), "ickquay astfay unray")
