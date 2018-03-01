from markov2 import *


chain = Graph()
chain.feedCorpus('singleFortune.txt')
# chain.printWeb()

# for i in range(0, 10):
#	print(chain.generate())


longerChain = Graph()
longerChain.feedCorpus('EICorpus.txt')
# longerChain.printWeb()

longerChain.feedCorpus('handmade_corpus')


for i in range(0, 50):
	print(longerChain.generate())
