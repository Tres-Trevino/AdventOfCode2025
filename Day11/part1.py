import sys

filename = sys.argv[1] if sys.argv[1] else ""

with open(filename, mode="r") as file:
	
	lines = [line.strip().split(" ") for line in file.readlines()]

	# Assemble states dict
	states = {}
	for line in lines:
		parent = line[0][:-1]
		children = line[1:]

		states[parent] = children

	start_state = "you"
	target_state = "out"

	def traverse(state, seen):

		if state == target_state:
			return 1
		if state in seen:
			return 0

		seen = seen.copy()
		seen.add(state)

		return sum(traverse(child, seen) for child in states[state])

	num = traverse(start_state, set())

	print(num)