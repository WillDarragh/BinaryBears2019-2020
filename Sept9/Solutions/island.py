from pprint import pprint

dirs = [(0,1),(1,0),(0,-1),(-1,0)]

def valid(r,c):
	global R,C,marked
	return (0 <= r < R and 0 <= c < C) and not marked[r][c]

def magic(r,c):
	global grid,marked
	if not valid(r,c):
		return
	marked[r][c] = True
	if grid[r][c] == 'W':
		return
	grid[r][c] = 'L'
	for d in dirs:
		new_r,new_c = r+d[0],c+d[1]
		magic(new_r,new_c)

R,C = map(int,input().split())

grid = []
marked = []

for r in range(R):
	grid.append(list(input()))
	marked.append([False for c in range(C)])

count = 0

for r in range(R):
	for c in range(C):
		if not marked[r][c] and grid[r][c] == 'L':
			count += 1
			magic(r,c)

print(count)
'''
pprint(grid)
pprint(marked)
'''
