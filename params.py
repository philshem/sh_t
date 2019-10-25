#!/usr/bin/env python

''' parameter file for generate_puzzles.py '''

# this many words per game
WORDS_TO_PLAY = 5

# skipping a word costs you this many points
POINTS_SKIP = -3
# correctly solving gives you this many points
POINTS_YES = 5
# incorrect guesses cost you this much
POINTS_NO = -1
# if you guess incorrectly, proceed to the next word
ONE_CHANCE = False

# set min/max word length
MIN_WORD_LENGTH = 4
MAX_WORD_LENGTH = 10

# for formatting the target word
# https://stackoverflow.com/a/17303428/2327328
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# params for generating the puzzles
import os
# file paths
WORD_LIST_PATH = 'word_lists' + os.sep + 'TWL06.txt'
PUZZLE_DATA_PATH = 'data' + os.sep + 'puzzles.csv'
# debugging
#PUZZLE_DATA_PATH = 'data' + os.sep + 'debug.puzzles.csv'


# delimiter for data csv file
DELIM = '\t'
