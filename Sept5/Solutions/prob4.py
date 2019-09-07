# Prob4 Word Search

grid = []
for i in range(10):
	grid.append(input())

rgrid = list(zip(*grid))
rgrid = [''.join(row) for row in rgrid]

diags = 	[ ''.join([grid[x][y] for x,y in zip(range(10),range(10))]) ]
diags.append(	[ ''.join([grid[x][y] for x,y in zip(range(10),range(9,-1,-1))]) ])

for t in range(int(input())):

	notfound = True

	word = input()
	rword = ''.join(word[::-1])

	# Horiz
	for row in grid:
		if word in row or rword in row:
			notfound = print(f'{word} was found horizontally.')

	# Vert
	for row in rgrid:
		if word in row or rword in row:
			notfound = print(f'{word} was found vertically.')
	# Diag
	for d in diags:
		if word in d or rword in d:
			notfound = print(f'{word} was found diagonally.')

	# Not
	if notfound:
		print(f'{word} was not found.')
