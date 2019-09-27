# Last factorial

from math import factorial

FAC = {0:1,1:1}

N = int(input())

for n in range(N):
    x = int(input())

    if x in FAC:
        print(str(FAC[x])[-1])

    else:
        res = 1
        for i in range(0,x+1):
            if i in FAC:
                res = FAC[i]
            else:
                res = i*FAC[i-1]
                FAC[i] = res
        print(str(FAC[x])[-1])
