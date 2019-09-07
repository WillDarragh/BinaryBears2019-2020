# Prob5 Windows

d = 1

N = int(input())
while(N!=0):
	W,C = [],[]
	for n in range(N):
		W.append(list(map(int, input().split())))
	M = int(input())
	for m in range(M):
		C.append(list(map(int, input().split())))
	
	print(f'Desktop {d}:')
	
	for c in C:
		win = len(W)
		for w in W[::-1]:
			# Possibly a mistake in judging output which is why there is one <
			if w[0] <= c[0] < w[0]+w[3] and w[1] <= c[1] <= w[1]+w[2]:
				print(f'window {win}')
				break
			win -= 1
		else:
			print('background')


	d += 1
	N = int(input())
