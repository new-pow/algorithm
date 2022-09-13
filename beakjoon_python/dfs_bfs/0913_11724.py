# 0913_11724.py
# 연결 요소의 개수 https://www.acmicpc.net/problem/11724 푸는 중

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(x):
    visit[x]=True
    for i in range(1, n+1):
        if graph[x][i] == True and visit[i] == False:
            dfs(i)


n, m = map(int, input().split())
nums = [0]
visit = [True]
graph = [[False]*(n+1) for _ in range(n+1)]
for i in range(n):
    nums.append(i+1)
    visit.append(False)

for _ in range(m):
    s, e = map(int, input().split())
    graph[s][e] = graph[e][s] = True

result = 0

for i in range(1, n+1):
    if not visit[i]:
        dfs(i)
        result += 1

print(result)