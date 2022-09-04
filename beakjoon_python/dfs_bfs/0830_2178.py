# 0830_2178.py

from collections import deque


def bfs(i,j):
    queue = deque()
    queue.append((i,j))

    while queue:
        i, j = queue.popleft()

        for a in range(4):
            nx = i + dx[a]
            ny = j + dx[a]

            # 위치가 벗어나면 안되기 때문에 조건 추가
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            # 벽이므로 진행 불가
            if miro[nx][ny] == 0:
                continue
            
            # 벽이 아니므로 이동
            if miro[nx][ny] == 1:
                miro[nx][ny] = miro[i][j] + 1
                queue.append((nx, ny))
                
    return miro[n-1][m-1]


n, m = map(int, input().split())
miro = []

# 이동할 방향
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(n):
    miro.append(list(map(int, input())))
print(miro)

print(bfs(0,0))
