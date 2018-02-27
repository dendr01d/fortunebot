from markov import *


chain = Graph()
chain.feedCorpus('singleFortune.txt')
chain.printWeb()

print ('\n\nNow for some generation...')

for i in range(0, 10):
	print(chain.generate())


longerChain = Graph()
longerChain.feedCorpus('EICorpus.txt')
longerChain.printWeb()

for i in range(0, 40):
	print(longerChain.generate())
