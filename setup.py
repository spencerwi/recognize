try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    "name": "recognize",
    "description": "A simple python library for vocabulary recognition.",
    "author": "Spencer Williams",
    "url": "http://github.com/spencerwi/recognize.git",
    "download_url": "https://github.com/spencerwi/recognize/archive/master.zip",
    "author_email": "spencerwi@gmail.com",
    "version": "0.2.0",
    "packages": ["recognize"],
    "classifiers": [
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Topic :: Text Processing :: Linguistic"
    ],
    "test_suite": "nose.collector",
    "tests_require": ['nose']
}

setup(**config)
