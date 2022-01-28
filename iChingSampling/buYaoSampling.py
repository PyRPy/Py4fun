# this program will simulate how to choose 6 'yao' in i-ching
# import numpy as np

# boundle0 = np.arange(50) + 1
# print(boundle0)

# boundle1 = boundle0[-1]
# print(boundle1)

# print(type(boundle0))

import random

# there are 50 straws / sticks in original boundle
boundleA = [x + 1 for x in range(50)]

# print(boundleA)
# print(type(boundleA))

# remove one straw
boundleA.pop()
# print(boundleA)

## select first division
diffs = [1, 2, 3, 4] # differences in numbers of two sides
divide_first = len(boundleA) // 2 + random.choice(diffs)
print(divide_first)

divide_first_1 = boundleA[:divide_first]
divide_first_2 = boundleA[divide_first:]

print(divide_first_1)
print(divide_first_2)

divide_first_1.pop()

remainders = len(divide_first_1) % 4

if  remainders == 0 & len(divide_first_1) != 0:
    for i in range(4):
        divide_first_1.pop()

else:
    for i in range(remainders):
        divide_first_1.pop()

print(len(divide_first_1)) 

# choose the other port of the small boundle
remainders = len(divide_first_2) % 4

if  remainders == 0 & len(divide_first_2) != 0:
    for i in range(4):
        divide_first_2.pop()

else:
    for i in range(remainders):
        divide_first_2.pop()

print(len(divide_first_2)) 

divide_second = divide_first_1 + divide_first_2
print(len(divide_second))


    