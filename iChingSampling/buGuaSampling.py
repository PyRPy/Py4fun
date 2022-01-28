# this program will simulate how to choose 6 'yao' in i-ching

import random

# there are 50 straws / sticks in original boundle
boundleA = [x + 1 for x in range(50)]

# remove one straw
boundleA.pop()

## select first division
diff = [1, 2, 3, 4] # differences in numbers of two sides

## it takes 6 times to get a 'gua'

def divider(boundle, diffs = diff):
    """ This function simulate the divide and count the 
        the number of group of four straws to represent
        the number of straws left after one division.
    """
    divide_first = len(boundle) // 2 + random.choice(diffs)

    divide_first_1 = boundle[:divide_first]
    divide_first_2 = boundle[divide_first:]

    divide_first_1.pop()

    # simulate how to divide further the small boundles
    # into groups of 4 straws
    remainder1 = len(divide_first_1) % 4

    if  remainder1 == 0:
        for i in range(4):
            divide_first_1.pop()

    else:
        for i in range(remainder1):
            divide_first_1.pop()

    # choose the other part of the small boundle
    remainder2= len(divide_first_2) % 4
    if  remainder2 == 0:
        for i in range(4):
            divide_first_2.pop()

    else:
        for i in range(remainder2):
            divide_first_2.pop()

    divide_second = divide_first_1 + divide_first_2
    return divide_second


def buYao(boundle):
    
    part1 = divider(boundle)
    part2 = divider(part1) 
    part3 = divider(part2)

    return len(part3) // 4


print(buYao(boundleA))
# divider(divider(divider(boundleA)))

## to simulate how to get a 'gua' which have 6 'yao'
gua = [] 
for i in range(6):
    yao = buYao(boundleA)
    gua.append(yao)

print(gua)