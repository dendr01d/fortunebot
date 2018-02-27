import random

class Graph:
	web = {}
	
	# A dict that pairs a tuple with another tuple
	# the first tuple contains two strings (words)
	# the second tuple represents the words likely to follow
	# the second tuple is comprised of another dict and an int
	# the dict pairs more strings (words) with their relative weight
	# the int is the sum of all the weights

	# displays the web
	def printWeb(self):
		for wordPair in self.web:
			print('\n{} / {} ({}):'.format(wordPair(0), wordPair(1), self.web[wordPair][1]))
			
			for word3 in self.web[wordPair][0]:
				print('\t{} {}'.format(word3, self.web[wordPair][0][word3]))

	# adds a single word association to the web
	def addWord(self, word1, word2, word3):
		wordPair = (word1, word2)

		if wordPair not in self.web:
			self.web[wordPair] = [{}, 1]
		else:
			self.web[wordPair][1] += 1

		if word3 not in self.web[wordPair][0]:
			self.web[wordPair][0][word3] = 1
		else:
			self.web[wordPair][0][word3] += 1

	# turns a string into a list of words ready for the web
	# eventually I may want punctuation to be tokenized?
	def formatText(self, text):
		text = text.lower()
		text = text.strip() # for any extra whitespace
		text = text.split(' ')
		newText = [word.strip(" ,.!?;:-[]%*()\'\"\n") for word in text]
		
		return newText


	# adds a snippet of text to the web
	def addSnippet(self, text):
		
		formattedText = self.formatText(text)
		if 'i' in formattedText or 'me' in formattedText:
			return		


		wordList = ['<START1>', '<START2>'] + self.formatText(text) + ['<END>']
		
		for i in range(0, len(wordList)-2):
			self.addWord(wordList[i], wordList[i+1], wordList[i+2])
		
	
	# reads a file full of single-line snippets
	#	and adds each of them to the web
	def feedCorpus(self, fileName):
		inFile = open(fileName, 'r')
		fileLines = inFile.readlines()
		inFile.close()

		for snippet in fileLines:
			self.addSnippet(snippet)
		
	# given a word pair, pulls another word out of the web
	def genWord(self, word1, word2):
		wordPair = (word1, word2)
		rnum = random.randint(0, self.web[wordPair][1])
		newWord = 'N/A'

		for option in self.web[wordPair][0]:
			if rnum < 0:
				break
			else:
				rnum -= self.web[wordPair][0][option]
				newWord = option

		return newWord
			
	# takes a string and removes START and END tags
	# and capitalizes the first letter
	def reformatText(self, text):
		text = text.strip("<STAR12> END")
		text = text.capitalize()

		return text


	# generates a new snippet of text using the web
	def generate(self):
		word1 = '<START1>'
		word2 = '<START2>'
		text = '<START1> <START2>'

		while word2 != '<END>' and len(text) < 250:
			newWord = self.genWord(word1, word2)
			text = text + ' '
			text = text + newWord
			word1 = word2
			word2 = newWord
		
		return self.reformatText(text)
