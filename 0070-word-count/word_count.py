import re


def count_words(sentence):
    word_counts = {}

    # Replace non-alphanumeric characters (except apostrophes)
    # with spaces & convert sentence to lowercase
    sentence = re.sub(r"[^a-z0-9'\s]", " ", sentence.lower())

    # Count word occurrences
    for word in re.findall(r"\b\w+(?:'\w+)*(?:\b|$)", sentence):
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts
