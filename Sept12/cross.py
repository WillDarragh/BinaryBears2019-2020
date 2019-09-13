# cross

P = input()

n = 1

while(P):

    pins = list(map(int,P.split()))

    pairs = []
    for i in range(len(pins)):
        pairs.append((i+1,pins[i]))

    #print(pairs)
    cross = 0
    for p1 in range(len(pairs)):
        for p2 in range(p1+1,len(pairs)):
            if pairs[p2][1] < pairs[p1][1]:
                cross += 1


    
    print(f'There are {cross} wire crossing in routing channel {n}.')

    n += 1
    P = input()
