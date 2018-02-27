from markov2 import *


chain = Graph()
chain.feedCorpus('singleFortune.txt')
# chain.printWeb()

# for i in range(0, 10):
#	print(chain.generate())


longerChain = Graph()
longerChain.feedCorpus('EICorpus.txt')
# longerChain.printWeb()

longerChain.feedCorpus('bmc_fortuneCorpus.txt')
longerChain.feedCorpus('author-quote.txt')


for i in range(0, 50):
	print(longerChain.generate())
