import sys
import pulp

filename = sys.argv[1] if sys.argv[1] else ""

def solve(states, buttons):

	n = len(states)
	m = len(buttons)

	A = [[0] * m for _ in range(n)]
	for i, button in enumerate(buttons):
		for light in button:
			A[light][i] = 1

	prob = pulp.LpProblem("buttons", pulp.LpMinimize)
	x = [pulp.LpVariable(f"x{i}", lowBound=0, cat="Integer") for i in range(m)]

	prob += pulp.lpSum(x)

	for j in range(n):
		prob += (
			pulp.lpSum(A[j][i] * x[i] for i in range(m)) == states[j],
			f"Light_{j}"
		)
		
	prob.solve(pulp.PULP_CBC_CMD(msg=False))
	
	return int(sum(v.value() for v in x))

with open(filename, mode="r") as file:
	
	lines = [line.strip().split(" ") for line in file.readlines()]
	n = len(lines)

	buttons = [line[1:len(line)-1] for line in lines]
	buttons = [
		[list(map(int, t.strip("()").split(","))) for t in puzzle]
		for puzzle in buttons
	]

	joltages = [line[-1] for line in lines]
	joltages = [
		[int(c) for c in j.strip("{}").split(",")]
		for j in joltages
	]

	num_presses = 0
	for idx, (joltage, button) in enumerate(zip(joltages, buttons)):
		num_presses += solve(joltage, button)
		print(f"Solved {idx+1} of {n} puzzles!")

	print(num_presses)