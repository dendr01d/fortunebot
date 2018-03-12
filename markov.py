# a generic markov model where singular words are followed by singular words

from stt import *
from util import *

class markovModel:
	stt = Graph()

	# Process a snippet of text and add it to the model
	def addSnippet(self, text):
		wordList = ['<START>'] + tokenize(text) + ['<END>']
		
		for i in range(0, len(wordList)-1):
			self.stt.insert(wordList[i], wordList[i+1])
		
	
	# Read a text file line by line and process each line as a snippet
	def feedCorpus(self, fileName):
		inFile = open(fileName, 'r')
		fileLines = inFile.readlines()
		inFile.close()

		for snippet in fileLines:
			self.addSnippet(snippet)

	# Walk through the STT and create a new snippet of text
	def generate(self):
		word = '<START>'
		text = ['<START>']

		while word != '<END>' and len(text) < 250:
			word = self.stt.walk(word)
			text.append(word)
		
		return finalize(text, ['<START>', '<END>'])
