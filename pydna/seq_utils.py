def complement_codon(input_codon):
    """

    :param input_codon:
    :return:
    """
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
    """Validates a codon by checking that allowed list of bases are included
    in our input variable.

    :param input_codon: codon, may be valid or not
    :return: True or False

    >>> from pydna import seq_utils
    >>> input_codon = 'ATC'
    >>> seq_utils.is_codon_correct(input_codon)
    True
    """
    if type(input_codon) == float:
        return False

    allowed_bases = ['A', 'T', 'C', 'G', 'N', '?', '-']

    for base in input_codon:
        if base in allowed_bases:
            continue
        else:
            print("Your codon is incorrect")
            return False

    return True

