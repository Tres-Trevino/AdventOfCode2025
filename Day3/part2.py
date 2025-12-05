import sys

filename = sys.argv[1] if sys.argv[1] else ""

def findGreatestSubstring(substr: str, num_select: int):

	if num_select == 0:
		return ""
	if len(substr) == num_select:
		return substr
	
	end = len(substr) - num_select

	window = substr[:end+1]
	best_digit = max(window)
	idx = window.find(best_digit)

	return best_digit + findGreatestSubstring(substr[idx+1:], num_select-1)


with open(filename, mode="r") as file:
	
	lines = file.readlines()

	joltage = 0

	for line in lines:
		line = line.strip()

		result = findGreatestSubstring(line, 12)
		joltage += int(result)
	
	print(joltage)
