def find_anagrams(word, candidates):
    results = []
    for list_word in candidates:
        jackpot = True
        word_copy = word

        # Check that list_word and word are the same length and not the same word
        if len(word) == len(list_word) and word.lower() != list_word.lower():
            for letter in list_word:
                if jackpot:
                    if (
                        letter not in word_copy.upper()
                        and letter not in word_copy.lower()
                    ):
                        jackpot = False
                    else:
                        # Removed matched letter from word_copy so that letters appearing more than once can be accounted for
                        word_copy = word_copy.replace(letter, "", 1)

            if jackpot:
                results.append(list_word)
    return results


if __name__ == "__main__":
    candidates = ["hello", "world", "zombies", "pants"]
    expected = []
    print(find_anagrams("diaper", candidates))

    candidates = ["lemons", "cherry", "melons"]
    expected = ["lemons", "melons"]
    print(find_anagrams("solemn", candidates))

    candidates = ["dog", "goody"]
    expected = []
    print(find_anagrams("good", candidates))

    candidates = ["enlists", "google", "inlets", "banana"]
    expected = ["inlets"]
    print(find_anagrams("listen", candidates))

    expected = ["gallery", "regally", "largely"]
    print(find_anagrams("allergy", candidates))

    candidates = ["Eons", "ONES"]
    expected = ["Eons", "ONES"]
    print(find_anagrams("nose", candidates))

    candidates = ["last"]
    expected = []
    print(find_anagrams("mass", candidates))

    candidates = ["cashregister", "Carthorse", "radishes"]
    expected = ["Carthorse"]
    print(find_anagrams("Orchestra", candidates))

    candidates = ["cashregister", "carthorse", "radishes"]
    expected = ["carthorse"]
    print(find_anagrams("Orchestra", candidates))

    candidates = ["cashregister", "Carthorse", "radishes"]
    expected = ["Carthorse"]
    print(find_anagrams("orchestra", candidates))

    candidates = ["go Go GO"]
    expected = []
    print(find_anagrams("go", candidates))

    candidates = ["patter"]
    expected = []
    print(find_anagrams("tapper", candidates))

    candidates = ["BANANA"]
    expected = []
    print(find_anagrams("BANANA", candidates))

    candidates = ["Banana"]
    expected = []
    print(find_anagrams("BANANA", candidates))

    candidates = ["banana"]
    expected = []
    print(find_anagrams("BANANA", candidates))

    candidates = ["LISTEN", "Silent"]
    expected = ["Silent"]
    print(find_anagrams("LISTEN", candidates))
