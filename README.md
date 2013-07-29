recognize
=========

[![Build Status](https://travis-ci.org/spencerwi/recognize.png)](https://travis-ci.org/spencerwi/recognize)

recognize is a simple python library for vocabulary recognition.

It uses a configurable distance threshold from an arbitrary word-distance algorithm 
(defaults to the [Levenshtein algorithm](http://en.wikipedia.org/wiki/Levenshtein_distance)) to 
determine which words of a given vocabulary are likely matches.


Usage
-----

For use with recognize, your vocabulary should be an iterable of string-like objects.

Then, import recognize and just call the `recognize()` method with your word to match, your vocabulary, 
and optionally your desired distance threshold for matching (the default is 3):

```python
>>> from recognize import recognize
>>> recognize("ana", vocabulary=["banana", "grape", "orange", "cucumber"], distance=3)
set(['banana'])
```
    

To avoid having to pass your vocabulary and threshold into every call to `recognize()`, you can also initialize a
Recognizer object with these parameters:

```python
>>> from recognize import Recognizer
>>> r = Recognizer(vocabulary=["banana", "grape", "orange", "cucumber"], distance=3)
>>> r.recognize("ana")
set(['banana'])
>>> r.recognize("oge")
set(['orange'])
```

Algorithms
----------

By default, recognize uses the [Levenshtein algorithm](http://en.wikipedia.org/wiki/Levenshtein_distance) 
for determining distance between two words. The implementation for this is included in the 
`recognize.algorithms` module.

A Recognizer (and by extention, the `recognize` shortcut method) can accept an arbitrary word-distance function as 
a keyword parameter, with some constraints:

1. The function must accept two strings as parameters
2. The function must return an integer to be used as the "distance" between the two string parameters

For example:

```python
>>> from recognize import recognize
>>> def foo_distance(str1, str2):
...     if str1 is str2: return 1
...     return 2
>>> recognize("ana", vocabulary=["banana", "orange"], distance=3, algorithm=foo_distance)
set(['orange', 'banana'])
```

In this example, we defined `foo_distance` as our example distance algorithm; in practice you'd want your algorithm 
to be a bit more intelligent to avoid matching the entire vocabulary (or none of the vocabulary).

Likewise, you can initialize a Recognizer with a custom distance algorithm:

```python
>>> from recognize import Recognizer
>>> def foo_distance(str1, str2):
...     if str1 is str2: return 1
...     return 2
>>> r = Recognizer(vocabulary=["banana", "orange"], algorithm=foo_distance)
>>> r.recognize("ana")
set(['orange', 'banana'])
```


Installation
------------

After cloning the project into a directory, run `python setup.py install`

Tests are available by running `python setup.py test`; nosetest is used as the test runner.
