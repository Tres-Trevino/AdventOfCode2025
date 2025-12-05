import sys
filename = sys.argv[1] if sys.argv[1] else ""

with open(filename, mode="r") as file:
	
	lines = [x.strip() for x in file.readlines()]

	split = lines.index("")
	rangesText = lines[0:split]
	itemsText = lines[split+1:]


	# parse ranges
	ranges = []
	for rangeItem in rangesText:
		x = rangeItem.split("-")
		beg, end = x
		beg, end = int(beg), int(end)
		ranges.append(range(beg, end+1))
	
	# parse items
	numSpoiled = 0
	for item in itemsText:
		item = int(item)

		if any([item in rangeItem for rangeItem in ranges]):
			numSpoiled += 1

		
	print(numSpoiled)