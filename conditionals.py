# set up a variable, check it's value, and then go down some different paths depending on the outcome
temperature = int(input("input a value between 0 and 100: "))


if (temperature <= 4)
	# water is frozen
	print("water's state is a solid (ice)")
elif (temperature < 100):
	print("water's state is a liquid")
else:
	# water is boiling, so it's steam
	print("water is vapor") 