#!/usr/bin/env python

'''play sh_t'''

import params

import os
import random
import time
from datetime import datetime

def main():

	pzl = read_words()

	runtime = datetime.now()
	points = play(pzl)

	print('\n'*4+'#'*32+'\n'*2)
	print('TOTAL SCORE: '+str(points))
	print()
	print('TOTAL SECONDS:',(datetime.now() - runtime).seconds)
	print()


def read_words():
	with open(params.PUZZLE_DATA_PATH + os.sep + 'puzzles.csv','r') as f:
		data = f.readlines()
	
	word_pairs = []
	for item in data:
		word_pairs.append([x.strip() for x in item.split(params.DELIM)])

	print('Playing',params.WORDS_TO_PLAY,'words from total',len(word_pairs))

	#print(random.choice(word_pairs))
	# random.sample() also shuffles the results
	return random.sample(word_pairs, k=params.WORDS_TO_PLAY)

def play(p):

	points = 0
	for x in p:
		idx = get_diff(x[0],x[1])
		target = uncapitalize(x[0], idx)

		print ('\n'+target)

		while True:
			letter = input('?')

			if len(letter) == 0:
				points += params.POINTS_SKIP
				print ('skip'+'\t'+params.color.GREEN+x[1]+params.color.END+'\t'+str(points)+' points')
				break
			elif len(letter) > 1 or not letter.isalpha():
				print('invalid')
			elif x[1][idx] == letter.upper():
				points += params.POINTS_YES
				print ('yes'+'\t'+x[1]+'\t'+str(points)+' points')
				break
			else:
				points += params.POINTS_NO
				
				print ('no'+'\t'+target+'\t'+str(points)+' points')
				if params.ONE_CHANCE:
					break

	return points

def get_diff(a,b):
	return [i for i in range(len(a)) if a[i] != b[i]][0]

def uncapitalize(s, i):

	# returns formatting for target words

	# capitalized target letter
	#return s[:i].lower() + s[i].upper() + s[i+1:].lower()

	# use color class
	return s[:i].lower() + params.color.GREEN + s[i].upper() + params.color.END + s[i+1:].lower()
	
if __name__ == "__main__":

	main()
 