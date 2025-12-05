import sys

filename = sys.argv[1] if sys.argv[1] else ""

def isValid(id: str) -> bool:

	if len(id) % 2 != 0:
		return True
	
	halfway = len(id) // 2
	beg = id[0:halfway]
	end = id[halfway:]

	return beg != end

with open(filename, mode="r") as file:
	
	content = file.readline()
	ids = content.split(",")

	sum = 0

	for id in ids:
		beg, end = id.split("-")
		beg, end = int(beg), int(end)

		for i in range(beg, end+1):
			
			if not isValid(str(i)):
				sum += i
	
	print(sum)