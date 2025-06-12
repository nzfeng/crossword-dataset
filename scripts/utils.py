import numpy as np
import glob
import sys
import time
import os
#from itertools import chain

#import nltk
#nltk.download('wordnet')
#nltk.download('omw-1.4')
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('maxent_ne_chunker')
#nltk.download('words')
#from nltk.tokenize import SpaceTokenizer
#from nltk.corpus import wordnet as wn

WANTED_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

##### A bunch of basic utility functions.

def depunctuate(string):
	'''
	Remove all non-alphabetical characters from the given string.
	'''
	newWord = ''.join(i for i in string if i in WANTED_CHARS)
	return newWord

def removeUnwantedChars(string, unwanted_chars="_'.,/;[]\\-=`~_+{}|:<>?()@#$%^&* "):
	'''
	Remove all instances of each char in <unwanted_chars> from <word>.
	<unwanted_chars> can be either a string or a list.
	'''
	newWord = ''.join(i for i in string if not i in unwanted_chars)
	return newWord


def isAllDigits(string):
	'''
	Return True if the word consists solely of numbers.
	'''
	for letter in string:
		if letter not in "0123456789":
			return False
	return True


def standardize(string):
	return depunctuate(string.upper());


def buildStandardizedDictAndWordlist(wordlist):
	'''
	Build map from standardized versions of entries to the original entries.
	Return this map (a dict), and a list of the standardized entries.
	'''

	# Build map from standardized versions of entries to the original entries.
	wordMap = {}
	stdList = []
	for word in wordlist:
		std = standardize(word)
		wordMap[std] = word
		stdList.append(std)

	return (wordMap, stdList)


def mapFromStandardizedWordist(stdList, wordMap):
	'''
	Given a wordlist <stdList> of standardized entries, and a 
	dictionary <wordMap> mapping standardized entries to their original entries,
	return the mapped <stdList>.
	'''

	wordSet = []
	for word in stdList:
		wordSet.append(wordMap[word])

	return wordSet


def removeDuplicates(wordlist):
	'''
	Remove duplicates from the given wordlist, where duplicates are determined by 
	comparing standardized (de-puncutated) versions; preserve the original format of the word. 
	'''

	# Build map from standardized versions of entries to the original entries.
	(wordMap, stdList) = buildStandardizedDictAndWordlist(wordlist)

	# Remove duplicates.
	stdList = set(stdList)

	# Return original versions of entries.
	return mapFromStandardizedWordist(stdList, wordMap)


def removeEntries(wordlist, setlist):
	'''
	Subtract elements in <setlist> from <wordlist>. Preserve the original formatting of the word.
	'''

	# Lists are passed in by reference in Python...
	stdSetlist = [standardize(word) for word in setlist]

	# Build map from standardized versions of entries to the original entries.
	(wordMap, stdList) = buildStandardizedDictAndWordlist(wordlist)

	# Remove elements.
	newList = set(stdList) - set(stdSetlist)

	# Return original versions of entries.
	wordSet = mapFromStandardizedWordist(newList, wordMap)

	return wordSet


##### I/O


def readEntries(filepath):
	'''
	Read the newline-separated entries in the given .txt file.
	Return a list of these entries, preserving their original forms.
	'''

	f = open(filepath, 'r')
	words = f.read().splitlines() 
	f.close()
	
	return words


def saveMsFitWordlists():
	'''
	This is a MsFit-specific function.
	Outputs the .txt files for MsFit, separated by wordlength and in standardized form.
	'''
	# files = glob.glob('../*.txt', recursive = True) # this no longer seems to work in newer versions of Python
	files = glob.glob('../raw/*.txt', recursive = True)

	all_words = []
	for file in files:
		f = open(file, 'r')
		lines = f.read().splitlines() 
		f.close()
		all_words += lines

	print("Total number of words: %d" %len(all_words))

	all_words = [depunctuate(word).upper() for word in all_words]
	all_words = [word for word in all_words if len(word) >= 3]
	all_words = set(all_words)
	print("Number of unique words: %d" %len(all_words))

	# No categories for now. Just sort by wordlength.
	wordLengths = [len(word) for word in all_words]
	minLength = min(wordLengths)
	maxLength = max(wordLengths)
	print("min length: %d\t max length: %d" %(minLength,maxLength))

	for i in range(minLength,maxLength+1):
		n = len([word for word in all_words if len(word)==i])
		print("# of words of length %d: %d" %(i, n))

	# Save words.
	for i in range(minLength, maxLength+1):
		filename = "../words_%d.txt" %i
		words = [word for word in all_words if len(word)==i]

		with open(filename, 'w') as f:
			for word in words:
				f.write(word)
				f.write("\n")


##### Clean word lists.

def dedupAndSort(filepath):
	'''
	Read in the given .txt file; 
	De-duplicate entries, and write an alphabetized copy of the file.
	'''

	entries = readEntries(filepath)
	# Build map from standardized versions of entries to the original entries.
	(wordMap, stdList) = buildStandardizedDictAndWordlist(entries)
	# Remove duplicates.
	stdList = set(stdList)
	stdList = sorted(stdList) # alphabetized

	# Get file extension.
	splitPath = os.path.splitext(filepath)
	ext = splitPath[1]
	copyPath = splitPath[0] + "_sorted" + ext

	# Write to new file.
	with open(copyPath, 'w') as f:
		for word in stdList:
			if (len(word) >= 3):
				f.write(wordMap[word]) # write original entry
				f.write("\n")