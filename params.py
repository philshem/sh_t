#!/usr/bin/env python

''' parameter file for generate_puzzles.py '''

import os

# this many words per game
WORDS_TO_PLAY = 5

# skipping a word costs you this many points
POINTS_SKIP = -1
# correctly solving givey you this many points
POINTS_YES = 5
# incorrect guesses cost you this much
POINTS_NO = 0
# if you guess incorrectly, proceed to the next word
ONE_CHANCE = False

# params for generating the puzzles
# file paths
WORD_LIST_PATH = 'word_lists' + os.sep + 'TWL06.txt'
PUZZLE_DATA_PATH = 'data'

# set minimum word length and total letters used
MIN_WORD_LENGTH = 4
MAX_WORD_LENGTH = 10

DELIM = '\t'
