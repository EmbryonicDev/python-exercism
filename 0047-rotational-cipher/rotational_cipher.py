def rotate(text, key):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    answer = ""

    for letter in text:
        letter_lower = letter.lower()

        # add characters not in alpha
        if letter_lower not in alpha:
            answer += letter
            continue

        # get index of converted letter
        index = alpha.index(letter_lower)
        for i in range(key):
            index += 1
            if index == 26:
                index = 0

        answer += alpha[index].upper() if letter.isupper() else alpha[index]

    return answer


if __name__ == "__main__":
    print(rotate("a", 0), "a")

    print(rotate("a", 1), "b")

    print(rotate("a", 26), "a")

    print(rotate("m", 13), "z")

    print(rotate("n", 13), "a")

    print(rotate("OMG", 5), "TRL")

    print(rotate("O M G", 5), "T R L")

    print(rotate("Testing 1 2 3 testing", 4), "Xiwxmrk 1 2 3 xiwxmrk")

    print(rotate("Let's eat, Grandma!", 21), "Gzo'n zvo, Bmviyhv!")

    print(
        rotate("The quick brown fox jumps over the lazy dog.", 13),
        "Gur dhvpx oebja sbk whzcf bire gur ynml qbt.",
    )
