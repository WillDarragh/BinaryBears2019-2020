#Written by Harrison (and a tiny bit by Will)

def expand(x,y,n):
    global points, grid
    num = grid[y][x]
    if(x>0 and grid[y][x-1] == '0'):
        grid[y][x-1] = num + 1
        points.append((x-1,y))
    if(x<n-1 and grid[y][x+1] == '0'):
        grid[y][x+1] = num + 1
        points.append((x+1,y))
    if(y>0 and grid[y-1][x] == '0'):
        grid[y-1][x] = num + 1
        points.append((x,y-1))
    if(y<n-1 and grid[y+1][x] == '0'):
        grid[y+1][x] = num + 1
        points.append((x,y+1))

cases = int(input())

for c in range(cases):
    size = int(input())
    ay, ax = map(lambda x: int(x)-1, input().split())
    by, bx = map(lambda x: int(x)-1, input().split())
    grid = []
    for i in range(size):
        grid.append(input().split())

    grid[ay][ax] = 1

    points = [(ax,ay)]
    while(len(points)>0 and int(grid[by][bx])!=grid[by][bx]):
        expand(points[0][0],points[0][1],size)
        points.pop(0)
        
    print(f'There are {grid[by][bx]} squares on the shortest path from ({ay+1},{ax+1}) to ({by+1},{bx+1}).')
