#written and tested in Ubuntu 12.04


import sys, collections, itertools, math
from itertools import product
from datetime import datetime



from PyQt4 import QtCore, QtGui

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	_fromUtf8 = lambda s: s

class Ui_Mastermind(object):

	
	def setupUi(self, Mastermind):
		Mastermind.setObjectName(_fromUtf8("Mastermind"))
		Mastermind.resize(250, 374)
		Mastermind.setFixedSize(250, 374)
		self.label_2 = QtGui.QLabel(Mastermind)
		self.label_2.setGeometry(QtCore.QRect(150, 350, 101, 17))
		self.label_2.setObjectName(_fromUtf8("label_2"))
		self.verticalLayoutWidget_2 = QtGui.QWidget(Mastermind)
		self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 252, 341))
		self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
		self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
		self.verticalLayout_3.setMargin(0)
		self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
		self.verticalLayout_2 = QtGui.QVBoxLayout()
		self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
		self.horizontalLayout_2 = QtGui.QHBoxLayout()
		self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
		self.label = QtGui.QLabel(self.verticalLayoutWidget_2)
		self.label.setObjectName(_fromUtf8("label"))
		self.horizontalLayout_2.addWidget(self.label)
		self.lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_2)
		self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
		self.horizontalLayout_2.addWidget(self.lineEdit)
		self.verticalLayout_2.addLayout(self.horizontalLayout_2)
		self.horizontalLayout = QtGui.QHBoxLayout()
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		self.label_3 = QtGui.QLabel(self.verticalLayoutWidget_2)
		self.label_3.setObjectName(_fromUtf8("label_3"))
		self.horizontalLayout.addWidget(self.label_3)
		self.lineEdit_2 = QtGui.QLineEdit(self.verticalLayoutWidget_2)
		self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
		self.horizontalLayout.addWidget(self.lineEdit_2)
		self.verticalLayout_2.addLayout(self.horizontalLayout)
		self.verticalLayout_3.addLayout(self.verticalLayout_2)
		self.scrollArea = QtGui.QScrollArea(self.verticalLayoutWidget_2)
		self.scrollArea.setWidgetResizable(True)
		self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
		self.scrollAreaWidgetContents = QtGui.QWidget()
		self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 248, 232))
		self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
		self.plainTextEdit = QtGui.QPlainTextEdit(self.scrollAreaWidgetContents)
		self.plainTextEdit.setGeometry(QtCore.QRect(0, 0, 248, 232))
		self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
		self.plainTextEdit.setReadOnly(True)#manualy generated line
		self.scrollArea.setWidget(self.scrollAreaWidgetContents)
		self.verticalLayout_3.addWidget(self.scrollArea)
		self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget_2)
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		self.pushButton.clicked.connect(self.playGame)#manualy generated line
		self.verticalLayout_3.addWidget(self.pushButton)
		self.retranslateUi(Mastermind)
		QtCore.QMetaObject.connectSlotsByName(Mastermind)

	def retranslateUi(self, Mastermind):
		Mastermind.setWindowTitle(QtGui.QApplication.translate("Mastermind", "Mastermind", None, QtGui.QApplication.UnicodeUTF8))
		self.label_2.setText(QtGui.QApplication.translate("Mastermind", "By Ian Lovrich", None, QtGui.QApplication.UnicodeUTF8))
		self.label.setText(QtGui.QApplication.translate("Mastermind", "Enter any 6 letters here ", None, QtGui.QApplication.UnicodeUTF8))
		self.lineEdit.setText(QtGui.QApplication.translate("Mastermind", "ABCDEF", None, QtGui.QApplication.UnicodeUTF8))
		self.label_3.setText(QtGui.QApplication.translate("Mastermind", "Enter 4 of your letters here", None, QtGui.QApplication.UnicodeUTF8))
		self.lineEdit_2.setText(QtGui.QApplication.translate("Mastermind", "ABED", None, QtGui.QApplication.UnicodeUTF8))
		self.pushButton.setText(QtGui.QApplication.translate("Mastermind", "Begin!", None, QtGui.QApplication.UnicodeUTF8))




	def write(self,txt):
		print txt
		s = QtCore.QString(txt+"\n")
		q = self.plainTextEdit.toPlainText().append(s)
		self.plainTextEdit.setPlainText(q)
		
		self.plainTextEdit.moveCursor(QtGui.QTextCursor.End)
		self.plainTextEdit.ensureCursorVisible()

		QtGui.QApplication.processEvents()


	def chooseGuess (self,possibilities,possibilitiesRemaining):
		resultPegs = [[0,0],[0,1],[0,2],[0,3],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2],[3,0],[3,1],[4,0]]
		posLen=len(possibilities)
		resLen=13#len(resultPegs)

		if len(possibilitiesRemaining)==1:#if there is one possibilty left just pick it
			return possibilitiesRemaining[0]

		possibilityScores=[0]*posLen
		guessScores=[0]*resLen


		for x in range(0,posLen):
			for y in range(0,posLen):
				if(x==y):
					continue
				for z in range(0,resLen):
					if(resultPegs[z]==self.pegReturn(possibilities[x],possibilities[y])):
						guessScores[z]+=1
			possibilityScores[x]=min(guessScores)
			guessScores=[0]*resLen
		largest = max(possibilityScores)


		for x in range(0,posLen):
			if(possibilityScores[x]==largest and possibilities[x] in possibilitiesRemaining):
				return possibilities[x]

		return possibilityScores.index(max(possibilityScores))
		

	def pegReturn(self,activeGuess,answer):
		correct = sum([1 for (a, b) in zip(answer, activeGuess) if a == b])

		actual = [a for (a, b) in zip(answer, activeGuess) if a != b]
		guess = [b for (a, b) in zip(answer, activeGuess) if a != b]

		close = 0
		for possible in guess:
			if possible in actual:
				del actual[actual.index(possible)]
				close += 1

		return[correct, close]


	def removePossibilities (self,activeGuess,pegColors,possibilitiesRemaining,possibilities):
		possibilitiesRemaining = [x for x in possibilitiesRemaining if pegColors==self.pegReturn(activeGuess,x)]
		possibilities.remove(activeGuess)
		return possibilitiesRemaining


	def playGame(self):
		#self.write("playGame")
		if(len(sys.argv)==1):
			chars = str (ui.lineEdit.text())
			code = str (ui.lineEdit_2.text())
		else:
			chars = sys.argv[1]
			code = sys.argv[2]


		startTime = datetime.now()

		charList = list(chars)
		codeList = list(code)

		self.write("\nGame parameters:") 
		self.write("Character set: "+chars)
		self.write("Code: "+code)

		possibilities=[''.join(p) for p in product(chars, repeat=4)]#remove guessed things only
		possibilitiesRemaining=possibilities

		if len(code) == 4 and not (set(code) - set(chars)) and len(chars) == 6:
			self.write("\nLet the guessing begin!\n(Each guess should take roughly 1-2 minutes)")
			activeGuess = charList[0]+charList[0]+charList[1]+charList[1]

			guessCnt=0
			while activeGuess!=code:
				guessCnt += 1
				pegColors = self.pegReturn(activeGuess, code)
				self.write( "\n\nGuess number " + str(guessCnt) + " is " + activeGuess)
				self.write( "Correctly placed pegs: "+str(pegColors[0]))
				self.write( "Closely placed pegs: "+str(pegColors[1]))
				possibilitiesRemaining = self.removePossibilities(activeGuess,pegColors,possibilitiesRemaining,possibilities)
				self.write( str(len(possibilitiesRemaining))+ " possibilities remain")
				activeGuess=self.chooseGuess(possibilities,possibilitiesRemaining)

			self.write("\nGame Complete!")
			self.write( "Program took " + str(guessCnt) + " guesses to get " + code)
			self.write( "Run Time = "+str(datetime.now()-startTime))
			if(len(sys.argv)==1): self.pushButton.setText(QtGui.QApplication.translate("Mastermind", "Play Again!", None, QtGui.QApplication.UnicodeUTF8))

		else:
			self.write( "Malformed input, please try again!")


#get four digit code
if(len(sys.argv)==1):
	#GUI method
	app = QtGui.QApplication(sys.argv)
	Dialog = QtGui.QDialog()
	ui = Ui_Mastermind()
	ui.setupUi(Dialog)
	Dialog.show()
else:
	#sys args method
	app = QtGui.QApplication(sys.argv)
	Dialog = QtGui.QDialog()
	ui = Ui_Mastermind()
	ui.setupUi(Dialog)
	ui.playGame()



if(len(sys.argv)==1): sys.exit(app.exec_())