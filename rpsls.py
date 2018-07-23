import random
import checkWin as c
import os

gameTwo = ('ROCK', 'PAPER', 'SCISSORS', 'LIZARD', 'SPOCK');


def playRPS(maxGames):
	uWin, cWin, gameRound = 0, 0, 1;
	gameCalc = (maxGames * (1 / 2))
	checkWin = True
	winTrue = checkWin
	while winTrue == True:
		computerChoice = random.randint(0,4)
		print("")
		print("0 = Rock")
		print("1 = Paper")
		print("2 = Scissors")
		print("3 = Lizard")
		print("4 = Spock")
		print("Round: {2} of {4} Score: {0} to {1} Debug: {3} {5} {6} ".format( uWin, cWin, gameRound, computerChoice, maxGames, gameCalc, winTrue ))
		while True:
			try:
				userChoice = int(input("[0 - 4], [99 to Quit]: "))
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
			elif computerChoice == 2:
				print("You Win, paper smashes scissors")
				uWin += 1;
			elif computerChoice == 3:
				print("You Win, rock crushes lizard")
				uWin += 1;
			else:					#computerChoice = 4
				print("You Lose, Spock vaporizes rock")
				cWin += 1;
		elif userChoice == 1:
			if computerChoice == 0:
				print("You Win, paper covers rock")
				uWin += 1;
			elif computerChoice == 2:
				print("You Lose, scissors cuts paper")
				cWin += 1;
			elif computerChoice == 3:
				print("You Lose, lizard eats paper")
				cWin += 1;
			else: 				#computerChoice == 4:
				print("You Win, paper disproves Spock")
				uWin += 1;
		elif userChoice == 2:
			if computerChoice == 0:
				print("You Lose, rock crushes scissors")
				cWin += 1;
			elif computerChoice == 1:
				print("You Win, scissors cuts paper")
				uWin += 1;
			elif computerChoice == 3:
				print("You Win, scissors decapitates lizard")
				uWin += 1;
			else:				# computerChoice == 4:
				print("You Lose, Spock crushes scissors")
				cWin += 1;
		elif userChoice == 3:
			if computerChoice == 0:
				print("You Lose, rock crushes lizard")
				cWin += 1;
			elif computerChoice == 1:
				print("You Win, lizard eats paper")
				uWin += 1;
			elif computerChoice == 2:
				print("You Lose, scissors decapitates lizard")
				cWin += 1;
			else:				# computerChoice == 4:
				print("You Win, Lizard poisons Spock")
				uWin += 1;
		elif userChoice == 4:
			if computerChoice == 0:
				print("You Win, Spock Vaporizes rock")
				uWin += 1;
			elif computerChoice == 1:
				print("You Lose, paper disproves Spock")
				cWin += 1;
			elif computerChoice == 2:
				print("You Win, Spock crushes scissors")
				uWin += 1;
			else:				# computerChoice == 3:
				print("You Lose, lizard poisons Spock")
				cWin += 1;
		elif userChoice == 99:
			break;
		else:
			print("Invalid choice, try again.")
		gameRound += 1
		winTrue = c.checkWin(uWin, cWin, gameCalc)

#Rock Paper Scissors Menu
def rpsls():
	os.system('clear')
	maxGames = 0;
	rpsLoop = True;
	while rpsLoop:
		print("Now Playing: ")
		print(gameTwo[0:5])
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
			