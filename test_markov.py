from markov import *


chain = Graph()
chain.feedCorpus('singleFortune.txt')
chain.printWeb()

print ('\n\nNow for some generation...')

for i in range(0, 10):
	print(chain.generate())
