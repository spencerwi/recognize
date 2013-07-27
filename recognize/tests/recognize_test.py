#!/usr/bin/env python
from unittest import TestCase

import recognize

class TestRecognizer(TestCase):
    def setUp(self):
        self.recognizer = recognize.Recognizer(vocabulary=["grape", "banana", "strawberry"],
                                     distance=3)

    def test_levenshtein(self):
        """levenshtein should return the correct Levenshtein distance between two words."""
        self.assertEqual(self.recognizer.levenshtein("one", "ode"), 1)    # simplest case: change a letter
        self.assertEqual(self.recognizer.levenshtein("one", "once"), 1)   # slightly more complex: letter insertion
        self.assertEqual(self.recognizer.levenshtein("two", "three"), 4)  # different word lengths AND different letters

    def test_recognize(self):
        """recognize should return a list of matching words within the specified threshold."""
        expected = set(["banana"])
        self.assertSetEqual(self.recognizer.recognize("ana"), expected) # "ana" should match to "banana" with a levenshtein threshold of 3


class TestShortcutMethod(TestCase):
    def setUp(self):
        self.vocabulary = ["banana", "grape", "orange"]
        self.distance = 3

    def test_recognize_shortcut_correctness(self):
        """The shortcut method should produce correct results."""
        # Test that the shortcut result is correct
        expected = set(["banana"])
        result = recognize.recognize("ana", vocabulary=self.vocabulary, distance=self.distance) 
        self.assertSetEqual(result, expected)

    def test_recognize_shortcut_consistency(self):
        """The shortcut method should produce the same results as the "long way."""
        expected = set(["banana"])
        result = recognize.recognize("ana", vocabulary=self.vocabulary, distance=self.distance) 

        r = recognize.Recognizer(self.vocabulary, self.distance)
        long_way_result = r.recognize("ana")
        self.assertSetEqual(result, long_way_result)
