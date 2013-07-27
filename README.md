recognize
=========

recognize is a simple python library for vocabulary recognition.

It uses a configurable [Levenshtein distance](http://en.wikipedia.org/wiki/Levenshtein_distance) threshold to 
determine which words of a given vocabulary are likely matches.


Usage
-----

For use with recognize, your wordlist should be in an iterable of string-like objects.

Then, import recognize and initialize it with your wordlist (and optionally your desired Levenshtein 
distance threshold for matching; the default is 3):

    import recognize
    rec

