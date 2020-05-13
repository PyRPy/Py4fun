# reading big files
words_file = 'hangman_words.txt'
try:

	f = open(words_file)
	line = f.readline()
	while line != '':
		if line == 'elephant\n':
			print('There is an elephat in the file')
			break
		line = file.readline()
	f.close()
	
except IOError:
		print("Cannot find file: " + words_file)
		exit()