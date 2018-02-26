import random

class Graph:
	web = {}

	#basically it's a dict that pairs a word with a list
	# the list contains a dict and a sum of weights
	# within the subdict are linked words and their ind. weights

	# displays the web
	def printWeb(self):
		for word1 in self.web:
			print('\n{} ({}):'.format(word1, self.web[word1][1]))
			
			for word2 in self.web[word1][0]:
				print('\t{} {}'.format(word2, self.web[word1][0][word2]))

	# adds a single word association to the web
	def addWord(self, word1, word2):
		if word1 not in self.web:
			self.web[word1] = [{}, 1]
		else:
			self.web[word1][1] += 1

		if word2 not in self.web[word1][0]:
			self.web[word1][0][word2] = 1
		else:
			self.web[word1][0][word2] += 1

	# turns a string into a list of words ready for the web
	# eventually I may want punctuation to be tokenized?
	def formatText(self, text):
		text = text.lower()
		text = text.strip(" .!?\n").split(' ')
		#for word in text:
		#	word = word.strip(" ,.\"!?\n")
		
		return text


	# adds a snippet of text to the web
	def addSnippet(self, text):
		wordList = ['<START>'] + self.formatText(text) + ['<END>']
		
		for i in range(0, len(wordList)-1):
			self.addWord(wordList[i], wordList[i+1])
		
	
	# reads a file full of single-line snippets
	#	and adds each of them to the web
	def feedCorpus(self, fileName):
		inFile = open(fileName, 'r')
		fileLines = inFile.readlines()
		inFile.close()

		for snippet in fileLines:
			self.addSnippet(snippet)
		
	# given a word, pulls another word out of the web
	def genWord(self, word):
		rnum = random.randint(0, self.web[word][1])
		newWord = 'N/A'

		for option in self.web[word][0]:
			if rnum < 0:
				break
			else:
				rnum -= self.web[word][0][option]
				newWord = option

		return newWord
			
	# takes a string and removes START and END tags
	# and capitalizes the first letter
	def reformatText(self, text):
		text = text.strip("<STAR> END")
		text = text.capitalize()

		return text


	# generates a new snippet of text using the web
	def generate(self):
		word = '<START>'
		text = '<START>'

		while word != '<END>' and len(text) < 250:
			word = self.genWord(word)
			text = text + ' '
			text = text + word
		
		return self.reformatText(text)
