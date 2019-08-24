import statistics as stat

n = int(input())

X = list(map(float,input().split()))
Y = list(map(float,input().split()))

Z = list(zip(X,Y))

sx = stat.stdev(X)
sy = stat.stdev(Y)

mx = stat.mean(X)
my = stat.mean(Y)

E = sum(x*y for x,y in Z)

numer = E-(n*mx*my)
denom = (n-1)*sx*sy

p = numer/denom

print('The correlation between your X and Y variables is {:0<4}.'.format(round(p,2)))
