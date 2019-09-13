# wire

from pprint import pprint

dirs = [(1,0),(-1,0),(0,1),(0,-1)]

short = None

def paths(pos, path):
    global short, grid, br, bc, dirs, N
    if short:
        if path[1] >= short:
            return
    if pos == [br,bc]:
        print(path)
        short = path[1]
        return
    for d in dirs:
        rd,cd = d
        new_path = path.copy()
        new_path[0].append(pos)
        new_path[1] += 1
        new_pos = [pos[0]+rd,pos[1]+cd]
        if new_pos not in path[0]:
            if 0 <= new_pos[0] < int(N) and 0 <= new_pos[1] < int(N):
                newr,newc = new_pos
                if grid[newr][newc] == '0':
                    paths(new_pos, new_path)
    return

N = input()

while(N):
    ar,ac = map(int,input().split())
    br,bc = map(int,input().split())

    grid = []

    for n in range(int(N)):
        grid.append(input().split())

    #pprint(grid)    

    paths([ar,ac],[[],0])  

    print(f'There are {short+1} squares on a shortest path from ({ar},{ac}) to ({br},{bc}).')

    N = input()
