def to_rna(dna_strand):
    dna_compliments = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U",
   }
    rna = ''
    for l in dna_strand:
        rna += dna_compliments[l]
    return rna

print(to_rna(''))
print(to_rna('C'))
print(to_rna('G'))
print(to_rna('T'))
print(to_rna('A'))
print(to_rna('ACGTGGTCTTAA'))




