recognize
=========

recognize is a simple python library for vocabulary recognition.

It uses a configurable [Levenshtein distance](http://en.wikipedia.org/wiki/Levenshtein_distance) threshold to 
determine which words of a given vocabulary are likely matches.


Usage
-----

For use with recognize, your vocabulary should be an iterable of string-like objects.

Then, import recognize and initialize it with your vocabulary (and optionally your desired Levenshtein 
distance threshold for matching; the default is 3):

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

Installation
------------

After cloning the project into a directory, run `python setup.py install`

Tests are available by running `python setup.py test`; nosetest is used as the test runner.


