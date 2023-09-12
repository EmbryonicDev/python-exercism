def encode(plain_text):
    my_dict = create_alpha_dict("to_encode")
    return transform_text(my_dict, plain_text.lower())


def decode(ciphered_text):
    my_dict = create_alpha_dict("to_decode")
    return transform_text(my_dict, ciphered_text.lower(), must_encode=False)


def create_alpha_dict(request):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    alpha_r = alpha[::-1]

    if request == "to_encode":
        return {a: b for a, b in zip(alpha, alpha_r)}
    if request == "to_decode":
        return {b: a for a, b in zip(alpha, alpha_r)}


def transform_text(alpha_dict, text, must_encode=True):
    transformed_text = ""
    spaces = 0

    for letter in text:
        transformed_text_len = len(transformed_text) - spaces

        if letter.isdigit():
            transformed_text += letter
        if letter == " " or not letter.isalpha():
            continue

        if transformed_text_len > 0 and transformed_text_len % 5 == 0 and must_encode:
            transformed_text += " "
            spaces += 1

        transformed_text += alpha_dict[letter]

    return transformed_text


if __name__ == "__main__":
    print(encode("yes"), "bvh")

    print(encode("no"), "ml")

    print(encode("OMG"), "lnt")

    print(encode("O M G"), "lnt")

    print(encode("mindblowingly"), "nrmwy oldrm tob")

    print(encode("Testing,1 2 3, testing."), "gvhgr mt123 gvhgr mt")

    print(encode("Truth is fiction."), "gifgs rhurx grlm")

    print(
        encode("The quick brown fox jumps over the lazy dog."),
        "gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt",
    )

    print(decode("vcvix rhn"), "exercism")

    print(
        decode("zmlyh gzxov rhlug vmzhg vkkrm thglm v"),
        "anobstacleisoftenasteppingstone",
    )

    print(decode("gvhgr mt123 gvhgr mt"), "testing123testing")

    print(
        decode("gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt"),
        "thequickbrownfoxjumpsoverthelazydog",
    )

    print(decode("vc vix    r hn"), "exercism")

    print(decode("zmlyhgzxovrhlugvmzhgvkkrmthglmv"), "anobstacleisoftenasteppingstone")
