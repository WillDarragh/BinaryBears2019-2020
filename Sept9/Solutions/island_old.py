from pprint import pprint

def processLand(grid,r,c,x,y,land=False):

    if(x<0 or y<0 or x>=r or y>=c):
        return 0
    elif(grid[y][x]=="L" or grid[y][x]=="C"):
        if(x<0 or y<0 or x>=r or y>=c):
            return 0
        if(grid[y][x]=="L"):
            land=True
        grid[y][x]="."
        land = processLand(grid,r,c,x+1,y,land) or processLand(grid,r,c,x-1,y,land) or processLand(grid,r,c,x,y+1,land) or processLand(grid,r,c,x,y-1,land) or land
        return land
    else:
        return 0

def processWater(grid,r,c,x,y):
    if(x<0 or y<0 or x>=r or y>=c):
        return 0
    elif(grid[y][x]=="W"):
        grid[y][x]="w"
        processWater(grid,r,c,x+1,y)
        processWater(grid,r,c,x-1,y)
        processWater(grid,r,c,x,y+1)
        processWater(grid,r,c,x,y-1)
    return 0

def process(grid,r,c,x,y):
    if(grid[y][x]=='W'):
        return processWater(grid,r,c,x,y)
    else:
        return processLand(grid,r,c,x,y)

c,r = [int(i) for i in input().split()]
grid = []
for i in range(c):
    grid.append(list(input()))

total = 0

for y in range(c):
    for x in range(r):
        total+=process(grid,r,c,x,y)

print(total)
