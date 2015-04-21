def complement_codon(input_codon):
    base_complements = {
            'A': 'T',
            'T': 'A',
            'C': 'G',
            'G': 'C',
    }

    first_base = input_codon[0]
    second_base = input_codon[1]
    third_base = input_codon[2]

    complemented_codon = first_base + second_base + third_base

    return complemented_codon

