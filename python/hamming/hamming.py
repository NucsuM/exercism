def distance(seqA, seqB):
    hamming_inc = sum(x != y for x, y in zip(seqA, seqB))
    return hamming_inc
