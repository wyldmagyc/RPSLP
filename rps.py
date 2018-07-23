import random
import checkWin as c
import os

#Initialize game
gameOne = ('ROCK', 'PAPER', 'SCISSORS');

def playRPS(maxGames):
	uWin, cWin, gameRound = 0, 0, 1;
	gameCalc = (maxGames * (1 / 2))
	checkWin = True
	winTrue = checkWin
	while winTrue == True:
		computerChoice = random.randint(0,2)
		print("")
		print("0 = Rock")
		print("1 = Paper")
		print("2 = Scissors")
		print("Round: {2} of {4} Score: {0} to {1} ".format( uWin, cWin, gameRound, computerChoice, maxGames, gameCalc, winTrue ))
		while True:
			try:
				userChoice = int(input("[0 - 2], [99 to Quit]: "))
				break
			except:
				print("Invalid choice")

		if userChoice == computerChoice:
			print("Tie. Try again")
			continue
		if userChoice == 0:
			if computerChoice == 1:
				print("You Lose, paper covers rock")
				cWin += 1;
			else:
				print("You Win, paper smashes scissors")
				uWin += 1;
		elif userChoice == 1:
			if computerChoice == 0:
				print("You Win, paper covers rock")
				uWin += 1;
			else:
				print("You Lose, scissors cuts paper")
				cWin += 1;
		elif userChoice == 2:
			if computerChoice == 0:
				print("You Lose, rock crushes scissors")
				cWin += 1;
			else:
				print("You Win, scissors cuts paper")
				uWin += 1;
		elif userChoice == 99:
			break;
		else:
			print("Invalid choice, try again.")
		gameRound += 1
		winTrue = c.checkWin(uWin, cWin, gameCalc)

#Rock Paper Scissors Menu
def rps():
	os.system('clear')
	maxGames = 0;
	rpsLoop = True;
	while rpsLoop:
		print("Now Playing: ")
		print(gameOne[0:3])
		print("")
		print("How many games would you like to play? [1 - 9]")
		while True:
			try:
				maxGames = int(input("[1 - 9], [99 to quit]: "))
				break
			except:
				print("Invalid Option")

		if maxGames >=1 and maxGames <= 9:
			playRPS(maxGames)
		elif maxGames == 99:
			rpsLoop = False;
		else:
			print("Invalid Choice")
			