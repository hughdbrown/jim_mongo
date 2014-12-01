import re

filename_re = re.compile(r'''
    results\-
    (?P<lohi>hi|lo)
    \-
    (?P<rank>\d+)
    \.txt
''', re.VERBOSE)


def process(filename):
    print("-" * 30)
    print(filename)
    m = filename_re.match(filename)
    g = m.groupdict()
    rank = int(g["rank"])
    lohi = g["lohi"].strip()
    
    with open(filename) as handle:
        while True:
            score = handle.readline()
            if not score:
                break
            else:
                score = int(score.strip())
                data = [handle.readline() for i in range(rank)]
                yield (rank, score, lohi, data)
