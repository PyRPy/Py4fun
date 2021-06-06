Python 3.8.10 (v3.8.10:3d8993a744, May  3 2021, 09:09:08) 
[Clang 12.0.5 (clang-1205.0.22.9)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> random.random()
0.5492564854748728
>>> random.randint(1, 6)
4
>>> myList = [1, 2, 3, 4, 5, 6]
>>> random.shuffle(myList)
>>> myList
[3, 5, 2, 4, 6, 1]
>>> random.choice(myList)
1
>>> # like roll a dice