def recite(start_verse, end_verse):
    data = [
        ('first', 'a Partridge in a Pear Tree.'),
        ('second', 'two Turtle Doves, '),
        ('third', 'three French Hens, '),
        ('fourth', 'four Calling Birds, '),
        ('fifth', 'five Gold Rings, '),
        ('sixth', 'six Geese-a-Laying, '),
        ('seventh', 'seven Swans-a-Swimming, '),
        ('eighth', 'eight Maids-a-Milking, '),
        ('ninth', 'nine Ladies Dancing, '),
        ('tenth', 'ten Lords-a-Leaping, '),
        ('eleventh', 'eleven Pipers Piping, '),
        ('twelfth', 'twelve Drummers Drumming, '),
    ]
    total_verses = []
    gifts_sentence = ''
    for i, data_set in enumerate(data):
        day, gift = data_set[0], data_set[1]
        pre_sentence = f'On the {day} day of Christmas my true love gave to me: '
        gifts_sentence = f'{gift}{gifts_sentence}'
        total_verses.append(f'{pre_sentence}{gifts_sentence}')
        if i == 0:
            gifts_sentence = 'and ' + gifts_sentence

    return total_verses[start_verse-1:end_verse]


if __name__ == "__main__":
    expected = [
        "On the sixth day of Christmas my true love gave to me: "
        "six Geese-a-Laying, "
        "five Gold Rings, "
        "four Calling Birds, "
        "three French Hens, "
        "two Turtle Doves, "
        "and a Partridge in a Pear Tree."
    ]
    print(recite(6, 6))
