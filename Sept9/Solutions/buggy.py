#buggy

MOVES = {'L':(-1,0),'R':(1,0),'U':(0,-1),'D':(0,1)}

def robot(moves):
	global board,start
	b = board.copy()
	pos = start
	for move in moves:
		dr,dc = MOVES[move]
		
r,c = map(int,input().split())

board = []

for i in range(r):
    board.append(input())

moves = input()
start = (0,0)

for row in range(r):
	for col in range(c):
		if board[row][col] == 'R':
			start = (r,c)
			break
	else:
		continue
	break


