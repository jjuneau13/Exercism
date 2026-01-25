def proteins(strand):
    protein = {"AUG": "Methionine", 
               "UUU": "Phenylalanine",
               "UUC": "Phenylalanine",
               "UUA": "Leucine",
               "UUG": "Leucine",
               "UCU": "Serine",
               "UCC": "Serine",
               "UCA": "Serine",
               "UCG": "Serine",
               "UAU": "Tyrosine",
               "UAC": "Tyrosine",
               "UGU": "Cysteine",
               "UGC": "Cysteine",
               "UGG": "Tryptophan"}
    rna = ""
    result = []
    for codon in strand:
        rna += codon
        if rna in protein:
            result.append(protein[rna])
            rna = ""
    return result