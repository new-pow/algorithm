# 0905_2468.py
# 안전영역: https://www.acmicpc.net/problem/2468 풀이 완료!

from collections import deque

# bfs 함수
def bfs(x,y,i):
    queue = deque()
    sink[x][y]==True
    queue.append((x,y))

    while queue :
        x, y = queue.popleft()

        for j in range(4):
            nx = x+ dx[j]
            ny = y+ dy[j]

            if nx>=0 and nx<n and ny>=0 and ny<n:
                if sink[nx][ny] == False and city[nx][ny]>=i:
                    sink[nx][ny] = True
                    queue.append((nx,ny))


# 그래프 그리기
n = int(input())
city = []
result = 0
maxNum = 0
minNum = 9
for i in range(n):
    graph = list(map(int, input().split()))
    city.append(graph)
    
    for j in range(n):
        if city[i][j]>maxNum:
            maxNum = city[i][j]
        if city[i][j]<minNum:
            minNum = city[i][j]5

dx = [1,-1,0,0]
dy = [0,0,1,-1]

# 물이 스며들었을 때 방문 배열
for i in range(minNum, maxNum):
    temp_num = 0
    sink = [[False]*n for _ in range(n)]

    for x in range(n):
        for y in range(n):
            if sink[x][y] == False and city[x][y]>=i:
                bfs(x,y,i)
                temp_num += 1
                
    if result<temp_num:
        result = temp_num

print(result)

# 안전지역 개수 구하기
