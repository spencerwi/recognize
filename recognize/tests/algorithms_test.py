try:
    from unittest2 import TestCase
except ImportError:
    from unittest import TestCase

from recognize import algorithms

class TestAlgorithsm(TestCase):

    def test_levenshtein(self):
        """levenshtein should return the correct Levenshtein distance between two words."""
        assert algorithms.levenshtein("one", "ode")   == 1  # simplest case: change a letter
        assert algorithms.levenshtein("one", "once")  == 1  # slightly more complex: letter insertion
        assert algorithms.levenshtein("two", "three") == 4  # different word lengths AND different letters
