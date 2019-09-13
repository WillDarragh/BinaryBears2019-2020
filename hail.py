# hail stones

N = input()
while(N):
    n = int(N)

    i = 0
    while(n > 1):
        if n%2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        i += 1

    print(f'{i-2} steps were necessary for {N}.')

    N = input()
