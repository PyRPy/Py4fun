# guess a number in python
# from https://opensource.com/article/20/12/learn-python
import random as rd
number = rd.randint(1, 100)
print("guess a number between 1 and 100")
while True:
    guess = int(input())
    if guess < = number:
        print("too low ! try again !")
    elif guess > number:
        print("too high, try again !")
    else:
        print("you got it right !")
        break

