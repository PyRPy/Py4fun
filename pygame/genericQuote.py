# generic quote
# from 'MATH ADVENTURES WITH PYTHON'
import random

target = "I never go back on my word, because that is my Ninja way."
characters = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.',?!"

def makeList():
    """Return a list of characters the same length as the target."""
    charList = []
    for i in range(len(target)):
        charList.append(random.choice(characters))
    return charList

def score(mylist):
    """Return one integer : the number of matches with target."""
    matches = 0
    for i in range(len(target)):
        if mylist[i] == target[i]:
            matches += 1
    return matches


    
def mutate(mylist):
    """Return mylist with one letter changed."""
    newlist = list(mylist)
    new_letter = random.choice(characters)
    index = random.randint(0, len(target)-1)
    newlist[index] = new_letter
    return newlist

random.seed()
bestList = makeList()
bestScore = score(bestList)

guesses = 0

while True:
    guess = mutate(bestList)
    guessScore = score(guess)
    guesses += 1
    
    if guessScore <= bestScore:
        continue
    
    print(''.join(guess), guessScore, guesses)
    if guessScore == len(target):
        break

    bestList = list(guess)
    bestScore = guessScore

    


    
