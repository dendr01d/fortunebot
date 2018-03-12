# some functions for processing strings

# takes a snippet of text and returns a list of its composite words
# converted to lowercase
# and with extraneous punctuation removed
def tokenize(text):
	text = text.strip() # just in case
	text = text.lower()
	text = text.split()

	newText = [word.strip(" .,!?;:-[]%*()\'\"\n") for word in text]
	newText = [word for word in newText if word is not '']
	# in case that somehow happens

	return newText


# takes a list of words and formats them into a whole string
# removes any words in the "remove" list
# capitalizes the first letter of the snippet
# also any instances of the pronoun 'I'
def finalize(text, remove=[]):
	text = [word for word in text if word not in remove]
	text = [word if word is not 'i' else 'I' for word in text]
	text[0] = text[0].capitalize()

	newText = ' '.join(word for word in text)

	return newText

