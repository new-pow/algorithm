# 1697.py
# 숨바꼭질 https://www.acmicpc.net/submit/1697

# import
from collections import deque
import sys
input = sys.stdin.readline

# def bfs
def bfs(x):
    x = q.popleft()
    print(x)
    if not x+1 in visit:
        visit.append(x+1)
        q.append(x+1)
    if not x-1 in visit:
        visit.append(x-1)
        q.append(x-1)
    if not x*2 in visit:
        visit.append(x*2)
        q.append(x*2)
        

# input 받기
n, k = map(int, input().split())
x = n
q = deque()
visit = []
count = 0

# 연산하기
q.append(x)
while True:
    bfs(x)
    if k in q:
        break
    elif k not in q:
        count +=1
# 출력하기
print(count)