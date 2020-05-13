# dictionary
eggs_per_week = {'Penny': 7, 'Amy': 6, 'Berna': 0}
print(eggs_per_week)

print(eggs_per_week['Amy'])

eggs_per_week['Penny'] = 3
print(eggs_per_week)

# tuples
tuple = 1, 2, 3
print(tuple)

# tuple[0] = 9

a, b, c = 1, 2, 3
print('c in tuple: ' + str(c))

# multiple return values
def stats(numbers):
	numbers.sort()
	return (numbers[0], numbers[-1])
	
list = [5, 45, 12, 1, 78]
min, max = stats(list)
print('list: ', list)
print('min: ', str(min))
print('max: ', str(max))

# exceptions
try:
	list = list
	list[9]
except IndexError:
	print('Ooops')