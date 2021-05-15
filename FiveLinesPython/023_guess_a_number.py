Python 3.8.5 (default, Sep  3 2020, 21:29:08) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # guess a number
>>> myKey = 10
>>> guess = int(input('enter a number'))
enter a number9
>>> if guess > myKey:
	print('too large')
elif guess < myKey:
	print('too small')
else:
	print('correct')

	
too small
>>> 