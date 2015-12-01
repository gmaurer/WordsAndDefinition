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


def buildIt(vowel,consonant,dictionary):
	newWord = ''
	random = randint(3,9)
	alphabet = []
	alphabet = vowel + consonant
	dicLength = len(dictionary)-1
	ible = "ible"
	able = "able"
	ableLess = 0
	ibleLess = 0
	
	for i in range(random):

		vOrC = randint(0,3)
		if vOrC%3 == 0:
			vRandom = randint(0,(len(vowel)-1))
			newWord += vowel[vRandom]
		else:
			cRandom = randint(0,(len(consonant)-1))
			newWord += consonant[cRandom]
			if consonant[cRandom] == "q":
				newWord += vowel[4]

	if "c" in newWord and "ie" in newWord:
		print("detected spelling issue")
		newWord1 = list(newWord)		
		for i in range(len(newWord)):
			if newWord[i] == "i" and newWord[i+1] == "e":
				newWord1[i] = "e"
				newWord1[i+1] = "i"
				newWord = ''.join(newWord1)
	
	if "gh" in newWord and "ie" in newWord:
		print("detected spelling issue")
		newWord1 = list(newWord)		
		for i in range(len(newWord)):
			if newWord[i] == "i" and newWord[i+1] == "e":
				newWord1[i] = "e"
				newWord1[i+1] = "i"
				newWord = ''.join(newWord1)
	
	if newWord.endswith("able"):
		newWord1 = newWord[:-4]
		for j in range(dicLength):
			if newWord1 == dictionary[j]:
				ableLess = 1
				
		if ableLess == 0:
			newWord = newWord1 + ible
		ableLess = 0

	if newWord.endswith("ible"):
		newWord1 = newWord[:-4]
		for j in range(dicLength):
			if newWord1 == dictionary[j]:
				ibleLess = 1
				
		if ibleLess == 1:
			newWord = newWord1 + able
		ibleLess = 0



		


	
	
	print newWord
	for j in range(dicLength):
		if newWord == dictionary[j]:
			print("MATCH",newWord)



def readIn():
	vowels = []
	consonants = []
	dictionary = []

	f = open("vowels.txt","r")
	for line in f:
		lines = line.rstrip('\n')

		vowels.append(lines)
		
	g = open("dictionary.txt","r")
	for line in g:
		lines = line.rstrip('\n')

		dictionary.append(lines)

	h = open("consonants.txt","r")
	for line in h:
		lines = line.rstrip('\n')

		consonants.append(lines)


	buildIt(vowels,consonants,dictionary)





readIn()

#done
#for real