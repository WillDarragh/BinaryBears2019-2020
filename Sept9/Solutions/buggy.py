#buggy

from pprint import pprint
from copy import deepcopy
from itertools import product

MOVES = {'L':(0,-1),'R':(0,1),'U':(-1,0),'D':(1,0)}

# Could implement encoding and decoding for maximum efficiency
'''
def enc(moves):
	new_moves = []
	curr = 0
	for i in range(1,len(moves)//2):
		while(curr != len(moves)):
			count = 1
			group = moves[curr:curr+i]
			while(moves[curr+i:curr+2*i] == group):
				count += 1
				curr += i
			new_moves.append((group,count))
			curr += i
	return new_moves

def dec(moves):
	return
'''

def oob(pos):
	global R,C,board
	r,c = pos
	return (not (0 <= r < R and 0 <= c < C)) or board[r][c] == '#'

def robot(moves):
	global board,start
	b = deepcopy(board)
	pos = start
	for move in moves:
		r,c = pos
		dr,dc = MOVES[move]
		new_pos = (r+dr,c+dc)
		if not oob(new_pos):
			new_r,new_c = new_pos
			b[r][c] = '.'
			b[new_r][new_c] = 'R'
			if board[new_r][new_c] == 'E':
				return True
			pos = new_pos
	return False
		
def changes(moves, count):
	if count == 2:
		return False
	if robot(moves):
		return False
	lists = [list(range(len(moves))) for i in range(count)]
	things = list(product(*lists))
	for thing in things:
		new_moves = moves.copy()
		for part in thing:
			for m in MOVES.keys():
				new_moves[part] = m
				if robot(new_moves):
					return False
	return True
	
R,C = map(int,input().split())

board = []

for r in range(R):
    board.append(list(input()))

moves = list(input())
start = (0,0)

for r in range(R):
	for c in range(C):
		if board[r][c] == 'R':
			start = (r,c)
			break
	else:
		continue
	break

count = 0
while (changes(moves, count)):
	count += 1
print(count)
