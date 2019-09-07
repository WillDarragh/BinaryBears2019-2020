# Prob2 - Spiral

from math import sqrt,atan,sin,cos

R = {0:0}
for t in range(int(input())):
	N = int(input())
	if N-1 not in R:
		for n in range(1,N):
			if n not in R:
				R[n] = R[n-1] + atan(1/sqrt(n))
	r = R[N-1]
	h = sqrt(N)
	x,y = map(lambda a: f'{round(a,4):.4f}', [h*cos(r),h*sin(r)])
	print(x,y)
