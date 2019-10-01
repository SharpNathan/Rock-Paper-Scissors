# Nathan Sharp
# Rock Paper Scissors
# added a comment
#Variables
import random

pScore = 0
cScore = 0
ties = 0
computerChoices = ["r","p","s"]

# Final Score
def printScore():
	# write message
	print("The score is: ")
	# write pScore
	print(pName + ": " + str(pScore))
	# write cScore
	print("Computer: " + str(cScore))
	# write ties
	print("Ties: " + str(ties))

# Welcome message
print("Welcome to rock paper scissors! ")
# Prompt for player name
pName = input("What is your name? ")
# Game loop
# Make a forever loop
while True:
	# Print current score
	printScore()
	# Prompt for choice (rock paper scissors quit)
	pChoice = input("Enter r (Rock), p (Paper), s (Scissors), or q (Quit): ")
	# deal with q
	if pChoice == "q":
		print("The final scores are:")
		# write pScore
		print(pName + ": " + str(pScore))
		# write cScore
		print("Computer: " + str(cScore))
		# write ties
		print("Ties: " + str(ties))
		break
	# Get cpu choice
	cChoice = random.choice(computerChoices)
	# compare for player r
	if pChoice == "r":
		print(pName + " picked rock")
		# if cpu is r
		if cChoice == "r":
			print("Computer picked rock")
			print("Tie")
			ties = ties + 1
		# if cpu is p
		elif cChoice == "p":
			print("Computer picked paper")
			print("Computer wins this round")
			cScore = cScore + 1
		# if cpu is s
		else:
			print("Computer picked scissors")
			print(pName + "wins this round")
			pScore = pScore + 1
	# compare for player p
	elif pChoice == "p":
		print(pName + " picked paper")
		# if cpu is r
		if cChoice == "r":
			print("Computer picked rock")
			print(pName + " wins this round")
			pScore = pScore + 1
		# if cpu is p
		elif cChoice == "p":
			print("Computer picked paper")
			print("Tie")
			ties = ties + 1
		# if cpu is s
		else:
			print("Computer picked scissors")
			print("Computer wins this round")
			cScore = cScore + 1
	# compare for player s
	elif pChoice == "s":
		print(pName + " picked scissors")
		# if cpu is r
		if cChoice == "r":
			print("Computer picked rock")
			print("Computer wins this round")
			cScore = cScore + 1
		# if cpu is p
		elif cChoice == "p":
			print("Computer picked paper")
			print(pName + " wins this round")
			pScore = pScore + 1
		# if cpu is s
		else:
			print("Computer picked scissors")
			print("Tie")
			ties = ties + 1
	# deal with entering anything else
	else:
		pass