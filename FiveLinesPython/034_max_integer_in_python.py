Python 3.8.5 (default, Sep  3 2020, 21:29:08) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # what's the maximum integer in a
>>> # computer
>>> import sys
>>> sym.maxsize
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    sym.maxsize
NameError: name 'sym' is not defined
>>> sys.maxsize
9223372036854775807
>>> # we can guess it
>>> 2**32 - 1
4294967295
>>> # again
>>> 2**63 -1
9223372036854775807
>>> # it is a match !