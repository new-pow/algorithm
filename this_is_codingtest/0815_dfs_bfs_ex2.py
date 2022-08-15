# 0815_dfs_bfs_ex2.py

# n*m 크기의 직사각형 미로
# 동빈이의 위치는 (1,1)이며 미로의 출구는 (n,m)의 위치에 있다. 한번에 한칸씩 이동할 수 있다.
# 이때 괴물이 있는 부분은 0, 없는 부분은 1로 표시되어 있다.
# 동빈이 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구해보자. 칸을 셀때는 시작칸과 마지막 칸을 모두 포함해서 계산

# 해답풀이
from collections import deque

def move(x,y):
    queue = deque()
    queue.append((x,y))
    # 큐가 빌때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x+dx[i]
            ny = y+dx[i]
            # 미로 공간 벗어난경우 무시
            if nx==0 and ny==0:
                continue
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny] = graph[x][y]+1
                print(nx,ny)
                queue.append((nx,ny))

    return graph[n-1][m-1]

# 1. 미로 입력
n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))

print(graph)

# 방향벡터
dx=[1,-1,0,0]
dy=[0,0,1,-1]

print(move(0,0))