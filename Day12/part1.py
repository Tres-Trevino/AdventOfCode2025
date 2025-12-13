import sys
from itertools import chain

filename = sys.argv[1] if sys.argv[1] else ""

class Present:
	size: int
	shape: list[list[str]]

class Region:
	area: int
	dimension: tuple[int, int]
	presents: list[int]

with open(filename, mode="r") as file:
	
	# parse presents
	shapes = []
	buffer = []
	for _ in range(6):
		while (line := file.readline().strip()) != "":
			buffer.append(line)

		shapes.append(buffer[1:])
		buffer.clear()

	presents = []
	for shape in shapes:
		p = Present()
		itr = chain.from_iterable(shape)
		p.size = sum([1 if cell == "#" else 0 for cell in itr])
		p.shape = shape
		presents.append(p)

	# parse regions
	bounds = [line.strip().split(" ") for line in file.readlines()]

	regions = []
	for bound in bounds:
		
		r = Region()
		x, y = bound[0].strip(":").split("x")
		r.dimension = (int(x), int(y))
		r.area = int(x) * int(y)

		r.presents = []
		for cell in bound[1:]:
			r.presents.append(int(cell))
		
		regions.append(r)

	# operate
	num_valid = 0
	for region in regions:

		total_present_area = sum(
			presents[idx].size * present
			for idx, present in enumerate(region.presents)
		)

		if total_present_area <= region.area:
			num_valid += 1


	print(num_valid)

	