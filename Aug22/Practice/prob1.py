
ones = ['zero','one','two','three','four','five','six','seven','eight','nine']
teens = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tens = ['twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']

huns = ones + teens

for t in tens:
	huns.append(t)
	for o in ones[1:]:
		huns.append((t+'-'+o))

def digs3(x):
	result = ''
	if len(x) == 3:
		result = ones[int(x[0])]+'hundred '
		result += huns[int(x[1:])]
	else:
		print(int(x))
		result = huns[int(x)]
	return(result)
	

n = int(input())

for i in range(n):
	d,c = input().split('.')

	print(digs3(d))
