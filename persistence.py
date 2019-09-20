#persistence

from functools import reduce

n = input()

res = n

count = 0

while(len(res)>1):
    res = str(reduce(lambda a,b : a*b,[int(i) for i in res]))
    count += 1

print(count)
