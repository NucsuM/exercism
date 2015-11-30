def to_rna(nucleoide):
    dic={   'G':'C',
            'C':'G',
            'T':'A',
            'A':'U'}

    outStr = []

    for pos in range(len(nucleoide)):
        outStr.append(dic[nucleoide[pos]])

    return (''.join(outStr))
