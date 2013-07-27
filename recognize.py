vocabulary = []
threshold = 3

class Recognizer(object):
    def __init__(self, vocabulary = [], distance = 3):
        self.vocabulary = vocabulary
        self.distance = distance


    @staticmethod
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


    def recognize(self, word):
        """Fetches a list of candidate vocabulary words that a might match the given word."""
        if word in self.vocabulary:
            return word
        candidates = {candidate for candidate in self.vocabulary if Recognizer.levenshtein(candidate, word) <= self.distance}
        return candidates


def recognize(word, vocabulary = [], distance = 3):
    """Fetches a list of candidate vocabulary words from a given wordlist that a might match the given word."""
    recognizer = Recognizer(vocabulary, distance)
    return recognizer.recognize(word)
