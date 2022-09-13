# 0913_1012.py
# 유기농 배추 https://www.acmicpc.net/problem/1012 풀이완료!

import sys
sys.setrecursionlimit(10000)

def dfs(x,y):
    v[x][y]=-1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx >= 0 and nx<m and ny>=0 and ny<n:
            if land[nx][ny]==1 and v[nx][ny]==0:
                dfs(nx,ny)

t = int(input()) # 테스트 개수
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(t):
    m, n, k = map(int, input().split())
    
    result = 0

    land = [[0]*n for _ in range(m)]
    v = [[0]*n for _ in range(m)]

    for i in range(k):
        x,y = map(int, input().split())
        land[x][y] = 1

    for i in range(m):
        for j in range(n):
            if land[i][j] ==1 and v[i][j] == 0:
                dfs(i,j)
                result +=1
    print(result)
