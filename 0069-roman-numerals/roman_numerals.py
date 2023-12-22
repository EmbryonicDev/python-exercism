def roman(number):
    roman_chars = [
        ('M', 1000),
        ('CM', 900),
        ('D', 500),
        ('CD', 400),
        ('C', 100),
        ('XC', 90),
        ('L', 50),
        ('XL', 40),
        ('X', 10),
        ('IX', 9),
        ('V', 5),
        ('IV', 4),
        ('I', 1),
    ]

    roman_num = ''

    for char, value in roman_chars:
        while number >= value:
            roman_num += char
            number -= value

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
