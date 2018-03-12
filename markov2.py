# a slightly more complicated markov model that matches pairs of words to singular words
# as a result it can create more comprehensible output
# but using the same corpus as a regular model, the stt is quadratically more sparse

from stt import *
from util import *

# this variable determines mutation rate
# see the generate_m() function for details
threshold = 1


class additiveMarkovModel:
	stt = Graph()
	
	# Process a snippet of text and add it to the model
	def addSnippet(self, text):
		wordList = ['<START1>', '<START2>'] + tokenize(text) + ['<END>']
		
		for i in range(0, len(wordList)-2):
			self.stt.insert((wordList[i], wordList[i+1]), wordList[i+2])
		
	
	# Read a text file line by line and process each line as a snippet
	def feedCorpus(self, fileName):
		inFile = open(fileName, 'r')
		fileLines = inFile.readlines()
		inFile.close()

		for snippet in fileLines:
			if snippet is '\n':
				continue
			self.addSnippet(snippet)
		
	# Walk through the STT and create a new snippet of text
	def generate(self):
		word1 = '<START1>'
		word2 = '<START2>'
		text = [word1, word2]

		while word2 != '<END>' and len(text) < 250:
			newWord = self.stt.walk((word1, word2))
			text.append(newWord)
			word1 = word2
			word2 = newWord

		return finalize(text, ['<START1>', '<START2>', '<END>'])

	# Walk through the STT and create a new snippet of text with occasional mutations
	# if a particular state's successors have a combined weight
	#	lower than a certain threshold
	# then randomly choose to insert a random word into the output
	#	instead of the actual successor
	# the chance of this happening scales with how far below the threshold
	def generate_m(self):
		word1 = '<START1>'
		word2 = '<START2>'
		text = [word1, word2]

		while word2 != '<END>' and len(text) < 250:
			newWord = stt.walk((word1, word2))

			if random.randint(0, threshold) > stt.getTotalSucc((word1, word2)):
				text.append('[' + stt.randState()[0] + ']')
			else:
				text.append(newWord)

			# note that the walk continues as if the word hadn't been replaced

			word1 = word2
			word2 = newWord
		
		return self.reformatText(text)
