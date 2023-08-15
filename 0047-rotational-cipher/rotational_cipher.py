def rotate(text: str, key: int):
    """
    Rotates the text by the given key.

    Returns:
        str: The rotated text.
    """

    alpha = "abcdefghijklmnopqrstuvwxyz"

    def rotate_letter(letter, key):
        index = alpha.find(letter.lower())
        if index == -1:
            return letter

        rotated_index = (index + key) % 26
        return (
            alpha[rotated_index].upper() if letter.isupper() else alpha[rotated_index]
        )

    return "".join(rotate_letter(letter, key) for letter in text)


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
