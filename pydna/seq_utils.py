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

    first_complemented_base = base_complements[first_base]
    second_complemented_base = base_complements[second_base]
    third_complemented_base = base_complements[third_base]

    complemented_codon = first_complemented_base + second_complemented_base + third_complemented_base

    return complemented_codon


def is_codon_correct(input_codon):
    allowed_bases = ['A', 'T', 'C', 'G', 'N', '?', '-']

    for base in input_codon:
        if base in allowed_bases:
            continue
        else:
            print("Your codon is incorrect")
            return False

    return True

