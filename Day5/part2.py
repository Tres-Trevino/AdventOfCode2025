import sys
# filename = "Day5/test.txt"
filename = sys.argv[1] if sys.argv[1] else ""

with open(filename, mode="r") as file:
	
	lines = [x.strip() for x in file.readlines()]

	split = lines.index("")
	rangesText = lines[0:split]
	itemsText = lines[split+1:]

	totalRange = 0

	ranges = []

	# parse ranges
	for rangeItem in rangesText:
		x = rangeItem.split("-")
		beg, end = x
		beg, end = int(beg), int(end)
		rangeObj = range(beg, end+1)
		ranges.append(rangeObj)

	ranges = list(set(ranges))

	intervals = [(r.start, r.stop) for r in ranges]

	# Sort intervals by start
	intervals.sort()

	merged = []
	cur_start, cur_end = intervals[0]

	for start, end in intervals[1:]:
		if start <= cur_end:
			cur_end = max(cur_end, end)
		else:
			merged.append(range(cur_start, cur_end))
			cur_start, cur_end = start, end

	merged.append(range(cur_start, cur_end))

	print(merged)

	print(sum([len(rang) for rang in merged]))

# not 347152476137554
# not 320807242916566
# not 310540277678765
# not 131263188991116

# try 321658113405502
