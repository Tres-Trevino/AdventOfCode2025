import sys
from functools import cache

filename = sys.argv[1] if sys.argv[1] else ""

with open(filename, mode="r") as file:
	
	lines = [line.strip().split(" ") for line in file.readlines()]

	# Assemble states dict
	states = {}
	for line in lines:
		parent = line[0][:-1]
		children = line[1:]

		states[parent] = children

	start_node = "svr"
	required_nodes = {"dac", "fft"}
	target_node = "out"

	@cache
	def dfs(node, seen_required):

		if node == target_node:
			return int(seen_required == required_nodes)

		new_seen_required = seen_required | ({node} if node in required_nodes else set())

		return sum(
			dfs(child, new_seen_required)
			for child in states.get(node, [])
		)

	paths = dfs(start_node, frozenset())
	print(paths)