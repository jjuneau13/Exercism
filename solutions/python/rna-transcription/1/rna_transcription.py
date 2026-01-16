def to_rna(dna_strand):
    rna = {"G":"C", "C":"G", "T":"A", "A":"U"}
    result = ""
    for item in dna_strand:
        result += rna[item]
    return result