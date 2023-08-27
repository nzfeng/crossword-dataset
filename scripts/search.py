import re
from utils import *

def find(regex):
	'''
	Return a list of all words that satisfy the given regex pattern.
	'''
	pass

def findSchrodinger(pattern):
	'''
	Ex: ..[DT].. will find pairs of 5-letter words that differ only by their 3rd letter, which can be either a D or T.
	It is assumed the input regex pattern yields fixed length words.
	'''

	# Get all entries in my dataset.
	files = glob.glob('../raw/*.txt', recursive = True)
	all_words = []
	for file in files:
		f = open(file, 'r')
		lines = f.read().splitlines() 
		f.close()
		all_words += lines
	# Standardize and remove duplicates.
	all_words = [standardize(word) for word in all_words]
	all_words = [word for word in all_words if len(word) >= 3]
	all_words = set(all_words)

	pool = []
	for word in all_words:
		if re.fullmatch(pattern, word) == None: continue
		pool.append(word)

	if pool == []: return []
	# get index of wildcard character (warning: this is based on assumptions about the input, not robust to general regex patterns)
	N = len(pool[0])
	idx = 0
	for i in range(N):
		if pattern[i] == "[":
			idx = i
			break

	pool = sorted(pool)
	candidates = []
	while len(pool) > 0:
		word = pool[0]
		# Look through rest of words, and find ones that differ by only one letter.
		partners = [w for w in pool[1:] if sum(a!=b for a,b in zip(word,w)) == 1 and word[idx] != w[idx]]
		for partner in partners:
			candidates.append((word, partner))
		pool = pool[1:]

	return candidates

if __name__=="__main__":

	search = ''
	while True:
		try:
			search = input("Enter search string: ")
		except ValueError:
			print("Sorry, invalid value entered.")
			continue
		else:
			break

	print(findSchrodinger(search))