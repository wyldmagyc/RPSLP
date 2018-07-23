import sys
import rps
import rpsls
import os
from datetime import datetime as d

startTimer = d.now();

#create Menu
def printMenu():
	os.system('clear')
	print("What game would you like to play?")
	print("1 - Rock, Paper, Scissors")
	print("2 - Rock, Paper, Scissors, Lizard, Spock")
	print("99 - Exit")

menuLoop = True;
	
def mainMenu():						#Will keep looping until loop = False
	startTimer
	while menuLoop:
		printMenu()					#display Menu
		while True:
			try:
				menuChoice = int(input("Enter your choice [1-2]: "))
				break
			except:
				print("Invalid Option")

		if menuChoice == 1:
			os.system('clear')
			rps.rps()				#call rock paper scissors
		elif menuChoice == 2:
			os.system('clear')
			rpsls.rpsls()				#call rock paper scissors lizard spock
		elif menuChoice == 99:
			os.system('clear')
			print("Made a clean get-away")
			print("Total Time played : {0}".format(d.now() - startTimer)) 
			sys.exit(0)
		else:
			print("Invalid Choice")