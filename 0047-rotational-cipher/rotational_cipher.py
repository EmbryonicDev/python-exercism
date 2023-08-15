def rotate(text, key):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    answer = ""

    for letter in text:
        if letter.lower() in alpha:
            is_upper = letter.isupper()
            index = (alpha.index(letter.lower()) + key) % 26
            new_letter = alpha[index]
            answer += new_letter.upper() if is_upper else new_letter
        else:
            answer += letter

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
