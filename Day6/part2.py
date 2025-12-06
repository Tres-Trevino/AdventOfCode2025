import sys
from functools import reduce

filename = sys.argv[1] if sys.argv[1] else ""

with open(filename, mode="r") as file:
	
	lines = [x.removesuffix('\n') for x in file.readlines()]
	parsedLines = []
	lastFound = 0

	for i in range(len(lines[0])):
		if all([line[i] == " " for line in lines]):
			
			nums = []
			for line in lines:
				num = line[lastFound:i]
				nums.append(num)
			parsedLines.append(nums)

			lastFound = i+1

	nums = []
	for line in lines:
		num = line[lastFound:]
		nums.append(num)
	parsedLines.append(nums)

	total = 0

	for line in parsedLines:

		def add(a, b):
			return a+b
		def mul(a, b):
			return a*b

		nums = line[:len(line)-1]
		op = add if "+" in line[len(line)-1] else mul

		arguments = []
		for i in range(len(nums[0])):

			newNum = ""
			for num in nums:
				newNum += num[i]

			arguments.append(int(newNum))

		temp = reduce(op, arguments)
		total += temp

	print(total)
