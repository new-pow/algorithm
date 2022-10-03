# 2583.py

from argparse import Action
# import sys
# input = sys.stdin.readline

def dfs(x,y,area):
    area += 1
    visit[x][y] = True
    for i in range(len(dx)):
        nx = x+dx[i]
        ny = y+dy[i]
        print(nx, ny)
        if nx>=0 and ny>=0 and nx<m and ny<m:
            if paper[nx][ny] == False and visit[nx][ny] == False:
                print("action")
                dfs(nx,ny,area)
            else:
                print("noaction")
        else:
            print("pass")
    return area

n, m, k = map(int, input().split())
paper = [[False]*m for _ in range(n)]
visit = [[False]*m for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
areas = []
area = 0

for i in range(k):
    y1, x1, y2, x2 = map(int, input().split())
    for j in range(x1,x2):  # 그래프 완료
        for k in range(y1,y2):
            paper[j][k] = True

    print(paper)
    print(visit)

    for j in range(n):  # dfs
        for k in range(m):
            if paper[j][k] == False and visit[j][k] == False:
                area = 0
                dfs(j,k,area)
                print(area)
                areas.append(area)
    
    print(areas)