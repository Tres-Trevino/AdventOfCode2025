

with open("input.txt", mode="r") as file:

	lines = file.readlines()

	numZeroes = 0

	dial = 50
	for line in lines:


		direction = line[0]
		distance = int(line[1:])

		if direction == "R":

			while (distance > 0):
				dial += 1
				dial %= 100
				distance -= 1

				if (dial == 0):
					numZeroes += 1

		else:

			while (distance > 0):
				dial -= 1
				dial %= 100
				distance -= 1

				if (dial == 0):
					numZeroes += 1

		# print(f"Dial: {dial}, nZ: {numZeroes}", end="")
		# input()

	print(numZeroes)
