def get_length(dna):
    dna_length = 0
    for x in dna:
        if x in "AGCT":
            dna_length += 1
    return dna_length
    # """ (str) -> int
    #
    # Return the length of the DNA sequence dna.
    #
    # >>> get_length('ATCGAT')
    # 6
    # >>> get_length('ATCG')
    # 4
    # """


def is_longer(dna1, dna2):
    if dna1 > dna2:
        return True
    # """ (str, str) -> bool
    #
    # Return True if and only if DNA sequence dna1 is longer than DNA sequence
    # dna2.
    #
    # >>> is_longer('ATCG', 'AT')
    # True
    # >>> is_longer('ATCG', 'ATCGGA')
    # False
    # """


def count_nucleotides(dna, nucleotide):
    nucleotide_counter = 0
    for x in dna:
        if x == nucleotide:
            nucleotide_counter += 1
    return nucleotide_counter
    # """ (str, str) -> int
    #
    # Return the number of occurrences of nucleotide in the DNA sequence dna.
    #
    # >>> count_nucleotides('ATCGGC', 'G')
    # 2
    # >>> count_nucleotides('ATCTA', 'G')
    # 0
    # """


def contains_sequence(dna1, dna2):
    return dna2 in dna1

    # """ (str, str) -> bool
    #
    # Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    # dna1.
    #
    # >>> contains_sequence('ATCGGC', 'GG')
    # True
    # >>> contains_sequence('ATCGGC', 'GT')
    # False
    #
    # """


def is_valid_sequence(dna):
    for validity in dna:
        if validity not in "ATCG":
            return False
        else:
            return True

    # (str) -> bool
    # The parameter is a potential DNA sequence. Return True if the DNA sequence is valid.
    # # >>> is_valid_sequence("ATCG")
    #     True
    # # >>> is_valid_sequence("ATCGF")
    #     False


def insert_sequence(dna1, dna2, x):
    return dna1[:x] + dna2 + dna1[x:]
    # (str, str, int) -> str
    # The first two parameters are DNA sequences and the third parameter is an index.
    # Return the DNA sequence obtained by inserting the second DNA sequence
    # into the first DNA sequence at the given index. (You can assume that the index is valid)
    # >>> insert_sequence("CCGG", "AT", 2)
    #     "CCATGG"
    # >>> insert_sequence("ATCG", "AA", 1)
    #     "AAATCG"


def get_complement(dna):
    if dna == "T":
        return "A"
    elif dna == "A":
        return "T"
    elif dna == "G":
        return "C"
    else:
        return "G"

    # (str) -> str
    # The first parameter is a nucleotide ("A", "T", "C", "G")
    # Return the nucleotide's complement.
    # >>> get_complement("G")
    #       C
    # >>> get_complement("T")
    #       A


def get_complementary_sequence(dna):
    complementing = ""
    for x in dna:
        complementing += get_complement(x)
    return complementing

    # (str) -> str
    # The parameter is a DNA sequence.
    # Return the DNA sequence that is complementary to the given DNA sequence.
    # # >>> get_complementary_sequence("AT")
    #         TA
