# The Perfect Python Script

Based on [this reddit post]( http://www.reddit.com/r/Python/comments/28yo37/what_are_the_top_10_builtin_python_modules_that_a/)
A python script template, it's a demonstrator and reminder for the most usefull python libraries and best practices

Context
-------
,
[The Hitchhiker’s Guide to Python](http://docs.python-guide.org/en/latest/)
 and
[Python patterns](http://python-3-patterns-idioms-test.readthedocs.org/)

This script template aim is to enforce best-pratices use. Please contribute if you feel it should be better written. Pull Request welcome !!!

[![Build Status](https://api.travis-ci.org/GustavePate/perfectpythonbatch.png?branch=master)](https://travis-ci.org/GustavePate/perfectpythonbatch)

## This template make use of

### Generalities

- logging
- Makefile
- requirement.txt / virtualenv
- Json configuration / Borg
- argument parsing: click
- python 2.7 / 3.4 compatibility

### Quality

- py.test
- travis ci
- pep8 compliance check

### Pretty

- colorlog
- click progress bar

## Usefull libraries

- collections:  specifically namedtuples
- tempfile:  always use this to create temporary files
- pillow: image juggling
- decimal: you will need it, try this if you dare:  `print((0.1 + 0.1 + 0.1 - 0.3) == 0)`

## data

- csv:  always use this to read/write CSV files, don't try and roll your own methods, it'll end in tears
- sqllite


## Documentation



## Pending



******

## Todo

- pandas -- csv loading and quick graphing
- datetime
- math -- try and use these functions rather than the global ones, as they're faster when you import them into the global namespace
- re -- regular expressions
- requests -- if you need to do any http requests at all, use this
- string -- I rarely see this used, but it's very handy
- rename git repo to perfect python script
- sphinx
- matplotlib
- unittest
- lxml -- always use this for working with XML data
- BeautifulSoup -- for webscraping and/or parsing potentially malformed HTML
- os / shutils
- setuptools
- redis

## Don't know if it's usefull

- buildout -- I'd recommend this over virtualenv any day
- PyYAML -- for working with YAML docs.
- ujson -- faster than both simplejson and the built-in json modules, handy if you work with lots of/big JSON blobs

## See also

- https://github.com/audreyr/cookiecutter-pypackage.git
- https://github.com/jacebrowning/template-python
- https://github.com/seanfisk/python-project-template
