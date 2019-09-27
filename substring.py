# substring

def magic(A,B):
    SIZE = len(A)

    for size in range(SIZE,0,-1):

        for p1 in range(0,SIZE+1-size):

            a = A[p1:p1+size]

            for p2 in range(0,SIZE+1-size):

                b = B[p2:p2+size]

                for s in set(a):
                    if a.count(s) != b.count(s):
                        break
                else:
                    return (a)

    return ('NONE')

for n in range(int(input())):

    A = input()
    B = input()

    print(magic(A,B))
