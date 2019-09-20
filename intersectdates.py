# intersectdates

from datetime import date,timedelta

DAY = timedelta(days=1)

def printy(date):
    y,m,d = str(date).split('-')
    return f'{d}/{m}/{y}'

def datify(string):
    y = string[:4]
    m = string[4:6]
    d = string[6:]
    y,m,d = map(int, [y,m,d])
    return date(y,m,d)

case = 1

NX, NR = map(int,input().split())
while not (NX == 0 and NR == 0):

    NXs = []
    for nx in range(NX):
        d1,d2 = map(lambda x: datify(x), input().split())
        for pair in NXs[::-1]:
            p1,p2 = pair
            if d1 > p1:
                if d1 > p2:
                    NXs.append([d1,d2])
                    break
                if d2 > p2:
                    pair[1] = d2
                    break
        else:
            for pair in NXs:
                p1,p2 = pair
                if d2 < p2:
                    if d2 < p1:
                        NXs.append([d1,d2])
                        break
                    if d1 < p1:
                        pair[0] = d1
                        break
            else:
                NXs.append([d1,d2])

    NXs.sort()
    NXf = []

    skip = False
    for nx in range(len(NXs)):
        if skip:
            skip = False
            continue
        if nx < len(NXs)-1:
            if NXs[nx+1][0] == NXs[nx][1]+DAY:
                NXf.append([NXs[nx][0],NXs[nx+1][1]])
                skip = True
                continue
        skip = False
        NXf.append(NXs[nx])

    NRs = []
    for nr in range(NR):
        d1,d2 = map(lambda x: datify(x), input().split())
        for pair in NRs[::-1]:
            p1,p2 = pair
            if d1 > p1:
                if d1 > p2:
                    NRs.append([d1,d2])
                    break
                if d2 > p2:
                    pair[1] = d2
                    break
        else:
            for pair in NRs:
                p1,p2 = pair
                if d2 < p2:
                    if d2 < p1:
                        NRs.append([d1,d2])
                        break
                    if d1 < p1:
                        pair[0] = d1
                        break
            else:
                NRs.append([d1,d2])

    NRs.sort()
    NRf = []

    skip = False
    for nr in range(len(NRs)):
        if skip:
            skip = False
            continue
        if nr < len(NRs)-1:
            if NRs[nr+1][0] == NRs[nr][1]+DAY:
                NRf.append([NRs[nr][0],NRs[nr+1][1]])
                skip = True
                continue
        skip = False
        NRf.append(NRs[nr])

    final = []

    for nr in NRf:
        r1,r2 = nr
        for nx in NXf:
            x1,x2 = nx
            if r1 > x1:
                if r1 > x2:
                    final.append([r1,r2])
                    break
                if r2 > x2:
                    final.append([x2+DAY,r2])
                    break
                else:
                    break
        else:
            for nx in NXf:
                x1,x2 = nx
                if r2 < x2:
                    if r2 < x1:
                        final.append([r1,r2])
                        break
                    if r1 < x1:
                        final.append([r1,x1-DAY])
                        break
                    else:
                        break
            else:
                final.append([r1,r2])

    #print(NRf)
    #print(NXf)
    #print(final)
    FINAL = []

    for f in final:
        if f[0] == f[1]:
            FINAL.append([f[1]])
        elif f[0] > f[1]:
            FINAL.append([f[1],f[0]])
        else:
            FINAL.append(f)

    #print(NRf)
    #print(NXf)
    #print(FINAL)
    print(f'Case {case}:')
    if not FINAL:
        print('\tNo additional quotes are required')
    else:
        for f in FINAL:
            print(f'\t',end='')
            if len(f)==1:
                print(printy(f[0]))
            else:
                print(f'{printy(f[0])} to {printy(f[1])}')
    case += 1
    NX,NR = map(int,input().split())
