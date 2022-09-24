# 0914_4963.py

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

# dfs
def dfs(x, y):
    visit[x][y] = True
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx>=0 and ny>=0 and nx<h and ny<w:
            if land[nx][ny] == 1 and not visit[nx][ny]:
                dfs(nx,ny)

# input
while True:
    w, h = map(int, input().split())
    if w==0 and h==0:
        break

    land = []
    visit = [[False] * w for _ in range(h)]
    for i in range(h):
        temp = list(map(int, input().split()))
        land.append(temp)

    dx = [-1,1,0,0,-1,-1,1,1]
    dy = [0,0,-1,1,-1,1,-1,1]
    result = 0

    for i in range(h):
        for j in range(w):
            if land[i][j] == 1 and not visit[i][j]:
                dfs(i,j)
                result += 1

    print(result)