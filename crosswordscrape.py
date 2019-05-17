#!/usr/bin/python

import string
import re
import requests 
import os
import sys
import random
import numpy

class CharBlock(object):
	def __init__(self):
		self.targetChar = None
		self.indexDisplay = ""
		self.value = "-"

class WordClue(object):
	def __init__(self, word, clue):
		self.word = word
		self.clue = clue

def is_valid_board(board):
	blankCount = 0
	x = 0
	while x < 15:
		y = 0
		while y < 15:
			if board[x, y] == None:
				blankCount += 1
			y += 1
		x += 1
	
	if blankCount > 37:
		return False
	else:
		return True

def placeWord(word, clue, x, y, vertical, grid) :
	wordPlaced = False
	if vertical == True:
		if len(word) + x < GRID_HEIGHT:
			i = 0
			while i < len(word):
				grid[x + i][y].targetChar = word[i]
			wordPlaced = True
	else:
		if len(word) + y < GRID_WIDTH:
			i = 0
			while i < len(word):
				grid[x][y + i].targetChar = word[i]
			wordPlaced = True
	if wordPlaced == True
		currentIndex = len(ACTIVE_WORDS)
		

		
arguments = len(sys.argv) - 1 
if arguments == 0:
	NUM_WORDS = 20; #we will use 20 by default
else:
	NUM_WORDS = int(sys.argv[1])
	
print ("Creating a Crossword with " + str(NUM_WORDS) + " Words")
WORD_POOL_NUM = NUM_WORDS * 2
#however we are going to grab a pool of double that..	
exists = os.path.isfile('words.txt')
if exists:
    # Store configuration file values
	file = open("words.txt", "r")
	WORDS = file.read().upper().splitlines();
	file.close()
else:
    # Keep presets
	word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
	response = requests.get(word_site)
	file = open("words.txt", "w")
	file.write(response.text)
	WORDS = file.read().upper().splitlines();
	file.close()
	
RAW_WORDS = random.sample(WORDS, WORD_POOL_NUM)
print(RAW_WORDS)
RAW_WORDS.sort(key = len, reverse=True)
print(RAW_WORDS)

global WORD_INTERSECTIONS
WORD_INTERSECTIONS = {}

global EMPTY_CHAR
EMPTY_CHAR = None

global ACTIVE_WORDS
ACTIVE_WORDS = []

RANDOM_WORD = "" 

ACROSS_CLUES = {}
DOWN_CLUES = {}

ACROSS_ANSWERS = {}
DOWN_ANSWERS = {}

global GRID_WIDTH
GRID_WIDTH = 15
global GRID_HEIGHT
GRID_HEIGHT = 15

global WORD_ARRAY
WORD_ARRAY = []

LIST_WORDS = list(RAW_WORDS)
for word in LIST_WORDS:
	if len(word) > 14: 
		print(word + " This word is longer than 14")
		RAW_WORDS.remove(word)
	else:
		RANDOM_WORD = word
		INTERSECTIONS = []
		for check_word in RAW_WORDS:
			if word is not check_word:
				WORD_INT = ( check_word, frozenset(word).intersection(check_word) )
				INTERSECTIONS.append(WORD_INT)
		TUPLE_INTERSECTIONS = tuple(INTERSECTIONS)
		WORD_INTERSECTIONS[word] = TUPLE_INTERSECTIONS
		WORD_ARRAY.append(WordClue(word, "Test Clue"))
	
#Creating a blank board 15x15
CROSSWORD_BOARD = numpy.full((15, 15), CharBlock())

print(WORD_ARRAY[0].word)

#We are going to place the longest word in the first slot.
FIRST_WORD = RAW_WORDS[0]
print(FIRST_WORD)
k = 0
for c in FIRST_WORD:
	CROSSWORD_BOARD[0, k] = c
	k += 1
ACTIVE_WORDS.append(FIRST_WORD)
ACROSS_ANSWERS["1"] = FIRST_WORD
print(CROSSWORD_BOARD)
print(ACTIVE_WORDS)
print(ACROSS_ANSWERS)
print(is_valid_board(CROSSWORD_BOARD))
			

			



		
				
				
