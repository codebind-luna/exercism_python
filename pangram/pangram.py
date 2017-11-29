import string

def is_pangram(sentence):
	alphabets = string.ascii_lowercase 
	sentence  = sentence.replace(' ', '').replace('_', '').lower()
	for char in alphabets:
		if char not in sentence:
			return False
	return True

