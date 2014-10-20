#written and tested in Ubuntu 12.04

import sys, collections, itertools, math
from itertools import product
from datetime import datetime


startTime = datetime.now()
resultPegs = [[0,0],[0,1],[0,2],[0,3],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2],[3,0],[3,1],[4,0]]

#get four digit code
if(len(sys.argv)==1):
	#prompt user typed method
	chars = raw_input("Enter any 6 unique characters (such as \"ABCDEF\"):: ")
	code = raw_input("Enter a 4 character code made up of your chosen 6 characters(such as \"ABDF\"):: ")
else:
	#sys args method
	chars = sys.argv[1]
	code = sys.argv[2]
charList = list(chars)
codeList = list(code)

print "\nGame parameters:"
print "Character set:",chars
print "Code:",code

possibilities=[''.join(p) for p in product(chars, repeat=4)]#remove guessed things only
possibilitiesRemaining=possibilities

guessCnt=0


def chooseGuess ():
	guessTime = datetime.now()
	global possibilities
	global resultPegs
	posLen=len(possibilities)
	resLen=len(resultPegs)

	if len(possibilitiesRemaining)==1:#if there is one possibilty left just pick it
		return possibilitiesRemaining[0]

	possibilityScores=[0]*posLen
	guessScores=[0]*resLen
	for x in range(0,posLen):
		for y in range(0,posLen):
			if(x==y):
				continue
			for z in range(0,resLen):
				if(resultPegs[z]==pegReturn(possibilities[x],possibilities[y])):
					guessScores[z]+=1
		#print guessScores
		possibilityScores[x]=min(guessScores)
		guessScores=[0]*resLen
	#print possibilityScores
	largest = max(possibilityScores)
	for x in range(0,posLen):
		if(possibilityScores[x]==largest and possibilities[x] in possibilitiesRemaining):
			return possibilities[x]

	return possibilityScores.index(max(possibilityScores))
	
		






def pegReturn (pegGuess, answer):
	correctly = len(set(pegGuess) & set(answer))
	incorrectly = sum(1 for v1, v2 in itertools.izip(pegGuess,answer) if v1 == v2)
	return [correctly-incorrectly, incorrectly]#incorrect, correct


def removePossibilities (pegGuess):
	global possibilitiesRemaining
	global code
	possibilitiesRemaining = [x for x in possibilitiesRemaining if pegReturn(pegGuess,code)==pegReturn(pegGuess,x)]
	possibilities.remove(pegGuess)


def guess (theGuess):
	global guessCnt
	guessCnt += 1
	if theGuess==code:
		#win case
		return 1
	else:
		#continue case
		pegColors=pegReturn(theGuess, code)
		print "Guess number", guessCnt,"is", activeGuess
		print "Incorrectly placed pegs:",pegColors[0]
		print "Correctly   placed pegs:",pegColors[1]
		removePossibilities(theGuess)
		print len(possibilitiesRemaining), "possibilities remain\n\n"




if len(code) == 4 and not (set(code) - set(chars)) and len(chars) == 6:
	print "\nLet the guessing begin!\n"
	activeGuess = charList[0]+charList[0]+charList[1]+charList[1]
	while guess(activeGuess)!=1:
		activeGuess=chooseGuess()
	print "\nProgram took",guessCnt, "guesses to get", code
	print "Run Time =",datetime.now()-startTime
	


	print "done"
else:
	print "Malformed input, please try again!"


#print possibilitiesRemaining