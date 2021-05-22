Python 3.8.5 (default, Sep  3 2020, 21:29:08) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from sympy import Symbol
>>> x = Symbol('x')
>>> y = Symbol('y')
>>> from sympy import factor, expand
>>> expr = x**2 + 2*x*y + y**2
>>> factor(expr)
(x + y)**2
>>> # super powerful !