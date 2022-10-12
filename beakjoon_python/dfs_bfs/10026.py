# 10026.py
# 적록색약 https://www.acmicpc.net/problem/10026

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

#DFS
def dfs(a,b):
    visit[a][b] = True
    for i in range(4):
        x = a+dx[i]
        y = b+dy[i]
        if x>=0 and y>=0 and x<n and y<n:
            if visit[x][y]==False and grid[x][y]==grid[a][b]:
                dfs(x,y)

# 입력 및 연산
n = int(input())
grid = []

for i in range(n):
    temp = list(input().replace('\n',''))
    grid.append(temp)

visit = [[False]*n for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
count_all = 0
count_rg = 0

for i in range(n):
    for j in range(n):
        if visit[i][j] == False:
            dfs(i,j)
            count_all += 1
            
for i in range(n):
    for j in range(n):
        if grid[i][j] == 'R':
            grid[i][j] = 'G'

visit = [[False]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visit[i][j] == False:
            dfs(i,j)
            count_rg += 1


print(count_all, end=' ')
print(count_rg)