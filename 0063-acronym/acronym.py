def abbreviate(words):
    # Split the words by spaces, hyphens, and underscores
    acronym = "".join(
        word[0].upper()
        for word in words.replace("-", " ").replace("_", " ").split()
        if word[0].isalnum()
    )
    return acronym

if __name__ == "__main__":
    print(abbreviate("Portable Network Graphics"), "PNG")

    print(abbreviate("Ruby on Rails"), "ROR")

    print(abbreviate("First In, First Out"), "FIFO")

    print(abbreviate("GNU Image Manipulation Program"), "GIMP")

    print(abbreviate("Complementary metal-oxide semiconductor"), "CMOS")

    print(
        abbreviate(
            "Rolling On The Floor Laughing So Hard That My Dogs Came Over And Licked Me"
        ),
        "ROTFLSHTMDCOALM",
    )

    print(abbreviate("Something - I made up from thin air"), "SIMUFTA")

    print(abbreviate("Halley's Comet"), "HC")

    print(abbreviate("The Road _Not_ Taken"), "TRNT")
