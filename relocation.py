N,Q = map(int, input().split())

comps = list(map(int, input().split()))

for q in range(Q):
    line = list(map(int,input().split()))
    if line[0] == 1:
        comps[line[1]-1] = line[2]
    else:
        print(abs(comps[line[2]-1]-comps[line[1]-1]))
