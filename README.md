# The Perfect Python Batch

A demonstrator and reminder for the most usefull python libraries and best practices

## Context

Based on [this reddit post]( http://www.reddit.com/r/Python/comments/28yo37/what_are_the_top_10_builtin_python_modules_that_a/)
and
[The Hitchhiker’s Guide to Python](http://docs.python-guide.org/en/latest/)
[Python patterns](http://python-3-patterns-idioms-test.readthedocs.org/)

Pull Request welcome !!!

[![Build Status](https://api.travis-ci.org/GustavePate/perfectpythonbatch.png?branch=master)](https://travis-ci.org/GustavePate/perfectpythonbatch)

##Done

### Generalities

- logging
- Makefile
- requirement.txt / virtualenv
- Json configuration / Borg
- argument parsing: click

### Quality

- pep8 compliance
- py.test
- travis ci

### Pretty

- colorlog
- click progress bar

## Pending

******

## Todo

- collections -- specifically namedtuples
- csv -- always use this to read/write CSV files, don't try and roll your own methods, it'll end in tears
- sqllite
- datetime
- sphinx
- math -- try and use these functions rather than the global ones, as they're faster when you import them into the global namespace
- re -- regular expressions
- string -- I rarely see this used, but it's very handy
- tempfile -- always use this to create temporary files
- pandas -- csv loading and quick graphing
- matplotlib
- unittest
- requests -- if you need to do any http requests at all, use this
- lxml -- always use this for working with XML data
- PyYAML -- for working with YAML docs.
- buildout -- I'd recommend this over virtualenv any day
- BeautifulSoup -- for webscraping and/or parsing potentially malformed HTML
- os / shutils
- setuptools

## Don't know

- ujson -- faster than both simplejson and the built-in json modules, handy if you work with lots of/big JSON blobs
