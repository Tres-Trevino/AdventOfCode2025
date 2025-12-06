import sys
from functools import reduce

filename = sys.argv[1] if sys.argv[1] else ""

def add(a, b):
	return a+b
def mul(a, b):
	return a*b

with open(filename, mode="r") as file:
	
	lines = [x.strip() for x in file.readlines()]

	lines = [line.split() for line in lines if line.split(" ") != ""]

	operands = lines[len(lines)-1]
	lines.pop(len(lines)-1)


	total = 0

	for i in range(len(lines[0])):

		fn = add if operands[i] == "+" else mul
		accumulate = 0 if operands[i] == "+" else 1

		arguments = [int(lines[x][i]) for x in range(len(lines))]
		total += reduce(fn, arguments)


	print(total)