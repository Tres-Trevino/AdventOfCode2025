import sys
from itertools import combinations

filename = sys.argv[1] if sys.argv[1] else ""

def find_area(a, b):
	width = abs(a[0] - b[0]) + 1
	height = abs(a[1] - b[1]) + 1
	return width * height

with open(filename, mode="r") as file:
	
	lines = [line.strip().split(",") for line in file.readlines()]
	coords = [(int(line[0]), int(line[1])) for line in lines]
	
	max_area = 0
	for combo in combinations(coords, 2):
		a, b = combo

		max_area = max(max_area, find_area(a,b))

	print(max_area)
	