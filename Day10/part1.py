import sys
import sympy as sp
from itertools import product

filename = sys.argv[1] if sys.argv[1] else ""

def solve(states, buttons):

	def mod2(M):
		return M.applyfunc(lambda s: s%2)

	n = len(states)
	m = len(buttons)

	b = sp.Matrix(n, 1, lambda i, _: states[i])

	# A_j,i is 1 if button i toggles light j, 0 otherwise
	A = sp.Matrix.zeros(n, m)
	for idx, button in enumerate(buttons):
		for t in button:
			A[t, idx] = 1
	
	solutions = []
	for bits in product([0, 1], repeat=m):
		x = sp.Matrix(bits).reshape(m, 1)
		if mod2(A * x) == b:
			solutions.append(bits)
	
	return min([sum(solution) for solution in solutions])

with open(filename, mode="r") as file:
	
	lines = [line.strip().split(" ") for line in file.readlines()]

	n = len(lines)

	lights = [line[0] for line in lines]
	lights = [
		[0 if c == "." else 1 for c in light.strip("[]")]
		for light in lights
	]

	buttons = [line[1:len(line)-1] for line in lines]
	buttons = [
		[list(map(int, t.strip("()").split(","))) for t in puzzle]
		for puzzle in buttons
	]

	num_presses = 0
	for idx, (light, button) in enumerate(zip(lights, buttons)):
		num_presses += solve(light, button)
		print(f"Solved {idx+1} of {n} puzzles!")

	print(num_presses)