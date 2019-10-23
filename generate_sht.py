#!/usr/bin/env python

'''generate words with missing unique letter'''

import params
from datetime import datetime

from collections import defaultdict
import itertools

import os

def main():

	runtime = datetime.now()
 
	word_list = read_all_words()
	print (len(word_list),'total words')

	word_list = clean_all_words(word_list)
	print (len(word_list),'possible words')


	# split all words into dict based on length
	d = defaultdict(list)
	for w in word_list:
		d[len(w)].append(w)

	# Marker for pairs that have not been found yet.
	NOT_FOUND = object()

	# Collection of found pairs x => y. Each item is in one of three states:
	# - y is NOT_FOUND if x has not been seen yet
	# - y is a string if it is the only accepted pair for x
	# - y is None if there is more than one accepted pair for x

	if False:
		for k,w in d.items():
			pairs = defaultdict(lambda: NOT_FOUND)
			print('Running words with',k,'letters')

			for x,y in itertools.combinations(w,2):
				if diff_letters(x,y) == 1:
					if pairs[x] is NOT_FOUND:
						pairs[x] = y
					else:
						pairs[x] = None
					if pairs[y] is NOT_FOUND:
						pairs[y] = x
					else:
						pairs[y] = None

			# Remove None's and change into normal dict.
			pairs = {x: y for x, y in pairs.items() if y}

			#for x, y in pairs.items():
			#	print("Target = {}, Only near matching word = {}".format(x, y))

	with open(params.PUZZLE_DATA_PATH + os.sep + 'puzzles.csv','w') as f:
		# write header to csv
		#f.write('target_word'+params.DELIM+'near_match_word'+'\n')
		
		# loop over dict of words
		pairs = dict()
		result = dict()
		for k,w in d.items():
			print('Running words with',k,'letters')
			#w = ['AAHS','AALS','DAHS','XYZA']
			for x, y in itertools.combinations(w, 2):
				if diff_letters(x, y) == 1:
					pairs.setdefault(x, []).append(y)
					pairs.setdefault(y, []).append(x)
			
			result[k] = [{ "target": key, "match": head, } for key, (head, *tail) in pairs.items() if not tail]
			print('With',k,'letters, there are',len(result[k]),'found results')
		
		# combine values from dicts
		#print(*result.values())
		result = [v for v in result.values() if len(v) > 0][0]
		for item in result:
			f.write(item.get("target") + params.DELIM + item.get("match")+'\n')
		
		print ((datetime.now() - runtime).seconds, 'seconds')

		#print(result)
		#with open(params.PUZZLE_DATA_PATH + os.sep + 'puzzles.json', 'w') as jf:
		#	json.dump(result, jf)


def read_all_words():
	with open(params.WORD_LIST_PATH,'r') as wp:
		words = wp.readlines()

	return words

def clean_all_words(words):
	# trim whitespace and remove short/long words
	words = [w.strip() for w in words if len(w.strip()) >= params.MIN_WORD_LENGTH and len(w.strip()) <= params.MAX_WORD_LENGTH]
	return words

def diff_letters(a,b):
	# https://stackoverflow.com/a/12226874/2327328
	return sum ( a[i] != b[i] for i in range(len(a)) )



if __name__ == "__main__":

	main()
 