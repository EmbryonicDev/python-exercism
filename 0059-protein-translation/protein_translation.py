def proteins(strand):
    codons = {
        "Methionine": ["AUG"],
        "Phenylalanine": ["UUU", "UUC"],
        "Leucine": ["UUA", "UUG"],
        "Serine": ["UCU", "UCC", "UCA", "UCG"],
        "Tyrosine": ["UAU", "UAC"],
        "Cysteine": ["UGU", "UGC"],
        "Tryptophan": ["UGG"],
        "STOP": ["UAA", "UAG", "UGA"],
    }

    # Use a generator to iterate through the input strand
    codons_lst = (strand[i : i + 3] for i in range(0, len(strand), 3))

    protein_sequence = []
    for codon in codons_lst:
        for protein, codon_list in codons.items():
            if codon in codon_list:
                if protein == "STOP":
                    return protein_sequence
                protein_sequence.append(protein)

    return protein_sequence


if __name__ == "__main__":
    value = "AUG"
    expected = ["Methionine"]
    print(proteins(value), expected)

    value = "UUU"
    expected = ["Phenylalanine"]
    print(proteins(value), expected)

    value = "UUC"
    expected = ["Phenylalanine"]
    print(proteins(value), expected)

    value = "UUA"
    expected = ["Leucine"]
    print(proteins(value), expected)

    value = "UUG"
    expected = ["Leucine"]
    print(proteins(value), expected)

    value = "UCU"
    expected = ["Serine"]
    print(proteins(value), expected)

    value = "UCC"
    expected = ["Serine"]
    print(proteins(value), expected)

    value = "UCA"
    expected = ["Serine"]
    print(proteins(value), expected)

    value = "UCG"
    expected = ["Serine"]
    print(proteins(value), expected)

    value = "UAU"
    expected = ["Tyrosine"]
    print(proteins(value), expected)

    value = "UAC"
    expected = ["Tyrosine"]
    print(proteins(value), expected)

    value = "UGU"
    expected = ["Cysteine"]
    print(proteins(value), expected)

    value = "UGC"
    expected = ["Cysteine"]
    print(proteins(value), expected)

    value = "UGG"
    expected = ["Tryptophan"]
    print(proteins(value), expected)

    value = "UAA"
    expected = []
    print(proteins(value), expected)

    value = "UAG"
    expected = []
    print(proteins(value), expected)

    value = "UGA"
    expected = []
    print(proteins(value), expected)

    value = "UUUUUU"
    expected = ["Phenylalanine", "Phenylalanine"]
    print(proteins(value), expected)

    value = "UUAUUG"
    expected = ["Leucine", "Leucine"]
    print(proteins(value), expected)

    value = "AUGUUUUGG"
    expected = ["Methionine", "Phenylalanine", "Tryptophan"]
    print(proteins(value), expected)

    value = "UAGUGG"
    expected = []
    print(proteins(value), expected)

    value = "UGGUAG"
    expected = ["Tryptophan"]
    print(proteins(value), expected)

    value = "AUGUUUUAA"
    expected = ["Methionine", "Phenylalanine"]
    print(proteins(value), expected)

    value = "UGGUAGUGG"
    expected = ["Tryptophan"]
    print(proteins(value), expected)

    value = "UGGUGUUAUUAAUGGUUU"
    expected = ["Tryptophan", "Cysteine", "Tyrosine"]
    print(proteins(value), expected)
