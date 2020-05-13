# reading files
words_file = 'hangmen_words.txt'
try:

	f = open(words_file)
	words = f.read().splitlines()
	print(words)
	f.close()
	
except IOError:
		print("Cannot find file 'file name'")
		exit()