# 0906_9205.py
from collections import deque
from queue import Empty
import sys
# input = sys.stdin.readline().rstrip()

# def walk
def walk(x1,y1,q, mood):
    if q is Empty:
        return
    (x2,y2) = q.popleft()
    if (x2-x1)+(y2-y1) > 1000:
        mood = "sad"
    walk(x2,y2,q,mood)


# 테스트 케이스의 개수 t가 주어진다. (t ≤ 50)
t = int(input())
mood = "happy"

for _ in range(t):
    # 맥주를 파는 편의점의 개수 n이 주어진다. (0 ≤ n ≤ 100)
    n = int(input())
    q = deque()
    # 좌표 입력
    for _ in range(n+2):
        x,y = map(int, input().split())
        q.append((x,y))
    (x1, y1) = q.popleft()
    walk(x1,y1,q, mood)
    print(mood)

