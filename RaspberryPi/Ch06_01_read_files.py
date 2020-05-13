# reading files

f = open('hangman_words.txt')
words = f.read().splitlines()
print(words)
f.close()