class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num
        self.card_num = self.strip()

    def valid(self):
        if self.has_invalid_length() or self.has_invalid_characters():
            return False
        return self.div_by_ten()

    def div_by_ten(self):
        return self.calculate_sum() % 10 == 0

    def strip(self):
        return self.card_num.replace(" ", "")

    def has_invalid_length(self):
        return len(self.card_num) < 2

    def has_invalid_characters(self):
        return not all(char.isdigit() for char in self.card_num)

    def calculate_sum(self):
        sum_total = 0
        # reverse card_num
        card_num_r = self.card_num[::-1]

        for i, char in enumerate(card_num_r):
            digit = int(char)

            # every second index in reversed card_num
            if i % 2 != 0:
                digit *= 2
                if digit > 9:
                    sum_total += digit - 9
                else:
                    sum_total += digit
            # every even index in reversed card_num
            else:
                sum_total += digit

        return sum_total


if __name__ == "__main__":
    print(Luhn("1").valid(), False)

    print(Luhn("0").valid(), False)

    print(Luhn("059").valid(), True)

    print(Luhn("59").valid(), True)

    print(Luhn("055 444 285").valid(), True)

    print(Luhn("055 444 286").valid(), False)

    print(Luhn("8273 1232 7352 0569").valid(), False)

    print(Luhn("1 2345 6789 1234 5678 9012").valid(), False)

    print(Luhn("1 2345 6789 1234 5678 9013").valid(), False)

    print(Luhn("095 245 88").valid(), True)

    print(Luhn("234 567 891 234").valid(), True)

    print(Luhn("059a").valid(), False)

    print(Luhn("055-444-285").valid(), False)

    print(Luhn("055# 444$ 285").valid(), False)

    print(Luhn(" 0").valid(), False)

    print(Luhn("0000 0").valid(), True)

    print(Luhn("091").valid(), True)

    print(Luhn("9999999999 9999999999 9999999999 9999999999").valid(), True)

    print(Luhn("109").valid(), True)

    print(Luhn("055b 444 285").valid(), False)

    print(Luhn(":9").valid(), False)

    print(Luhn("59%59").valid(), False)

    # Additional tests for this track

    # This test was added, because we saw many implementations
    # in which the first call to valid() worked, but the
    # second call failed().
    number = Luhn("055 444 285")
    print(number.valid(), True)
    print(number.valid(), True)
