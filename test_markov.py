from markov import *

model = markovModel()
model.feedCorpus('singleFortune.txt')
model.stt.printGraph()

for i in range(0, 5):
	print(model.generate())


model.feedCorpus('EICorpus.txt')
model.feedCorpus('handmadeCorpus.txt')

for i in range(0, 50):
	print(model.generate())
