# import packages to extend python ( just like we extend sublime, or Atom, or VSCode)
from random import randint

# [] => this is an array, an array is a special type of container that can hold multiple items
# arrays are indexed (their cotents get assigned a number)
# the index always starts at 0
choices = ["rock", "paper", "scissors"]

# this is the player choice
player = input("Choose rock, paper or scissors: ")

# this will be the AI choice -> a random pick from the choices array
computer = choices [randint(0, 2)]

# check to see what the user input

#print outputs whatever is in the round brackets -> in this case player to the comnmand prompt window
print("User chose: " + player
)

# validate that the random choice worked for the AI
print("AI chose: " + computer)

if (computer == player
):
	print("tie")

elif (computer == "rock")
	if (player == "scissors")
		print("You lose!")
	else:
		print("You Win!")

elif (computer == "paper")
	if (player == "scissors")
		print("You Win!")
	else:
		print("You Lose!")

# needs work
elif (computer == "paper")
	if (player == "scissors")
		print("You Win!")
	else:
		print("You Lose!")