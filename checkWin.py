#Check for game win
def checkWin(uWin, cWin, gameCalc):
	if uWin > gameCalc:
		print("You Win! The score is: {0} to {1}".format( uWin, cWin ))
		return False
	if cWin > gameCalc:
		print("You Lose! The score is: {0} to {1}".format( uWin, cWin ))
		return False
	else:
		return True