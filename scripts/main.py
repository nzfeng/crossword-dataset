from utils import *
import argparse

def main(filepath):
	'''
	Standardize the given file of words.
	'''
	dedupAndSort(filepath)

if __name__=="__main__":
	parser = argparse.ArgumentParser(description='De-duplicate and alphabetize word list.')
	parser.add_argument('filepath', type=str, help='Filepath to input .txt file.')

	args = parser.parse_args()
	main(args.filepath)