#read in alphabet text file, then
#build random number of letters
# then run thru dictionary to cross check
#import matching definitions and print those

#allow to search for word and if its spelled wrong pull words
#with most of the correct letters.
#find similar words from online definition synonims and
#search for those.


#create list of wrong words and dont allow those to be created anymore
import csv
import sys
import time

from random import randint

global wrong
wrong = []
global wordList 
wordList= []



'''
build a word from the constraints given
uses vowels and consonants
Also adds a "u" if there is a "q"
'''


def buildIt(vowel,consonant,dictionary,blackList):

	newWord = ''
	random = randint(3,9)
	alphabet = []
	knownWordsRange = []
	alphabet = vowel + consonant
	dicLength = len(dictionary)-1
	wordLength = len(knownWordsRange)
	ible = "ible"
	able = "able"
	ableLess = 0
	ibleLess = 0
	
	newWordInt = 0
	
		
	########THIS SLOWS DOWN PROCESS HUGELY BUT ALLOWS YOU TO
	########TO CHECK IF WORD IS WRONG BEFORE DOING TO SPELL CHECK
	########AND OTHER PROCESSES
	
	#h = open("wrongWords.txt","r")
	#for line in h:
	#	lines = line.rstrip('\n')
	#	if line not in wrong:
	#		wrong.append(lines)
	
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

		
		if newWord in wrong:
			print("detected wrong word:" + newWord + " Redoing build")
			buildIt(vowel,consonant,dictionary,blackList)
	


	spellCheck(dictionary,newWord,vowel,consonant)

	#start_time = time.time()
	#elapsed_time = time.time() - start_time
	#print(elapsed_time)	


	
'''
Checks the spelling of the parameter with a dictionary
Also checks for common spelling mistakes(ex: ei or ie )
'''



def spellCheck(dictionary,newWord,vowel,consonant):

	
	random = randint(3,4)
	alphabet = []
	knownWordsRange = []
	alphabet = vowel + consonant
	dicLength = len(dictionary)-1
	wordLength = len(knownWordsRange)
	ible = "ible"
	able = "able"
	ableLess = 0
	ibleLess = 0
	
	newWordInt = 0

	if "ie" in newWord:
		if "c" in newWord and "ie" in newWord and newWord.index("c")< newWord.index("i"):
			print("detected spelling issue " + newWord)
			newWord1 = list(newWord)		
			for i in range(len(newWord)):
				if newWord[i] == "i" and newWord[i+1] == "e":
					newWord1[i] = "e"
					newWord1[i+1] = "i"
					newWord = ''.join(newWord1)
		
		if "gh" in newWord and "ie" in newWord and newWord.index("e")<newWord.index("g"):
			print("detected spelling issue " + newWord)
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

	
	
	
	for j in range(dicLength):
		if newWord == dictionary[j]:
			print("MATCH",newWord)
			f = open("knowWords.txt","a")
			#for k in (range(len(knownWordsRange)+1)):
			f.write(newWord+ '\n')
		
	if newWord not in dictionary:
		
		wrongWordLog(newWord)
		#print("this")


'''
Logs if the parameter wrongWord is in the list/array
wrong, if it isnt in wrong then adds it to the list/array
'''
			
	

def wrongWordLog(wrongWord):
	
	if wrongWord not in wrong:
		wrong.append(wrongWord)
		f = open("wrongWords.txt","a")
		f.write(wrongWord + '\n')
		f.close
	
		
'''
Reads in from each of the text files for building words
and the dictionary then adds them to list/array
'''




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
	######LOOP LENGTH
	a1a = 50
	for i in range(a1a):
		buildIt(vowels,consonants,dictionary,wrong)



'''
Finds words in the knowWords text file.  Repeats until user specifies
to stop.  
'''

def findWord(word):
	
	f = open("knowWords.txt","r")
	for line in f:

		lines = line.rstrip('\n')
		if lines not in wordList:
			wordList.append(lines)

	if word in wordList:
		print(word + " in know word list")
	else:
		print(word + " not in list, Try again? (y/n)")
		while True:
			tryAgain = raw_input()
			if tryAgain == "y":
				print("Enter in new word to try")
				try2 = raw_input()
				findWord(try2)
				break
			elif tryAgain == "n":
				print("BYE")
				break
			else:
				print( "Try again? (y/n)")
				







readIn()
print("done")

print("Search for a word already found, Enter word: ")
inWord = raw_input()

findWord(inWord)

#done
#do not loop creating dictionary and all other arrays, takes so much longerrrrrrr
#for real