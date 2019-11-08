#!/usr/bin/env python

'''play sh_t'''

import params

import os
import random
import time
from datetime import datetime
import string

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

	# read pairs of words from source file, defined in params.py
	with open(params.PUZZLE_DATA_PATH,'r') as f:
		data = f.readlines()
	
	# create list of lists (pairs of words)
	word_pairs = []
	for item in data:
		word_pairs.append([x.strip() for x in item.split(params.DELIM)])

	# print status
	print_header(len(word_pairs))

	# random.sample() also shuffles the results
	return random.sample(word_pairs, k=params.WORDS_TO_PLAY)

def play(p):

	points = 0
	for x in p:
		
		raw_original = x[0]
		raw_solution = x[1]

		idx = get_diff(raw_original,raw_solution)

		# special printing for the original word
		pretty_original = uncapitalize(raw_original, idx)
		print('\n'+pretty_original)

		# set variables for while loop
		hint_used = False
		player_turn = True
		guessed_list = []

		while player_turn:
			letter = input('?').upper()

			# user quits
			if len(letter) > 1 and letter in ('!Q'):
				print(make_color('Goodbye',params.color.PURPLE)+'\t'+str(points)+' points')
				exit(0)

			# user skips this word, leave the loop
			elif len(letter) == 0:
				points += params.POINTS_SKIP
				print (make_color('skip',params.color.PURPLE)+'\t'+uncapitalize(raw_solution,idx)+'\t'+str(points)+' points')
				player_turn = False
				continue

			# user wants a hint, but it costs some points
			elif len(letter) > 1 and letter in ('!H') and not hint_used:
				points += params.POINTS_HINT
				hint_list = get_hint(raw_original, raw_solution, idx, guessed_list)
				print(make_color('hint',params.color.PURPLE)+'\t'+' '.join(hint_list)+'\t'+str(points)+' points')
				hint_used = True
				continue

			# hint already used this turn, reprint the hint
			elif len(letter) > 1 and letter in ('!H') and hint_used:
				print(make_color('hint',params.color.PURPLE)+'\t'+' '.join(hint_list))
				continue

			# not a valid letter
			elif len(letter) > 1 or not letter.isalpha():
				print('invalid')
				continue

			# the guessed letter is in the original word
			elif letter == raw_original[idx]:
				print('same letter: '+make_color(letter,params.color.PURPLE)+'\t'+pretty_original)
				continue

			# already guessed that letter
			elif letter in guessed_list:
				print('already guessed: '+make_color(letter,params.color.PURPLE)+'\t'+pretty_original)
				continue
			
			# correct answer, leave loop
			elif raw_solution[idx] == letter:
				points += params.POINTS_YES
				print (make_color('yes',params.color.PURPLE)+'\t'+raw_solution+'\t'+str(points)+' points')
				player_turn = False
			else:
				guessed_list.append(letter)
				points += params.POINTS_NO
				
				print (make_color('no',params.color.PURPLE)+'\t'+pretty_original+'\t'+str(points)+' points')
				if params.ONE_CHANCE:
					player_turn = False
				continue

	return points

def print_header(total_pairs):

	if params.DEBUG:
		return
	# prints instructions
	print('Playing',params.WORDS_TO_PLAY,'words from', total_pairs,'total')
	print(32*'*')
	print('HOW TO PLAY:')
	print('\tMake the only other valid word by guessing the capital letter.')
	print('\t\t','Example:',uncapitalize('count', 3),'becomes',uncapitalize('court', 3))
	
	print('\tType a letter and hit ENTER to play your turn.')
	print('\tIncorrect guesses : ',params.POINTS_NO,'points, but keep trying!')
	print('\tCorrect guesses : ',params.POINTS_YES,'points')
	print('\tHint ENTER to skip a word : ',params.POINTS_SKIP,'points')
	if params.ALLOW_HINT:
		print('\tType',make_color('!h',params.color.GREEN),',and ENTER to get a hint: ',params.POINTS_HINT,'points')
		if params.SHUFFLE_HINT:
			print('\t\t(Hints are randomly shuffled)')
		else:
			print('\t\t(Hints are alphabetically sorted)')
	print('\tType',make_color('!q',params.color.GREEN),'and ENTER to quit')
	print(32*'*')

	return

def get_hint(raw_original, raw_solution, idx, guessed_list):

	hint_list = []
	# add actual answer to hint_list
	hint_list.append(raw_solution[idx])

	ignore_list = list(raw_original[idx]) + list(raw_original) + guessed_list + hint_list
	ignore_list = set(ignore_list)
	if params.DEBUG: print(ignore_list)

	while len(hint_list) < params.HINT_SIZE:
		h = random.choice(string.ascii_uppercase)
		if h not in ignore_list and h not in hint_list:
			hint_list.append(h)
			continue

	if params.DEBUG: print(hint_list)

	# choose how to display hint, random or sorted (set in params.py)
	if params.SHUFFLE_HINT:
		random.shuffle(hint_list)
	else:
		hint_list = sorted(hint_list)

	return hint_list


def make_color(s,start):
	return start + s + params.color.END

def get_diff(a,b):
	return [i for i in range(len(a)) if a[i] != b[i]][0]

def uncapitalize(s, i):

	# returns formatting for target words

	# capitalized target letter
	#return s[:i].lower() + s[i].upper() + s[i+1:].lower()

	# use color class
	return s[:i].lower() + make_color(s[i].upper(), params.color.GREEN) + s[i+1:].lower()
	
if __name__ == "__main__":

	main()
 