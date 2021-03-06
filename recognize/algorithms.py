"""A collection of word-distance algorithms.

All algorithms are methods that take two string parameters and return the 
"distance" between them as an integer.

Contains:
    * levenshtein
"""


def levenshtein(seq1, seq2):
    """Calculates the levenshtein distance between two strings."""
    oneago = None
    thisrow = range(1, len(seq2) + 1) + [0]
    for x in xrange(len(seq1)):
        (twoago, oneago, thisrow,) = (oneago, thisrow, [0] * len(seq2) + [x + 1])
        for y in xrange(len(seq2)):
            delcost = oneago[y] + 1
            addcost = thisrow[(y - 1)] + 1
            subcost = oneago[(y - 1)] + (seq1[x] != seq2[y])
            thisrow[y] = min(delcost, addcost, subcost)


    return thisrow[(len(seq2) - 1)]
