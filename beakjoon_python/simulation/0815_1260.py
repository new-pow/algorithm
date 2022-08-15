# 0815_1260.py

# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

# 풀이
## 함수정의1 : DFS
def dfs(v):
    visit1[v]=1
    print(v, end=" ")
    for i in range(1, n+1):
        if graph[i][v] == 1 and visit1[i]==0:
            dfs(i)

## 함수정의2 : BFS
def bfs(v):
    queue = deque()
    queue.append(v)
    visit2[v]=1

    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in range(1, n+1):
            if graph[i][v] == 1 and visit2[i]==0:
                queue.append(i)
                visit2[i]=1


## 임포트
from collections import deque
## 입력
n,m,v = map(int, input().split())
## 그래프 만들기
graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    x,y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1
visit1 = [0]*(n+1)
visit2 = [0]*(n+1)

dfs(v)
print()
bfs(v)