# 0911_11866.py
# 요세푸스 문제 0 https://www.acmicpc.net/problem/11866 풀이 완료

from collections import deque

q = deque()
result = []
n, k = map(int, input().split())
for i in range(1, n+1):
    q.append(i)

while q:
    # q.append(q.popleft()) # 이부분이 틀림... 3만 생각했다...;
    # q.append(q.popleft())
    # result.append(q.popleft())
    for i in range(k-1):
        q.append(q.popleft())
    result.append(q.popleft())

print('<', end="")
for i in range(len(result)):
    if i==len(result)-1:
        print(result[i], end="")
    else:
        print(result[i], end=", ")
print('>')