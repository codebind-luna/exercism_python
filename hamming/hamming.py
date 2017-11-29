def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError

    hamming_distance = 0
    for pos, nucleotide in enumerate(strand_a):
        if nucleotide != strand_b[pos]:
            hamming_distance += 1

    return hamming_distance