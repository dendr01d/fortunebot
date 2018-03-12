# STT = state transition table
# this class holds the data structure representing the finite-state automaton

import random
import pickle


class Graph():
	web = {}

	# this data structure is kind of a doozy
	# the top level is a simple key/value dictionary
	# the key is one of the automaton's "states"
	# the value represents possible transitions from that state
	#	and metadata about the state in question
	# this takes the form of a tuple, which itself contains:
	# another dict comprised of successor/weight pairs
	# and an int that's just the sum of all the successor weights

	# in future versions that int could be replaced with something
	# 	more complicated that represents more information

	
	# prints out the web
	def printGraph(self):
		for key in self.web:
			print('\n{} ({}):'.format(key, self.web[key][1]))

			for succ in self.web[key][0]:
				print('    ({}) {}'.format(self.web[key][0][succ], succ))


	# save the web to the file specified
	def export(self, fileName):
		data = open(fileName, 'wb')
		pickle.dump(self.web, data)
		data.close()


	# load the web from the file specified
	# beware IOError exceptions
	def load(self, fileName):
		data = open(fileName, 'wb')
		self.web = pickle.load(data)
		data.close()


	# insert a state/successor pair into the graph
	# all of the particulars of the data structure are abstracted away
	# :)
	def insert(self, key, succ):
		# add/update the state
		if key not in self.web:
			self.web[key] = [{}, 1]
		else:
			self.web[key][1] += 1

		# add/update the successor
		if succ not in self.web[key][0]:
			self.web[key][0][succ] = 1
		else:
			self.web[key][0][succ] += 1


	# given a key, returns a random successor
	# the distribution of successors is scaled by their respective weights
	def walk(self, key):
		newState = 'N/A'

		# this method of random selection seems kind of hacky to me
		rnum = random.randint(0, self.web[key][1])
		
		for succ in self.web[key][0]:
			if rnum < 0:
				break
			else:
				rnum -= self.web[key][0][succ]
				newState = succ

		return newState


	# return a random state from the graph
	def randState(self):
		return random.choice(list(self.web))


	# given a key, return the combined weight of its successors
	def getTotalSucc(self, key):
		return self.web[key][1]


