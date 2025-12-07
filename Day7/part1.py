import sys

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

	print(numSplits)
