Python 3.8.5 (default, Sep  3 2020, 21:29:08) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # words patterns
>>> import re
>>> pattern = r"Honey"
>>> words = "Honey"
>>> re.match(pattern, words).group(0)
'Honey'
>>> 