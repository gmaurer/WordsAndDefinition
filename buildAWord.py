#read in alphabet text file, then
#build random number of letters
# then run thru dictionary to cross check
#import matching definitions and print those

#allow to search for word and if its spelled wrong pull words
#with most of the correct letters.
#find similar words from online definition synonims and
#search for those.
import csv
import sys
from random import randint


def buildIt(alphabet,dictionary):
	newWord = ''
	random = randint(3,5)
	
	for i in range(random):
		dicRandom = randint(0,(len(alphabet)-1))
		newWord+= alphabet[dicRandom]
	
	dicLength = len(dictionary)-1
	word = "hobab"
	print newWord
	for j in range(dicLength):
		if newWord == dictionary[j]:
			print("MATCH",newWord)



def readIn():
	alphabet = []
	dictionary = []

	f = open("alphabet.txt","r")
	for line in f:
		lines = line.rstrip('\n')

		alphabet.append(lines)
		
	g = open("dictionary.txt","r")
	for line in g:
		lines = line.rstrip('\n')

		dictionary.append(lines)


	buildIt(alphabet,dictionary)



readIn()

#done