def roman(number):
    roman_num = ''
    index_str = str(number).rjust(4, "0")
    num_list = [int(num) for num in index_str]

    def reduce(num, subtract):
        return num - subtract

    def translator(num, roman_chars):
        add_str = ''
        char_1, char_2, char_3 = (char for char in roman_chars)

        while True:
            if num < 1:
                break
            if num >= 9:
                add_str += char_1 + char_3
                num = reduce(num, 9)
            elif num >= 5:
                add_str += char_2
                num = reduce(num, 5)
            elif num >= 4:
                add_str += char_1 + char_2
                num = reduce(num, 4)
            elif num >= 1:
                add_str += char_1
                num = reduce(num, 1)
        return add_str

    thousands = int(num_list.pop(0))
    roman_num += thousands * 'M'

    for chars in ['CDM', 'XLC', 'IVX']:
        """
        100 / 500 / 1000 CDM
        10 / 50 / 100 XLC
        1 / 5 / 10 IVX
        """
        number = int(num_list.pop(0))
        roman_num += translator(number, chars)

    return roman_num


if __name__ == '__main__':
    print(roman(1), "I")
    print(roman(2), "II")
    print(roman(3), "III")
    print(roman(4), "IV")
    print(roman(5), "V")
    print(roman(6), "VI")
    print(roman(9), "IX")
    print(roman(16), "XVI")
    print(roman(27), "XXVII")
    print(roman(48), "XLVIII")
    print(roman(49), "XLIX")
    print(roman(59), "LIX")
    print(roman(66), "LXVI")
    print(roman(93), "XCIII")
    print(roman(141), "CXLI")
    print(roman(163), "CLXIII")
    print(roman(166), "CLXVI")
    print(roman(402), "CDII")
    print(roman(575), "DLXXV")
    print(roman(666), "DCLXVI")
    print(roman(911), "CMXI")
    print(roman(1024), "MXXIV")
    print(roman(1666), "MDCLXVI")
    print(roman(3000), "MMM")
    print(roman(3001), "MMMI")
    print(roman(3999), "MMMCMXCIX")
