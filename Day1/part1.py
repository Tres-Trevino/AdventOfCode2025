

with open("input.txt", mode="r") as file:

	lines = file.readlines()

	numZeroes = 0

	dial = 50
	for line in lines:

		direction = line[0]
		distance = int(line[1:])

		if direction == "R":
			dial += distance
		else:
			dial -= distance

		dial %= 100

		if dial == 0:
			numZeroes += 1

	print(numZeroes)