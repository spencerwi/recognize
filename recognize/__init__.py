"""recognize is a simple python library for vocabulary recognition.

It uses a configurable Levenshtein distance threshold to determine which words of a given vocabulary are likely matches.

*Usage*

For use with recognize, your vocabulary should be an iterable of string-like objects.

Then, import recognize and just call the recognize() method with your word to match, your vocabulary, and optionally your desired Levenshtein distance threshold for matching (the default is 3):

    >>> from recognize import recognize
    >>> recognize("ana", vocabulary=["banana", "grape", "orange", "cucumber"], distance=3)
    set(['banana'])

To avoid having to pass your vocabulary and threshold into every call to recognize(), you can also initialize a Recognizer object with these parameters:

    >>> from recognize import Recognizer
    >>> r = Recognizer(vocabulary=["banana", "grape", "orange", "cucumber"], distance=3)
    >>> r.recognize("ana")
    set(['banana'])
    >>> r.recognize("oge")
    set(['orange'])
"""

vocabulary = []
threshold = 3


class Recognizer(object):
    def __init__(self, vocabulary = [], distance = 3):
        self.vocabulary = vocabulary
        self.distance = distance

    def vocab_from_file(self, filename, delimiter=None):
        """Reads vocabulary from a file. Delimiter defaults to all whitespace."""
        # TODO: finish this
        raise NotImplementedError

    # TODO: move this to a "algorithms.distance" package, refactor to "get_distance()" method
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
        candidates = set(candidate for candidate in self.vocabulary if Recognizer.levenshtein(candidate, word) <= self.distance)
        return candidates


def recognize(word, vocabulary = [], distance = 3):
    """Fetches a list of candidate vocabulary words from a given wordlist that a might match the given word."""
    recognizer = Recognizer(vocabulary, distance)
    return recognizer.recognize(word)
