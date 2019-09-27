# Trominos

from math import log, ceil

for n in range(int(input())):
    x, y = map(int,input().split())

    order = 1

    if x>0 and y>0:
        order = ceil(log(max([x,y]),2))

    rotate = 0

    while(order > 3):

        size = 2**order

        if x < size/2 and y < size/2 and not ( x >= size/4 and y >= size/4 ):
            x = size/2 - x
            y = size/2 - y
        elif x >= size/2 and y < size/2 and not ( x < 3*size/4 and y >= size/4 ):
            x -= size/2
            newx = y
            newy = size/2-1-x
            x = newx
            y = newy
            rotate += 1
        elif x < size/2 and y >= size/2 and not ( x >= size/4 and y < 3*size/4 ):
            y -= size/2
            newy = x
            newx = size/2-1-y
            x = newx
            y = newy
            rotate -= 1
        else:
            x -= size/4
            y -= size/4
            x = size/2 - x
            y = size/2 - y

        order -= 1    

    #print('ord',order)

    #print(x,y)

    res = 0 

    if order == 1:
        res = 0
    elif order == 2:
        if x == y or x+1==y or x == y+1:
            res = 0 
        elif x >= 1:
            res = 1
        else:
            res = 3
    else:
        #print('x',x,'y',y)
        y -= x
        y %= 8
        x %= 4
        #print('x',x)
        if x == 0:
            if y/2%2==0:
                res = 0 
            else:
                res = 1
        elif x == 1:
            if y in [0,1,3,7]:
                res = 0 
            else:
                res = 1
        elif x == 2:
            if y in [0,1]:
                res = 0
            elif y in [2,3,4,7]:
                res = 1
            elif y == 5:
                res = 2
            else:
                res = 3
        else:
            if y in [0,1]:
                res = 0 
            elif y in [2,7]:
                res = 1
            elif y in [3,4]:
                res = 2
            else:
                res = 3

    res -= rotate
    res %= 4
    print(res)
        
