# Water

from itertools import groupby

def get_paths(loc,path):
    global stations, pipes, paths
    path.append(loc)
    #print('loc',loc,'path',path)
    if loc == 2:
        paths.append(path)
        return
    for key in filter(lambda x: x[0]==loc,pipes.keys()):
        #print('key',key)
        new_loc = key[1]
        new_path = list(path)
        if new_loc not in new_path:
            if not new_path[0]:
                new_path[0] = pipes[key]
            elif new_path[0] > pipes[key]:
                    new_path[0] = pipes[key]
            get_paths(new_loc,new_path)

def total():
    global paths
    paths = sorted(paths, key=lambda x: x[-2])
    sep_paths = [list(g) for k,g in groupby(paths,key=lambda x:x[-2])]
    #print(sep_paths)
    S = 0
    for sp in sep_paths:
        S += max(sp, key=lambda x: x[0])[0]
    return(S)

N,P,K = map(int,input().split())

stations = list(range(1,N+1))
pipes = {}

for p in range(P):
    a,b,c = map(int,input().split())
    pipes[(a,b)] = c
    pipes[(b,a)] = c

#print(stations,pipes)

paths = []

get_paths(1,[None])
print(paths)
print(total())

paths = []

for k in range(K):
    a,b,c = map(int,input().split())
    if (a,b) not in pipes:
        pipes[(a,b)] = c
    else:
        pipes[(a,b)] += c
    if (b,a) not in pipes:
        pipes[(b,a)] = c
    else:
        pipes[(b,a)] += c

    get_paths(1,[None])
    #print(pipes)
    print(paths)
    print(total())
