import sys
from itertools import combinations

filename = sys.argv[1] if sys.argv[1] else ""

def dst2(a, b):
	x1, y1, z1 = a
	x2, y2, z2 = b
	
	return (x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2

with open(filename, mode="r") as file:
	
	# parse lines into tuple coordinates
	lines = [line.strip().split(",") for line in file.readlines()]
	coords = [tuple([int(coord) for coord in line]) for line in lines]

	N = len(coords)
	parent = [i for i in range(N)]
	size = [1 for _ in range(N)]

	def find_parent(x):
		while parent[x] != x:
			parent[x] = parent[parent[x]]
			x = parent[x]
		return x
	
	def union_tree(a, b):
		adx = find_parent(a)
		bdx = find_parent(b)

		if adx == bdx:
			return
		
		if size[adx] < size[bdx]:
			adx, bdx = bdx, adx

		parent[bdx] = adx
		size[adx] += size[bdx]

	edges = []
	for combo in combinations(range(N), 2):
		adx, bdx = combo
		distance = dst2(coords[adx], coords[bdx])
		edges.append((distance, adx, bdx))
	edges.sort(key = lambda x: x[0])

	for edge in edges:
		union_tree(edge[1], edge[2])
		
		if N in size:
			a = coords[edge[1]]
			b = coords[edge[2]]
			print(a[0] * b[0])
			break
