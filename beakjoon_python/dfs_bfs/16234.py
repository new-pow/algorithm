# 16234.py

from collections import deque
import sys
input = sys.stdin.readline

def bfs(a,b):
    open = []
    q = deque()
    q.append((a,b))
    while q:
        x, y = q.popleft()
        for i in range(len(dx)):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny<0 or nx>n-1 or ny>n-1:
                continue
            else:
                print("action")
                if abs(land[x][y]-land[nx][ny])>=l and abs(land[x][y]-land[nx][ny])<=r and open[x][y]=="BLANK":
                    open.append([x,y])
                    open.append([nx,ny])
            

n, l, r = map(int, input().split())
land = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]
day = 0

for i in range(n):
    population = list(map(int, input().split()))
    line = ["BLANK"]*len(population)
    land.append(population)
    open.append(line)
    
bfs(0,0)

print(land)
print(open)