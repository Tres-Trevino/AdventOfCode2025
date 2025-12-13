import sys
from collections import deque
from array import array

filename = sys.argv[1] if sys.argv[1] else ""

with open(filename, mode="r") as file:
	
	lines = [line.strip().split(",") for line in file.readlines()]
	coords = [(int(line[0]), int(line[1])) for line in lines]
	
	n = len(coords)
	xs, ys = set(), set()
	for x, y in coords:
		xs.add(x)
		xs.add(x + 1)
		ys.add(y)
		ys.add(y + 1)

	minx = min(x for x, _ in coords)
	maxx = max(x for x, _ in coords)
	miny = min(y for _, y in coords)
	maxy = max(y for _, y in coords)

	xs.add(minx - 1); xs.add(maxx + 2)
	ys.add(miny - 1); ys.add(maxy + 2)

	Bx = sorted(xs)
	By = sorted(ys)
	xidx = {v: i for i, v in enumerate(Bx)}
	yidx = {v: i for i, v in enumerate(By)}

	nx = len(Bx) - 1
	ny = len(By) - 1
	dx = [Bx[i + 1] - Bx[i] for i in range(nx)]
	dy = [By[j + 1] - By[j] for j in range(ny)]

	boundary = [bytearray(ny) for _ in range(nx)]

	def mark_h(y, x1, x2):
		j = yidx[y]
		a, b = (x1, x2) if x1 <= x2 else (x2, x1)
		i1 = xidx[a]
		i2 = xidx[b + 1]
		for i in range(i1, i2):
			boundary[i][j] = 1

	def mark_v(x, y1, y2):
		i = xidx[x]
		a, b = (y1, y2) if y1 <= y2 else (y2, y1)
		j1 = yidx[a]
		j2 = yidx[b + 1]
		for j in range(j1, j2):
			boundary[i][j] = 1

	for k in range(n):
		x1, y1 = coords[k]
		x2, y2 = coords[(k + 1) % n]
		if y1 == y2:
			mark_h(y1, x1, x2)
		else:
			mark_v(x1, y1, y2)

	outside = [bytearray(ny) for _ in range(nx)]
	dq = deque()
	if not boundary[0][0]:
		outside[0][0] = 1
		dq.append((0, 0))

	while dq:
		i, j = dq.popleft()
		if i > 0 and not boundary[i - 1][j] and not outside[i - 1][j]:
			outside[i - 1][j] = 1; dq.append((i - 1, j))
		if i + 1 < nx and not boundary[i + 1][j] and not outside[i + 1][j]:
			outside[i + 1][j] = 1; dq.append((i + 1, j))
		if j > 0 and not boundary[i][j - 1] and not outside[i][j - 1]:
			outside[i][j - 1] = 1; dq.append((i, j - 1))
		if j + 1 < ny and not boundary[i][j + 1] and not outside[i][j + 1]:
			outside[i][j + 1] = 1; dq.append((i, j + 1))

	pref = [array('Q', [0]) * (ny + 1) for _ in range(nx + 1)]
	for i in range(nx):
		row_pref = pref[i + 1]
		prev_row = pref[i]
		run = 0
		wi = dx[i]
		outrow = outside[i]
		for j in range(ny):
			if outrow[j]:
				run += wi * dy[j]
			row_pref[j + 1] = prev_row[j + 1] + run

	def forbidden_area(i1, i2, j1, j2):
		return pref[i2][j2] - pref[i1][j2] - pref[i2][j1] + pref[i1][j1]

	best = 0
	for a in range(n):
		x1, y1 = coords[a]
		for b in range(a + 1, n):
			x2, y2 = coords[b]
			area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
			if area <= best:
				continue

			xmin, xmax = (x1, x2) if x1 <= x2 else (x2, x1)
			ymin, ymax = (y1, y2) if y1 <= y2 else (y2, y1)

			i1 = xidx[xmin]
			i2 = xidx[xmax + 1]
			j1 = yidx[ymin]
			j2 = yidx[ymax + 1]

			if forbidden_area(i1, i2, j1, j2) == 0:
				best = area

	print(best)
