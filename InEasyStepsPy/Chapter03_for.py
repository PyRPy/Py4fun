# chapter 3, looping over items
chars = ['A', 'B', 'C']
fruits = ('Apple', 'Banana', 'Cherry')
dict = {'name' : 'Mike', 'ref' : 'Python', 'sys' : 'Win'}

print('\nElements:\t', end = ' ')
for item in chars :
	print(item, end = ' ')

print('\nEnumerate:\t', end = ' ')
for item in enumerate(chars) :
	print(item, end = ' ')

print('\nZipple:\t', end = ' ')
for item in zip(chars, fruits) :
	print(item, end = ' ')

print('\nPaired:')
for key, value in dict.items() :
	print(key, '=', value)
