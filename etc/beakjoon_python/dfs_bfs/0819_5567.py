# 0819_5567.py

# 첫째 줄에 상근이의 동기의 수 n (2 ≤ n ≤ 500)이 주어진다.
# 둘째 줄에는 리스트의 길이 m (1 ≤ m ≤ 10000)이 주어진다.
# 다음 줄부터 m개 줄에는 친구 관계 ai bi가 주어진다. (1 ≤ ai < bi ≤ n)
# ai와 bi가 친구라는 뜻이며, bi와 ai도 친구관계이다. 

# 첫째 줄에 상근이의 결혼식에 초대하는 동기의 수를 출력한다.

# 문제풀이1

from collections import deque
from itertools import count


# def dsf(x):
#     for i in range(n):
#         if arr[x][i] == 1:
#             relation_deep[i] += 1


# n = int(input()) # 상근이의 친구수
# m = int(input()) # 친구관계 리스트 길이

# arr = [[0] * (n+1) for _ in range(n+1)]
# relation_deep = [0]*(n+1)

# for _ in range(m):
#     x, y = map(int, input().split())
#     arr[x][y] = arr[y][x] = 1

# count = -1 # 상근이 제외

# for i in range(m):
#      if relation_deep[i] >0 and relation_deep < 3:
#         count +=1
# print(count)

# 문제풀이2 : bfs
def bfs(node):
    queue = deque()
    queue.append(node)
    while queue:
        node = queue.popleft()
        for n in graph[node]:
            if check[n] == 0:
                check[n] = check[node]+1
                queue.append(n)

n = int(input()) # 상근이의 친구수
m = int(input()) # 친구관계 리스트 길이
graph = [[] * (n+1) for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append[y]
    graph[y].append[x]
check = [0]*(n+1)
check[1] = 1
bfs[1]

res = sum(1 for t in check if 2<=t and t<=3)
print(res)

# --

# 런타임 해결책
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
m = int(input())
graph = [ [0] * (n+1) for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(x):
    q = deque()
    visited[x] = 1
    q.append(x)
    while q:
        a = q.popleft()
        for i in graph[a]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[a] + 1

bfs(1)
result = 0
for i in range(2,n+1):
    # 본인이거나 친구거나, 친구의 친구거나 경우의 수가 최대 3개
    if visited[i] < 4 and visited[i] != 0:
        result += 1
print(result)