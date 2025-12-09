import sys
from itertools import combinations
import math
import heapq
from functools import reduce

filename = sys.argv[1] if sys.argv[1] else ""
iterations = 10 if filename == "test.txt" else 1000

def dst2(a, b):
	x1, y1, z1 = a
	x2, y2, z2 = b
	
	return (x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2

with open(filename, mode="r") as file:
	
	lines = [line.strip().split(",") for line in file.readlines()]
	coords = [tuple([int(coord) for coord in line]) for line in lines]

	N = len(coords)
	parent = [i for i in range(N)]
	size = [1 for _ in range(N)]

	def find(x):
		while parent[x] != x:
			parent[x] = parent[parent[x]]
			x = parent[x]
		return x
	
	def union(a, b):
		adx = find(a)
		bdx = find(b)

		if adx == bdx:
			return False # already in the same family
		
		if size[adx] < size[bdx]:
			adx, bdx = bdx, adx

		parent[bdx] = adx
		size[adx] += size[bdx]

		return True

	edges = []
	for combo in combinations(range(N), 2):
		adx, bdx = combo
		distance = dst2(coords[adx], coords[bdx])
		edges.append((distance, adx, bdx))

	edges.sort(key = lambda x: x[0])


	for i in range(iterations):
		edge = edges[i]
		union(edge[1], edge[2])

	largest = heapq.nlargest(3, size)
	print(reduce(lambda x, y: x*y, largest))
