import sys
from functools import lru_cache

filename = sys.argv[1] if sys.argv[1] else ""

with open(filename, mode="r") as file:
	
	lines = [line.strip() for line in file.readlines()]
	lines[0] = lines[0].replace("S", "|")
	
	numSplits = 0
	for idx, line in enumerate(lines):
		for jdx, c in enumerate(line):

			if c != "|":
				continue
			if idx == len(lines)-1:
				break

			below = lines[idx+1][jdx]
			match(below):
				case ".":
					lines[idx+1] = lines[idx+1][:jdx] + "|" + lines[idx+1][jdx+1:]
				case "^":
					temp = list(lines[idx+1])
					temp[jdx-1] = "|"
					temp[jdx+1] = "|"
					lines[idx+1] = "".join(temp)

					numSplits += 1
	
	@lru_cache(None)
	def dfs(r, c):
		if r not in range(0, len(lines)) or c not in range(0, len(lines[0])):
			return 0
		
		cell = lines[r][c]
		if cell == ".":
			return 0
		if r == len(lines)-1:
			return 1
		
		below = lines[r+1][c]
		if cell == "|":

			if below == "|":
				return dfs(r+1, c)
			if below == "^":
				return dfs(r+1, c-1) + dfs(r+1, c+1)

		return 0
	
	print(dfs(0, lines[0].find("|")))
