import sys
filename = sys.argv[1] if sys.argv[1] else ""

with open(filename, mode="r") as file:
	
	lines = file.readlines()

	totalCount = 0

	for idx, line in enumerate(lines):
		for idy, char in enumerate(line.strip()):

			if char != "@":
				continue

			numAdjacent = 0

			for dx in [-1, 0, 1]:
				for dy in [-1, 0, 1]:

					if (dx, dy) == (0, 0):
						continue
					if (idx+dx) in [-1, len(lines)] or (idy+dy) in [-1, len(line.strip())]:
						continue

					numAdjacent += 1 if lines[idx+dx][idy+dy] == '@' else 0
			
			if numAdjacent < 4:
				totalCount += 1

	print(totalCount)