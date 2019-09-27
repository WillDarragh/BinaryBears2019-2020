# warehouse


T = int(input())

for t in range(T):
    D = {}
    N = int(input())
    for n in range(N):
        toy, count = input().split()
        if toy in D:
            D[toy] += int(count)
        else:
            D[toy] = int(count)

    print(len(D))
    for key, val in sorted([(key, val) for key, val in sorted([(key, val) for key, val in D.items()],key=lambda x: x[0].lower())],key=lambda x: x[1],reverse=True):
        print(key,val)
