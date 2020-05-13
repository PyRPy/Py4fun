# changing a list
basket = ['Apple', 'Bun', 'Cola']
crate = ['Egg', 'Fig', 'Grape']

print('Basket list:', basket)
print('Basket elements:', len(basket))

basket.append('Damson')
print('Appended:', basket)
print('Last item removed:', basket.pop())
print('Basket list:', basket)

basket.extend(crate)
print('Extended:', basket)
del basket[1]
print('Item removed:', basket)
del basket[1:3]
print('Slice removed:', basket)