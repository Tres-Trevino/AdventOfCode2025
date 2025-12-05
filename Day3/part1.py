import sys
import textwrap
import math

filename = sys.argv[1] if sys.argv[1] else ""

with open(filename, mode="r") as file:
	
	lines = file.readlines()

	joltage = 0

	for line in lines:

		max_found = -1

		for a_idx in range(0, len(line)):
			for b_idx in range(a_idx+1, len(line)-1):

				a = line[a_idx]
				b = line[b_idx]

				val = int(f"{a}{b}")
				max_found = max(max_found, val)

		joltage += max_found
	
	print(joltage)